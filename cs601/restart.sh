#!/usr/bin/env bash

kill -9 `pgrep -f flask` 2>/dev/null
./run.sh