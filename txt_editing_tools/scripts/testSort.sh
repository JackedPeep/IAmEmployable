#!/usr/bin/env bash

# Sets the variable PY_CMD to be the python command set by user in python.conf file
source scripts/python.conf 

echo "NOTE: The *byte count* on Windows might slightly differ"

# Print the command I'm running "$ python src/tt.py sort"
echo "TEST\$ $PY_CMD src/tt.py sort"
$PY_CMD src/tt.py sort

echo "TEST\$ $PY_CMD src/tt.py sort data/colors8"
$PY_CMD src/tt.py sort data/colors8

echo "TEST\$ $PY_CMD src/tt.py sort data/random20"
$PY_CMD src/tt.py sort data/random20

echo "TEST\$ $PY_CMD src/tt.py sort data/complexity"
$PY_CMD src/tt.py sort data/complexity

echo "TEST\$ $PY_CMD src/tt.py sort data/colors8 data/names10"
$PY_CMD src/tt.py sort data/colors8 data/names10

echo "TEST\$ $PY_CMD src/tt.py sort data/colors8 FILE_DNE data/names10"
$PY_CMD src/tt.py sort data/colors8 FILE_DNE data/names10
