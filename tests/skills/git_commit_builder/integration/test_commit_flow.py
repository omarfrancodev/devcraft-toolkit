"""Owned-repository commit recipe controls; coordinator judgment is tested separately."""
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from tests.support.git_fixtures import git_fixture, snapshot_repository
from tests.skills.git_stage_changes.integration.test_index_operations import SAFE


class CommitFlowTests(unittest.TestCase):
    def setUp(self):
        parent=Path(__file__).resolve().parents[3]/".tmp"
        parent.mkdir(parents=True,exist_ok=True)
        self.temp=tempfile.TemporaryDirectory(dir=parent)
        self.root=Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def git(self, repo, *args, data=None, check=True, extra_env=None):
        env={k:v for k,v in os.environ.items() if not k.upper().startswith("GIT_")}
        env.update(GIT_CONFIG_NOSYSTEM="1",GIT_CONFIG_GLOBAL=str(self.root/".fixture-global-config"))
        env.update(extra_env or {})
        return subprocess.run(["git",*SAFE,*args],cwd=repo,env=env,
                              input=data.encode("utf-8") if isinstance(data,str) else data,
                              capture_output=True,check=check)

    def head(self, repo):
        return self.git(repo,"rev-parse","HEAD").stdout.strip()

    def index(self, repo):
        result={}
        for row in self.git(repo,"ls-files","--stage","-z").stdout.split(b"\0"):
            if row:
                meta,path=row.split(b"\t",1)
                mode,oid,stage=meta.split()
                self.assertEqual(b"0",stage)
                result[path]=(mode,oid)
        return result

    def tree(self, repo):
        result={}
        for row in self.git(repo,"ls-tree","-r","-z","HEAD").stdout.split(b"\0"):
            if row:
                meta,path=row.split(b"\t",1)
                mode,kind,oid=meta.split()
                result[path]=(mode,oid)
        return result

    def working(self, repo):
        return {k:v for k,v in snapshot_repository(repo).items() if k.startswith(("working:","working-mode:"))}

    def hook(self, repo, script):
        path=repo/".git"/"hooks"/"pre-commit"
        path.write_bytes(("#!/bin/sh\n"+script+"\n").encode("utf-8"))
        path.chmod(0o755)

    def test_commit_uses_selected_index_and_literal_message(self):
        with git_fixture("normal",self.root) as repo:
            parent=self.head(repo)
            (repo/"README.md").write_bytes(b"Selected rounding fix.\n")
            self.git(repo,"add","--","README.md")
            expected=self.index(repo)
            (repo/"README.md").write_bytes(b"Selected rounding fix.\nExcluded debug.\n")
            (repo/"notes.txt").write_bytes(b"Untracked notes.\n")
            before=self.working(repo)
            message='fix: preserve "$()" and backticks as data\n\nLiteral body.\n'
            self.git(repo,"commit","--file=-","--cleanup=verbatim",data=message)
            self.assertEqual(expected,self.tree(repo))
            raw=self.git(repo,"cat-file","commit","HEAD").stdout
            self.assertEqual(message.encode("utf-8"),raw.split(b"\n\n",1)[1])
            self.assertEqual(parent,self.git(repo,"rev-parse","HEAD^").stdout.strip())
            self.assertEqual(before,self.working(repo))
            self.assertEqual(b"Fixture User <fixture@example.invalid>",self.git(repo,"show","-s","--format=%an <%ae>","HEAD").stdout.strip())
            self.assertEqual(b"",self.git(repo,"diff","--cached","--name-only").stdout)

    def test_unborn_commit_has_no_parent(self):
        with git_fixture("unborn",self.root) as repo:
            (repo/"README.md").write_bytes(b"Initial selected content.\n")
            self.git(repo,"add","--","README.md")
            expected=self.index(repo)
            self.git(repo,"commit","--file=-","--cleanup=verbatim",data="feat: initial selected content\n")
            self.assertEqual(1,len(self.git(repo,"rev-list","--parents","-n","1","HEAD").stdout.split()))
            self.assertEqual(expected,self.tree(repo))

    def test_failing_hook_preserves_pending_state(self):
        with git_fixture("staged",self.root) as repo:
            self.hook(repo,"exit 7")
            before_head=self.head(repo); before_index=self.index(repo); before_work=self.working(repo)
            result=self.git(repo,"commit","--file=-","--cleanup=verbatim",data="feat: selected content\n",check=False)
            self.assertNotEqual(0,result.returncode)
            self.assertEqual(before_head,self.head(repo))
            self.assertEqual(before_index,self.index(repo))
            self.assertEqual(before_work,self.working(repo))

    def test_hook_added_content_is_detectably_outside_expected_tree(self):
        with git_fixture("staged",self.root) as repo:
            self.hook(repo,"printf '%s\\n' 'Unexpected hook content.' > hook-added.txt\ngit add -- hook-added.txt")
            expected=self.index(repo); before=self.head(repo)
            result=self.git(repo,"commit","--file=-","--cleanup=verbatim",data="feat: selected content\n")
            self.assertEqual(0,result.returncode)
            self.assertNotEqual(before,self.head(repo))
            self.assertNotEqual(expected,self.tree(repo))
            self.assertIn(b"hook-added.txt",self.tree(repo))
            self.assertTrue((repo/"hook-added.txt").exists())

    def test_second_group_failure_preserves_first_commit(self):
        with git_fixture("normal",self.root) as repo:
            parent=self.head(repo)
            (repo/"README.md").write_bytes(b"First selected group.\n")
            self.git(repo,"add","--","README.md")
            self.git(repo,"commit","--file=-","--cleanup=verbatim",data="feat: first group\n")
            first=self.head(repo)
            self.assertNotEqual(parent,first)
            (repo/"later.txt").write_bytes(b"Second pending group.\n")
            self.git(repo,"add","--","later.txt")
            self.hook(repo,"exit 9")
            pending=self.index(repo); work=self.working(repo)
            result=self.git(repo,"commit","--file=-","--cleanup=verbatim",data="feat: second group\n",check=False)
            self.assertNotEqual(0,result.returncode)
            self.assertEqual(first,self.head(repo))
            self.assertEqual(parent,self.git(repo,"rev-parse","HEAD^").stdout.strip())
            self.assertEqual(pending,self.index(repo))
            self.assertEqual(work,self.working(repo))

    def test_effective_identity_override_is_observable_before_commit(self):
        with git_fixture("staged",self.root) as repo:
            before=self.head(repo); pending=self.index(repo); working=self.working(repo)
            identity=self.git(repo,"var","GIT_AUTHOR_IDENT",extra_env={
                "GIT_AUTHOR_NAME":"Different Author","GIT_AUTHOR_EMAIL":"other@example.invalid"}).stdout
            configured=self.git(repo,"config","--get","user.name").stdout.strip()
            self.assertEqual(b"Fixture User",configured)
            self.assertTrue(identity.startswith(b"Different Author <other@example.invalid> "))
            self.assertEqual(before,self.head(repo))
            self.assertEqual(pending,self.index(repo))
            self.assertEqual(working,self.working(repo))
