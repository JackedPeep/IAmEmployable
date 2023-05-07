#!/usr/bin/env bash

# Sets the variable PY_CMD to be the python command set by user in python.conf file
source scripts/python.conf 

echo "NOTE: The *byte count* on Windows might slightly differ"

# Print the command I'm running "$ python src/tt.py wc"
echo "TEST\$ $PY_CMD src/tt.py wc"
$PY_CMD src/tt.py wc

echo "TEST\$ $PY_CMD src/tt.py wc data/num2"
$PY_CMD src/tt.py wc data/num2

echo "TEST\$ $PY_CMD src/tt.py wc data/wordcount"
$PY_CMD src/tt.py wc data/wordcount

echo "TEST\$ $PY_CMD src/tt.py wc data/let3 data/random20 data/words200 data/dup5 data/complexity"
$PY_CMD src/tt.py wc data/let3 data/random20 data/words200 data/dup5 data/complexity

echo "TEST\$ $PY_CMD src/tt.py wc data/ages8 FILE_DNE data/words200"
$PY_CMD src/tt.py wc data/ages8 FILE_DNE data/words200
