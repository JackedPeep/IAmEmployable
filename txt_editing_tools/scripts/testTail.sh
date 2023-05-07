#!/usr/bin/env bash

# Sets the variable PY_CMD to be the python command set by user in python.conf file
source scripts/python.conf 

# Print the command I'm running "$ python src/tt.py tail"
echo "TEST\$ $PY_CMD src/tt.py tail"
$PY_CMD src/tt.py tail

echo "TEST\$ $PY_CMD src/tt.py tail data/let3"
$PY_CMD src/tt.py tail data/let3

echo "TEST\$ $PY_CMD src/tt.py tail data/words200"
$PY_CMD src/tt.py tail data/words200

echo "TEST\$ $PY_CMD src/tt.py tail -n 13 data/words200"
$PY_CMD src/tt.py tail -n 13 data/words200

echo "TEST\$ $PY_CMD src/tt.py tail -n 3 data/ages8 data/names8 data/words200"
$PY_CMD src/tt.py tail -n 3 data/ages8 data/names8 data/words200

echo "TEST\$ $PY_CMD src/tt.py tail data/ages8 FILE_DNE data/words200"
$PY_CMD src/tt.py tail data/ages8 FILE_DNE data/words200
