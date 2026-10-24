import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import assert from "node:assert/strict";
import {spawnSync} from "node:child_process";
const ref="b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e";
const previewBranch="docs/distribution-installation";
const previewHead="218aea8d180a17f2cb6d321c9141f2979191b8e0";
const repo="https://github.com/omarfrancodev/devcraft-toolkit.git";
const id="devcraft-toolkit@devcraft-toolkit";
const names=["conventional-commits-style","git-safety-check","git-working-directory-policy","natural-language-report-writer","todo-workflow-controller","using-devcraft-toolkit","validation-discovery"];
const cli=["/tool/node_modules/.bin/copilot"];
const commands=[], checks=[];
const env={...process.env,NO_COLOR:"1",GIT_TERMINAL_PROMPT:"0",DO_NOT_TRACK:"1"};
function run(prefix,args,cwd="/projects/selected",required=true){
 const r=spawnSync(prefix[0],[...prefix.slice(1),...args],{cwd,env,encoding:"utf8",timeout:90000,maxBuffer:8*1024*1024});
 const row={argv:[...prefix,...args],cwd,exit:r.status,error:r.error?.message,stdout:r.stdout,stderr:r.stderr};
 commands.push(row);console.log(JSON.stringify({argv:row.argv,exit:row.exit,error:row.error}));
 if(required)assert.equal(r.status,0,JSON.stringify(row));return row;
}
function hashes(root){
 const out={};
 for(const name of fs.readdirSync(root,{recursive:true}).sort()){
  const p=path.join(root,name);
  if(fs.lstatSync(p).isFile())out[name]=crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");
 }return out;
}
function verify(){
 const root="/root/.copilot/installed-plugins/devcraft-toolkit/devcraft-toolkit";
 assert(fs.existsSync(root),"Actual CLI-managed package directory missing");
 const list=fs.readdirSync(path.join(root,"skills")).filter(n=>fs.existsSync(path.join(root,"skills",n,"SKILL.md"))).sort();
 assert.deepEqual(list,names);
 const resources={};for(const n of names){
  resources[n]=hashes(path.join(root,"skills",n));
  assert.deepEqual(resources[n],hashes(path.join("/reference/skills",n)));
 }
 assert.deepEqual(JSON.parse(fs.readFileSync(path.join(root,"plugin.json"))),JSON.parse(fs.readFileSync("/reference/plugin.json")));
 return {root,names:list,resources};
}
let status="failed",error;
try{
 for(const dir of ["/projects/selected","/projects/control","/root/.copilot/skills/unrelated"])fs.mkdirSync(dir,{recursive:true});
 fs.writeFileSync("/projects/control/sentinel.txt","control");
 fs.writeFileSync("/root/.copilot/skills/unrelated/sentinel.txt","unrelated");
 run(["git"],["init","/reference"],"/");
 run(["git"],["fetch","--depth","1",repo,ref],"/reference");
 run(["git"],["checkout","--detach","FETCH_HEAD"],"/reference");
 assert.equal(run(["git"],["rev-parse","HEAD"],"/reference").stdout.trim(),ref);
 run(["node"],["--version"]);run(["git"],["--version"]);run(cli,["--version"]);
 run(cli,["plugin","marketplace","add","omarfrancodev/devcraft-toolkit#"+previewBranch]);
 const resolved=run(["git"],["rev-parse","HEAD"],"/root/.copilot/.cache/copilot/marketplaces/omarfrancodev-devcraft-toolkit").stdout.trim();
 assert.equal(resolved,previewHead,"Published preview branch advanced; review source expectation before replay");
 run(cli,["plugin","marketplace","browse","devcraft-toolkit"]);
 run(cli,["plugin","install",id]);
 const list=JSON.parse(run(cli,["plugin","list","--json"]).stdout);
 assert(JSON.stringify(list).includes("devcraft-toolkit"));
 checks.push({packet:"CLIENT-COPILOT-01",status:"limited",registration:"passed",resources:verify(),activation:"blocked: no authenticated model session"});
 const repeat=run(cli,["plugin","install",id],"/projects/selected",false);
 checks.push({packet:"repeat-install",exit:repeat.exit,resourcesPreserved:verify()});
 run(cli,["plugin","disable",id]);
 run(cli,["plugin","list","--json"]);
 run(cli,["plugin","enable",id]);
 run(cli,["plugin","marketplace","update","devcraft-toolkit"]);
 run(cli,["plugin","update",id]);
 checks.push({packet:"same-ref-refresh-update",status:"limited",resources:verify(),note:"No version change or active-session invocation was exercised."});
 run(cli,["plugin","uninstall",id]);
 const after=run(cli,["plugin","list","--json"]);
 assert(!after.stdout.includes('"name": "devcraft-toolkit"'));
 assert.equal(fs.readFileSync("/projects/control/sentinel.txt","utf8"),"control");
 assert.equal(fs.readFileSync("/root/.copilot/skills/unrelated/sentinel.txt","utf8"),"unrelated");
 checks.push({packet:"selected-removal-sentinels",status:"passed",control:"preserved",unrelatedSkill:"preserved"});
 status="limited";
}catch(e){error=String(e.stack??e);console.error(error);}
finally{
 fs.writeFileSync("/output/results.json",JSON.stringify({status,error,ref,previewBranch,previewHead,repository:repo,node:process.version,commands,checks,unverified:["Authenticated activation/model resource reads","Repository auto-install and active-session isolation","CLI to VS Code crossover","Kiro CLI V3/IDE/Crew sessions","Version-changing update"]},null,2)+"\n");
 fs.copyFileSync("/tool/package-lock.json","/output/toolchain-lock.json");
}
if(status==="failed")process.exitCode=1;
