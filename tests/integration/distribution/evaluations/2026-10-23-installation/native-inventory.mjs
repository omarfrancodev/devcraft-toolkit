import fs from "node:fs";
import {spawnSync} from "node:child_process";
const binary="/tool/node_modules/@anthropic-ai/claude-code-linux-x64-musl/claude";
const rows=[];
for(const args of [["plugin","details","--help"],["plugin","marketplace","add","/source"],["plugin","install","devcraft-toolkit@devcraft-toolkit","--scope","user"],["plugin","details","devcraft-toolkit@devcraft-toolkit"],["auth","status"]]){
 const r=spawnSync(binary,args,{encoding:"utf8",timeout:30000,env:{...process.env,CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC:"1",NO_COLOR:"1"}});
 rows.push({args,exit:r.status,error:r.error?.message,stdout:r.stdout,stderr:r.stderr});console.log(JSON.stringify(rows.at(-1)));
}
fs.writeFileSync("/output/native-inventory-corrected-results.json",JSON.stringify(rows,null,2));
