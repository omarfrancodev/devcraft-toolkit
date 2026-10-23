import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import assert from "node:assert/strict";
import {spawnSync} from "node:child_process";
const ref="b05a8c4367dc02e33ac9d19a8eb98e0bdb31c04e";
const repository="https://github.com/omarfrancodev/devcraft-toolkit.git";
const treeUrl="https://github.com/omarfrancodev/devcraft-toolkit/tree/"+ref;
const names=["conventional-commits-style","git-safety-check","git-working-directory-policy","natural-language-report-writer","todo-workflow-controller","using-devcraft-toolkit","validation-discovery"];
const commands=[],checks=[];
const codex=["node","/tool/node_modules/@openai/codex/bin/codex.js"];
const claude=["/tool/node_modules/@anthropic-ai/claude-code-linux-x64-musl/claude"];
const skills=["node","/tool/node_modules/skills/bin/cli.mjs"];
const env={...process.env,NO_COLOR:"1",DISABLE_TELEMETRY:"1",CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC:"1",CLAUDE_CODE_PLUGIN_PREFER_HTTPS:"1",GIT_TERMINAL_PROMPT:"0"};
function run(prefix,args,cwd="/projects/selected",required=true){
 const r=spawnSync(prefix[0],[...prefix.slice(1),...args],{cwd,env,encoding:"utf8",timeout:90000,maxBuffer:8*1024*1024});
 const row={argv:[...prefix,...args],cwd,exit:r.status,error:r.error?.message,stdout:r.stdout,stderr:r.stderr};commands.push(row);
 console.log(JSON.stringify({argv:row.argv,exit:row.exit,error:row.error}));
 if(required)assert.equal(r.status,0,JSON.stringify(row));return r.stdout;
}
function files(root){const out={};if(!fs.existsSync(root))return out;for(const name of fs.readdirSync(root,{recursive:true})){const p=path.join(root,name);if(fs.lstatSync(p).isFile())out[name]=crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");}return out;}
function verify(dest,selected){
 const actual=fs.readdirSync(dest).filter(n=>fs.existsSync(path.join(dest,n,"SKILL.md"))).sort();assert.deepEqual(actual,[...selected].sort());
 const hashes={};for(const n of selected){hashes[n]=files(path.join(dest,n));assert.deepEqual(hashes[n],files(path.join("/reference/skills",n)));}
 return {destination:dest,names:actual,hashes};
}
function packages(root){
 const out=[];
 function walk(p){if(!fs.existsSync(p))return;
  if(fs.existsSync(path.join(p,"skills")) && fs.existsSync(path.join(p,"plugin.json"))){out.push(verify(path.join(p,"skills"),names));return;}
  for(const entry of fs.readdirSync(p,{withFileTypes:true}))if(entry.isDirectory()&&entry.name!==".git")walk(path.join(p,entry.name));
 }walk(root);return out;
}
let status="failed",error;
try{
 for(const p of ["/projects/selected","/projects/control","/projects/individual","/projects/kiro"])fs.mkdirSync(p,{recursive:true});
 fs.writeFileSync("/projects/control/sentinel.txt","control");fs.writeFileSync("/projects/individual/sentinel.txt","individual");fs.writeFileSync("/projects/kiro/sentinel.txt","kiro");
 run(["git"],["init","/reference"],"/");
 run(["git"],["fetch","--depth","1",repository,ref],"/reference");
 run(["git"],["checkout","--detach","FETCH_HEAD"],"/reference");
 assert.equal(run(["git"],["rev-parse","HEAD"],"/reference").trim(),ref);
 assert.deepEqual(fs.readdirSync("/reference/skills").sort(),names);
 const portable=JSON.parse(fs.readFileSync("/reference/plugin.json"));
 const mirror=JSON.parse(fs.readFileSync("/reference/.claude-plugin/plugin.json"));assert.equal(portable.version,"0.1.0-preview.2");assert.equal(portable.version,mirror.version);
 checks.push({packet:"REMOTE-FS-01",status:"passed",ref,source:verify("/reference/skills",names)});
 for(const cli of [codex,claude,skills])run(cli,["--version"]);
 run(["git"],["--version"]);
 run(codex,["plugin","marketplace","add","omarfrancodev/devcraft-toolkit","--ref",ref]);
 run(codex,["plugin","add","devcraft-toolkit@devcraft-toolkit","--json"]);
 const codexList=JSON.parse(run(codex,["plugin","list","--json"]));
 assert(codexList.installed.some(p=>p.pluginId==="devcraft-toolkit@devcraft-toolkit"&&p.version==="0.1.0-preview.2"));
 const codexPackages=packages("/root/.codex/plugins/cache");assert(codexPackages.length>0,"No Codex installed package found");
 run(codex,["plugin","marketplace","upgrade","devcraft-toolkit"]);
 run(codex,["plugin","remove","devcraft-toolkit@devcraft-toolkit"]);
 checks.push({packet:"REMOTE-NATIVE-01",status:"limited",registration:"passed",resources:"passed",activation:"blocked: no model authentication",packages:codexPackages});
 run(claude,["plugin","marketplace","add",repository+"#docs/distribution-installation"]);
 const claudeSourceHead=run(["git"],["rev-parse","HEAD"],"/root/.claude/plugins/marketplaces/devcraft-toolkit").trim();
 assert.equal(claudeSourceHead,ref);
 for(const scope of ["user","project"]){
  run(claude,["plugin","install","devcraft-toolkit@devcraft-toolkit","--scope",scope]);
  const list=JSON.parse(run(claude,["plugin","list","--json"]));const item=list.find(p=>p.id==="devcraft-toolkit@devcraft-toolkit");
  assert.equal(item.scope,scope);
  const installed=verify(path.join(item.installPath,"skills"),names);
  run(claude,["plugin","details","devcraft-toolkit@devcraft-toolkit"]);
  const control=JSON.parse(run(claude,["plugin","list","--json"],"/projects/control"));
  if(scope==="project")assert.equal(control.find(p=>p.id===item.id).enabled,false);
  run(claude,["plugin","update","devcraft-toolkit@devcraft-toolkit","--scope",scope]);
  run(claude,["plugin","uninstall","devcraft-toolkit@devcraft-toolkit","--scope",scope]);
  checks.push({packet:"REMOTE-NATIVE-02",scope,status:"limited",registration:"passed",resources:"passed",activation:"blocked: no model authentication",installed});
 }
 for(const [cwd,target,selected,relative] of [["/projects/individual","codex",["conventional-commits-style"],".agents/skills"],["/projects/kiro","kiro-cli",names,".kiro/skills"]]){
  run(skills,["add",treeUrl,"--skill",...selected,"--agent",target,"--copy","--yes","--json"],cwd);
  checks.push({packet:"REMOTE-ALT-01",target,status:"passed",level:"filesystem only",installed:verify(path.join(cwd,relative),selected)});
 }
 assert.equal(fs.readFileSync("/projects/control/sentinel.txt","utf8"),"control");
 assert.equal(fs.readFileSync("/projects/individual/sentinel.txt","utf8"),"individual");assert.equal(fs.readFileSync("/projects/kiro/sentinel.txt","utf8"),"kiro");
 checks.push({packet:"REMOTE-LIMIT-01",status:"blocked",reason:"No authenticated model invocation, Copilot session or Kiro IDE; Kiro ref interface unestablished."});
 status="passed_with_native_limits";
}catch(e){error=String(e.stack??e);console.error(error);}
fs.writeFileSync("/output/results.json",JSON.stringify({repository,ref,node:process.version,platform:process.platform,network:"public Git/npm; no host credentials mounted",status,error,checks,commands},null,2));
if(error)process.exitCode=1;
