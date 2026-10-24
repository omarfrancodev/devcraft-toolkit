#!/bin/sh
set -eu
apk add --no-cache git ca-certificates >/tmp/apk-install.log
if [ ! -f /tool/package-lock.json ]; then
  npm install --ignore-scripts --no-audit --no-fund --prefix /tool @openai/codex@0.162.0 @anthropic-ai/claude-code@2.1.300 skills@1.7.4 >/tmp/npm-install.log
fi
node /runner/runner.mjs
