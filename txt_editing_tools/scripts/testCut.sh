#!/usr/bin/env bash

# Sets the variable PY_CMD to be the python command set by user in python.conf file
source scripts/python.conf 

# Need to make files to test from...
echo "Creating data/TMP_people.csv with built-in paste tool..."
echo "    Pasting together data/names8 data/ages8 data/colors8 data/verbs8"
paste -d, data/names8 data/ages8 data/colors8 data/verbs8 > data/TMP_people.csv
echo "Creating data/TMP_kids.csv with built-in paste tool..."
echo "    Pasting together data/num10 data/names10 data/words5"
paste -d, data/num10 data/names10 data/words5 > data/TMP_kids.csv

# Print the command I'm running "$ python src/tt.py cut"
echo "TEST\$ $PY_CMD src/tt.py cut"
$PY_CMD src/tt.py cut

echo "TEST\$ $PY_CMD src/tt.py cut data/TMP_people.csv"
$PY_CMD src/tt.py cut data/TMP_people.csv

echo "TEST\$ $PY_CMD src/tt.py cut -f 2 data/TMP_people.csv"
$PY_CMD src/tt.py cut -f 2 data/TMP_people.csv

echo "TEST\$ $PY_CMD src/tt.py cut -f 2,4 data/TMP_people.csv"
$PY_CMD src/tt.py cut -f 2,4 data/TMP_people.csv

echo "TEST\$ $PY_CMD src/tt.py cut -f 4,2 data/TMP_people.csv"
$PY_CMD src/tt.py cut -f 4,2 data/TMP_people.csv

echo "TEST\$ $PY_CMD src/tt.py cut -f 2 data/TMP_kids.csv data/TMP_people.csv"
$PY_CMD src/tt.py cut -f 2 data/TMP_kids.csv data/TMP_people.csv

echo "TEST\$ $PY_CMD src/tt.py cut -f 13 data/TMP_people.csv"
$PY_CMD src/tt.py cut -f 13 data/TMP_people.csv

echo "TEST\$ $PY_CMD src/tt.py cut -f 3 data/TMP_kids.csv"
$PY_CMD src/tt.py cut -f 3 data/TMP_kids.csv
 
echo "TEST\$ $PY_CMD src/tt.py cut data/let3 DOES_NOT_EXIST data/complexity"
$PY_CMD src/tt.py cut data/let3 DOES_NOT_EXIST data/complexity

echo "Removing data/TMP_people.csv..."
rm data/TMP_people.csv
echo "Removing data/TMP_kids.csv..."
rm data/TMP_kids.csv