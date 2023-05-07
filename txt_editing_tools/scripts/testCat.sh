#!/usr/bin/env bash

# Sets the variable PY_CMD to be the python command set by user in python.conf file
source scripts/python.conf

# Print the command I'm running "$ python src/tt.py cat"
echo "TEST\$ $PY_CMD src/tt.py cat"
$PY_CMD src/tt.py cat

echo "TEST\$ $PY_CMD src/tt.py cat data/let3"
$PY_CMD src/tt.py cat data/let3

echo "TEST\$ $PY_CMD src/tt.py cat data/let3 data/num2"
$PY_CMD src/tt.py cat data/let3 data/num2

echo "TEST\$ $PY_CMD src/tt.py cat data/dup5 data/let3 data/names8 data/num2"
$PY_CMD src/tt.py cat data/dup5 data/let3 data/names8 data/num2

echo "TEST\$ $PY_CMD src/tt.py cat data/let3 FILE_DNE data/num2"
$PY_CMD src/tt.py cat data/let3 FILE_DNE data/num2
