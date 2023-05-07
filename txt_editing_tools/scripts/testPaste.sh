#!/usr/bin/env bash

# Sets the variable PY_CMD to be the python command set by user in python.conf file
source scripts/python.conf 

# Print the command I'm running "$ python src/tt.py paste"
echo "TEST\$ $PY_CMD src/tt.py paste"
$PY_CMD src/tt.py paste

echo "TEST\$ $PY_CMD src/tt.py paste data/let3 data/num2"
$PY_CMD src/tt.py paste data/let3 data/num2

echo "TEST\$ $PY_CMD src/tt.py paste data/num2 data/let3"
$PY_CMD src/tt.py paste data/num2 data/let3

echo "TEST\$ $PY_CMD src/tt.py paste data/num2 data/words5 data/let3"
$PY_CMD src/tt.py paste data/num2 data/words5 data/let3

echo "TEST\$ $PY_CMD src/tt.py paste data/num2 data/let3 data/words5"
$PY_CMD src/tt.py paste data/num2 data/let3 data/words5

echo "TEST\$ $PY_CMD src/tt.py paste data/names8 data/ages8 data/colors8 data/verbs8"
$PY_CMD src/tt.py paste data/names8 data/ages8 data/colors8 data/verbs8

echo "TEST\$ $PY_CMD src/tt.py paste data/ages8 FILE_DNE data/words200"
$PY_CMD src/tt.py paste data/ages8 FILE_DNE data/words200
