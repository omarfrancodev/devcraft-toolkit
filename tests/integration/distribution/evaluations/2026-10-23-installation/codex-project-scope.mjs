import fs from "node:fs";
import assert from "node:assert/strict";
import {spawnSync} from "node:child_process";
const cli="/tool/node_modules/@openai/codex/bin/codex.js";
const rows=[];
for(const p of ["/projects/selected/.codex","/projects/control"])fs.mkdirSync(p,{recursive:true});
fs.writeFileSync("/projects/control/sentinel.txt","preserve control");
function run(args,cwd="/projects/selected"){
 const r=spawnSync(process.execPath,[cli,...args],{cwd,encoding:"utf8",timeout:30000,env:{...process.env,NO_COLOR:"1"}});
 rows.push({args,cwd,exit:r.status,stdout:r.stdout,stderr:r.stderr});assert.equal(r.status,0,JSON.stringify(rows.at(-1)));return r.stdout;
}
run(["plugin","marketplace","add","/source"]);
run(["plugin","add","devcraft-toolkit@devcraft-toolkit","--json"]);
const config="/root/.codex/config.toml";
const installedConfig=fs.readFileSync(config,"utf8");
fs.appendFileSync(config,'\n[projects."/projects/selected"]\ntrust_level = "trusted"\n[projects."/projects/control"]\ntrust_level = "trusted"\n');
fs.writeFileSync("/projects/selected/.codex/config.toml",'[plugins."devcraft-toolkit@devcraft-toolkit"]\nenabled = true\n');
function state(cwd){return JSON.parse(run(["plugin","list","--json"],cwd)).installed.find(p=>p.pluginId==="devcraft-toolkit@devcraft-toolkit").enabled;}
const before={selected:state("/projects/selected"),control:state("/projects/control")};
let red=false;
try{assert.equal(before.control,false);}catch{red=true;}
assert.equal(red,true,"The existing project recipe must reproduce the reported global-enable defect.");
let section="",changed=0;
const corrected=fs.readFileSync(config,"utf8").split("\n").map(line=>{
 if(line.startsWith("["))section=line;
 if(section==='[plugins."devcraft-toolkit@devcraft-toolkit"]' && /^enabled\s*=\s*true\s*$/.test(line)){changed++;return "enabled = false";}
 return line;
}).join("\n");
assert.equal(changed,1,"Expected exactly the selected plugin enablement.");
fs.writeFileSync(config,corrected);
const after={selected:state("/projects/selected"),control:state("/projects/control")};
assert.equal(after.selected,true);assert.equal(after.control,false);
assert.equal(fs.readFileSync("/projects/control/sentinel.txt","utf8"),"preserve control");
fs.writeFileSync("/output/codex-project-scope-results.json",JSON.stringify({source:"14bead6",client:"0.162.0",level:"registry enablement; no authenticated invocation",trust:"Only the two owned fixture projects explicitly trusted; global protection settings unchanged",installedConfig,before,baselineAssertion:"RED: expected control disabled; observed enabled",after,correctedAssertion:"GREEN: selected enabled/control disabled",correctedConfig:corrected,rows},null,2));
console.log(JSON.stringify({before,after,status:"registry-only RED-to-GREEN"}));
