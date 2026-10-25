"""Test-only execution of the documented local-history recipe; no skill runtime."""
from pathlib import Path
from tests.support.git_fixtures import _git

SAFE = ["--no-pager", "--no-optional-locks", "--no-lazy-fetch", "--no-replace-objects",
        "-c", "core.fsmonitor=false", "-c", "maintenance.auto=false", "-c", "gc.auto=0", "-c", "log.showSignature=false"]
DISPLAY = ["--no-notes", "--no-decorate", "--color=never", "--no-ext-diff", "--no-textconv"]

def query(repo, *args, check=True):
    return _git([*SAFE, *args], cwd=repo, check=check)

def history(repo: Path, *, start: int, end: int, emails: set[str] | None,
            basis: str = "author", budget: int = 1000, include_merges: bool = False,
            revision: str = "HEAD") -> dict:
    if start >= end or basis not in {"author", "committer"} or budget < 1:
        raise ValueError("Invalid normalized selection")
    result = {"status":"blocked", "oid":None, "records":[], "examined":0, "selected":[], "limits":[]}
    resolved = query(repo, "rev-parse", "--verify", "--end-of-options", revision+"^{commit}", check=False)
    if resolved.returncode:
        symbolic = query(repo, "symbolic-ref", "-q", "HEAD", check=False)
        ref = symbolic.stdout.strip()
        ref_exists = query(repo, "show-ref", "--verify", "--quiet", ref, check=False) if ref else None
        if revision == "HEAD" and ref and ref_exists.returncode == 1:
            result["status"] = "no_op"
        return result
    oid = resolved.stdout.strip()
    result["oid"] = oid
    shallow = query(repo, "rev-parse", "--is-shallow-repository").stdout.strip()
    if shallow == "true": result["limits"].append("shallow")
    graft_path = Path(query(repo, "rev-parse", "--git-path", "info/grafts").stdout.strip())
    if not graft_path.is_absolute(): graft_path = repo/graft_path
    if graft_path.is_file() and graft_path.read_bytes().strip(): result["limits"].append("grafts")
    walk = query(repo, "rev-list", f"--max-count={budget+1}", oid, "--", check=False)
    if walk.returncode:
        result["status"] = "limited"
        result["limits"].append("walk_error")
        return result
    oids = walk.stdout.splitlines()
    if len(oids) > budget: result["limits"].append("budget")
    for commit in oids[:budget]:
        metadata = query(repo, "show", "-s", *DISPLAY, "--format=%H%x00%P%x00%an%x00%ae%x00%at%x00%ct", commit, "--", check=False)
        message = query(repo, "show", "-s", *DISPLAY, "--format=%B", commit, "--", check=False)
        if metadata.returncode or message.returncode:
            result["limits"].append("record_error")
            break
        fields = metadata.stdout.rstrip("\n").split("\0")
        if len(fields) != 6:
            result["limits"].append("malformed")
            break
        sha, parents, name, email, authored, committed = fields
        record = {"oid":sha, "parents":parents.split(), "author_name":name, "author_email":email,
                  "author":int(authored), "committer":int(committed), "message":message.stdout.rstrip("\n")}
        result["records"].append(record)
        result["examined"] += 1
        if start <= record[basis] < end and (emails is None or email in emails) and (include_merges or len(record["parents"]) < 2):
            result["selected"].append(record)
    result["status"] = "limited" if result["limits"] else ("reported" if result["selected"] else "no_op")
    return result
