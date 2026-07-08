#!/bin/bash
# Usage: ./check.sh <program.py> [tests_dir]
# Example: ./check.sh permutations.py tests

prog="$1"
dir="${2:-tests}"

if [ -z "$prog" ]; then
    echo "Usage: $0 <program.py> [tests_dir]"
    exit 1
fi

for in in "$dir"/*.in; do
    out="${in%.in}.out"
    if diff -q <(python3 "$prog" < "$in") "$out" > /dev/null; then
        echo "PASS $in"
    else
        echo "FAIL $in"
    fi
done
