import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import assert from "node:assert/strict";
import {spawnSync} from "node:child_process";
const cli="/tool/node_modules/skills/bin/cli.mjs";
const targets={"codex":".agents/skills","github-copilot":".agents/skills","claude-code":".claude/skills","kiro-cli":".kiro/skills"};
const names=["using-devcraft-toolkit","git-working-directory-policy","git-safety-check","conventional-commits-style","todo-workflow-controller","natural-language-report-writer","validation-discovery"];
const selection=Object.fromEntries(names.map(n=>[n,n==="using-devcraft-toolkit"?names.slice(0,3):n==="git-safety-check"?["git-safety-check","git-working-directory-policy"]:[n]]));
selection.full=names;
const rows=[],lifecycle=[],commands=[];
function files(root){
 if(!fs.existsSync(root))return {};
 const out={};
 for(const name of fs.readdirSync(root,{recursive:true})){
  const p=path.join(root,name);
  if(fs.lstatSync(p).isFile())out[name]=crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
 }
 return out;
}
function resetHome(){
 for(const name of [".agents",".claude",".copilot",".kiro"]){
  const p=path.join("/root",name);
  assert(p.startsWith("/root/."));
  fs.rmSync(p,{recursive:true,force:true});
 }
 fs.writeFileSync("/root/unrelated.txt","home sentinel");
}
function run(args,cwd){
 const r=spawnSync(process.execPath,[cli,...args],{cwd,encoding:"utf8",timeout:30000,env:{...process.env,NO_COLOR:"1",DISABLE_TELEMETRY:"1"}});
 commands.push({argv:["node","skills/bin/cli.mjs",...args],cwd,exit:r.status});
 if(r.status!==0)throw Error(JSON.stringify({args,status:r.status,stdout:r.stdout,stderr:r.stderr,error:r.error?.message}));
 return r;
}
function install(source,names,target,scope,cwd){
 const args=["add",source,"--skill",...names,"--agent",target,"--copy","--yes","--json"];
 if(scope==="global")args.push("--global");
 return JSON.parse(run(args,cwd).stdout);
}
function verify(source,dest,selected){
 for(const n of selected){
  assert.deepEqual(files(path.join(dest,n)),files(path.join(source,"skills",n)));
  for(const name of fs.readdirSync(path.join(dest,n),{recursive:true}))assert(!fs.lstatSync(path.join(dest,n,name)).isSymbolicLink());
 }
 const actual=fs.readdirSync(dest).filter(n=>fs.existsSync(path.join(dest,n,"SKILL.md")));
 assert.deepEqual(actual.sort(),[...selected].sort());
}
for(const method of ["cli","manual"]){
 for(const [target,baseRelative] of Object.entries(targets)){
  for(const scope of ["project","global"]){
   for(const [requested,selected] of Object.entries(selection)){
    const relative=method==="manual" && target==="github-copilot" && scope==="global"?".copilot/skills":baseRelative;
    resetHome();
    const cwd=path.join("/cases",method,target,scope,requested);
    fs.mkdirSync(cwd,{recursive:true});
    fs.writeFileSync(path.join(cwd,"unrelated.txt"),"project sentinel");
    const control=path.join(cwd,"control");
    fs.mkdirSync(control);
    fs.writeFileSync(path.join(control,"unrelated.txt"),"control sentinel");
    const beforeProject=files(cwd);
    const dest=path.join(scope==="global"?"/root":cwd,relative);
    let reported=[];
    if(method==="cli"){
     reported=install("/source",selected,target,scope,cwd);
     assert.deepEqual(reported.map(s=>s.name).sort(),[...selected].sort());
    }else{
     fs.mkdirSync(dest,{recursive:true});
     for(const n of selected)fs.cpSync(path.join("/source/skills",n),path.join(dest,n),{recursive:true});
    }
    verify("/source",dest,selected);
    assert.equal(fs.readFileSync(path.join(cwd,"unrelated.txt"),"utf8"),"project sentinel");
    assert.deepEqual(files(control),{"unrelated.txt":beforeProject["control/unrelated.txt"]});
    assert.equal(fs.readFileSync("/root/unrelated.txt","utf8"),"home sentinel");
    if(scope==="global")assert(!fs.existsSync(path.join(cwd,relative)));
    else assert(!fs.existsSync(path.join("/root",relative)));
    rows.push({method,target,scope,requested,selected,status:"passed",destination:dest,beforeProject,afterProject:files(cwd),afterUser:files("/root"),reported});
   }
  }
 }
}
resetHome();
fs.mkdirSync("/bare-entry",{recursive:true});
const bare=install("/source",["using-devcraft-toolkit"],"codex","project","/bare-entry");
assert.deepEqual(bare.map(s=>s.name),["using-devcraft-toolkit"]);
for(const [target,relative] of Object.entries(targets)){
 for(const scope of ["project","global"]){
  resetHome();
  const cwd=path.join("/lifecycle",target,scope);
  fs.mkdirSync(cwd,{recursive:true});
  fs.writeFileSync(path.join(cwd,"keep.txt"),"keep project");
  const dest=path.join(scope==="global"?"/root":cwd,relative);
  const n="natural-language-report-writer";
  fs.mkdirSync(path.join(dest,n),{recursive:true});
  fs.writeFileSync(path.join(dest,n,"SKILL.md"),"existing personal content");
  fs.mkdirSync(path.join(dest,"unrelated"),{recursive:true});
  fs.writeFileSync(path.join(dest,"unrelated/keep.txt"),"unrelated skill sentinel");
  const pre=files(dest);
  // FS-04's workflow stops at the observed collision; the CLI is not invoked yet.
  assert.equal(fs.readFileSync(path.join(dest,n,"SKILL.md"),"utf8"),"existing personal content");
  assert.deepEqual(files(dest),pre);
  // FS-05 explicitly authorizes replacement inside this disposable case.
  install("/source",[n],target,scope,cwd);
  const first=files(path.join(dest,n));
  install("/source",[n],target,scope,cwd);
  assert.deepEqual(files(path.join(dest,n)),first);
  const source=path.join(cwd,"source-fixture");
  fs.cpSync("/source",source,{recursive:true});
  fs.appendFileSync(path.join(source,"skills",n,"SKILL.md"),"\nFixture update marker.\n");
  install(source,[n],target,scope,cwd);
  assert.deepEqual(files(path.join(dest,n)),files(path.join(source,"skills",n)));
  const args=["remove",n,"--agent",target,"--yes"];
  if(scope==="global")args.push("--global");
  run(args,cwd);
  assert(!fs.existsSync(path.join(dest,n)));
  assert.equal(fs.readFileSync(path.join(dest,"unrelated/keep.txt"),"utf8"),"unrelated skill sentinel");
  assert.equal(fs.readFileSync(path.join(cwd,"keep.txt"),"utf8"),"keep project");
  assert.equal(fs.readFileSync("/root/unrelated.txt","utf8"),"home sentinel");
  lifecycle.push({target,scope,status:"passed",collision:"stopped before install; explicit replacement then authorized",reinstall:"byte-identical",update:"explicit re-add from changed local source",remove:"named skill removed",unrelated:"preserved",before:pre,after:files(dest)});
 }
}
fs.writeFileSync("/output/filesystem-results.json",JSON.stringify({node:process.version,platform:process.platform,cli:"1.7.4",rows,lifecycle,bareEntry:{installed:bare.map(s=>s.name),dependenciesResolved:false},commands},null,2));
console.log(JSON.stringify({cases:rows.length,cli:rows.filter(r=>r.method==="cli").length,manual:rows.filter(r=>r.method==="manual").length,lifecycle:lifecycle.length,bareEntry:bare.map(s=>s.name),status:"passed"}));
