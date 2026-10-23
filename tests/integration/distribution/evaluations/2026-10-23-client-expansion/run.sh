#!/bin/sh
set -eu
apk add --no-cache git ca-certificates libstdc++ gcompat >/tmp/apk-install.log
npm install --ignore-scripts --no-audit --no-fund --prefix /tool @github/copilot@1.0.91 >/tmp/npm-install.log
node /runner/runner.mjs
