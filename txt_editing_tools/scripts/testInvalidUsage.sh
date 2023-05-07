#!/usr/bin/env bash

# Sets the variable PY_CMD to be the python command set by user in python.conf file
source scripts/python.conf 

echo "Gracefully handle invalid usages of the tools"
# Print the command I'm running "$ python src/tt.py head -n data/let3"
echo "TEST\$ $PY_CMD src/tt.py head -n data/forgot_number"
$PY_CMD src/tt.py head -n data/forgot_number

echo "TEST\$ $PY_CMD src/tt.py tail -n data/forgot_number"
$PY_CMD src/tt.py tail -n data/forgot_number

echo "TEST\$ $PY_CMD src/tt.py grep ONLY_PATTERN"
$PY_CMD src/tt.py grep ONLY_PATTERN

echo "TEST\$ $PY_CMD src/tt.py grep -v ONLY_PATTERN"
$PY_CMD src/tt.py grep -v ONLY_PATTERN

echo "TEST\$ $PY_CMD src/tt.py cut -f data/forgot_field"
$PY_CMD src/tt.py cut -f data/forgot_field
