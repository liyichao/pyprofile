#!/usr/bin/env bash
script_name=$1
duration=${2:-20}

set -e

trap 'kill $(jobs -p)' EXIT

python $1 &
PID=$!
../systemtap-python-tools/scripts/sample -t $duration -x $PID | ../FlameGraph/flamegraph.pl --colors=java > perf.svg
