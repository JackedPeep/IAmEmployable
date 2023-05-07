#!/usr/bin/env bash

# Sets the variable PY_CMD to be the python command set by user in python.conf file
source scripts/python.conf 

# Print the command I'm running "$ python src/tt.py"
echo "TEST\$ $PY_CMD src/tt.py"
$PY_CMD src/tt.py

echo "TEST\$ $PY_CMD src/tt.py cat"
$PY_CMD src/tt.py cat

echo "TEST\$ $PY_CMD src/tt.py tac"
$PY_CMD src/tt.py tac

echo "TEST\$ $PY_CMD src/tt.py head"
$PY_CMD src/tt.py head

echo "TEST\$ $PY_CMD src/tt.py tail"
$PY_CMD src/tt.py tail

echo "TEST\$ $PY_CMD src/tt.py grep"
$PY_CMD src/tt.py grep

echo "TEST\$ $PY_CMD src/tt.py wc"
$PY_CMD src/tt.py wc

echo "TEST\$ $PY_CMD src/tt.py sort"
$PY_CMD src/tt.py sort

echo "TEST\$ $PY_CMD src/tt.py paste"
$PY_CMD src/tt.py paste

echo "TEST\$ $PY_CMD src/tt.py cut"
$PY_CMD src/tt.py cut

