import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import {spawnSync} from "node:child_process";
const codex="/tool/node_modules/@openai/codex/bin/codex.js";
const claude="/tool/node_modules/@anthropic-ai/claude-code-linux-x64-musl/claude";
const rows=[];
fs.mkdirSync("/projects/selected",{recursive:true});
fs.mkdirSync("/projects/control",{recursive:true});
fs.writeFileSync("/projects/control/sentinel.txt","unchanged control");
function files(root){if(!fs.existsSync(root))return {};const out={};for(const n of fs.readdirSync(root,{recursive:true})){const p=path.join(root,n);if(fs.lstatSync(p).isFile())out[n]=crypto.createHash("sha256").update(fs.readFileSync(p)).digest("hex");}return out;}
function run(client,args,cwd="/projects/selected"){
 const r=spawnSync(client==="codex"?process.execPath:claude,client==="codex"?[codex,...args]:args,{cwd,encoding:"utf8",timeout:45000,env:{...process.env,NO_COLOR:"1",DISABLE_TELEMETRY:"1",CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC:"1"}});
 rows.push({client,args,cwd,exit:r.status,signal:r.signal,error:r.error?.message,stdout:r.stdout,stderr:r.stderr,project:files("/projects"),home:files("/root")});
 console.log(JSON.stringify({client,args,exit:r.status,error:r.error?.message,stdout:r.stdout?.slice(0,1200),stderr:r.stderr?.slice(0,1200)}));
}
for(const client of ["codex","claude"]){
 run(client,["--version"]);
 run(client,["plugin","--help"]);
 run(client,["plugin","marketplace","add","/source"]);
 if(client==="codex"){
  run(client,["plugin","add","devcraft-toolkit@devcraft-toolkit","--json"]);
  run(client,["plugin","list","--json"]);
  run(client,["plugin","marketplace","upgrade","devcraft-toolkit"]);
  run(client,["plugin","remove","devcraft-toolkit@devcraft-toolkit"]);
 }else{
  run(client,["plugin","validate","/source/.claude-plugin/plugin.json","--json"]);
  run(client,["plugin","validate","/source/.claude-plugin/marketplace.json","--json"]);
  for(const scope of ["user","project"]){
   run(client,["plugin","install","devcraft-toolkit@devcraft-toolkit","--scope",scope]);
   run(client,["plugin","list","--json"]);
   run(client,["plugin","list","--json"],"/projects/control");
   run(client,["plugin","update","devcraft-toolkit@devcraft-toolkit","--scope",scope]);
   run(client,["plugin","uninstall","devcraft-toolkit@devcraft-toolkit","--scope",scope]);
  }
 }
}
fs.writeFileSync("/output/native-cli-results.json",JSON.stringify({source:"72e190f0cceed4f42d70fca95213660fcb8fd9aa",node:process.version,platform:process.platform,network:"none",rows},null,2));
