#!/usr/bin/env bash

# Sets the variable PY_CMD to be the python command set by user in python.conf file
source scripts/python.conf 

# Print the command I'm running "$ python src/tt.py head"
echo "TEST\$ $PY_CMD src/tt.py head"
$PY_CMD src/tt.py head

echo "TEST\$ $PY_CMD src/tt.py head data/let3"
$PY_CMD src/tt.py head data/let3

echo "TEST\$ $PY_CMD src/tt.py head data/words200"
$PY_CMD src/tt.py head data/words200

echo "TEST\$ $PY_CMD src/tt.py head -n 13 data/words200"
$PY_CMD src/tt.py head -n 13 data/words200

echo "TEST\$ $PY_CMD src/tt.py head -n 3 data/ages8 data/names8 data/words200"
$PY_CMD src/tt.py head -n 3 data/ages8 data/names8 data/words200

echo "TEST\$ $PY_CMD src/tt.py head data/ages8 FILE_DNE data/words200"
$PY_CMD src/tt.py head data/ages8 FILE_DNE data/words200
