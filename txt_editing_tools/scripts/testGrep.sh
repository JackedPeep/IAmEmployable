#!/usr/bin/env bash

# Sets the variable PY_CMD to be the python command set by user in python.conf file
source scripts/python.conf 

# Print the command I'm running "$ python src/tt.py grep"
echo "TEST\$ $PY_CMD src/tt.py grep"
$PY_CMD src/tt.py grep

echo "TEST\$ $PY_CMD src/tt.py grep Blue data/colors8"
$PY_CMD src/tt.py grep Blue data/colors8

echo "TEST\$ $PY_CMD src/tt.py grep blue data/colors8"
$PY_CMD src/tt.py grep blue data/colors8

echo "TEST\$ $PY_CMD src/tt.py grep a data/ages8 data/colors8 data/let3"
$PY_CMD src/tt.py grep a data/ages8 data/colors8 data/let3

echo "TEST\$ $PY_CMD src/tt.py grep -v a data/ages8 data/colors8 data/let3"
$PY_CMD src/tt.py grep -v a data/ages8 data/colors8 data/let3

echo "TEST\$ $PY_CMD src/tt.py grep a data/ages8 FILE_DNE data/words200"
$PY_CMD src/tt.py grep a data/ages8 FILE_DNE data/words200
