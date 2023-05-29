#!/bin/bash

FILE1=$1
FILE2=$2

FILE3="$(pwd)/merged.txt"
cat $FILE1 >> $FILE3
cat $FILE2 >> $FILE3

echo "Merge done. Results are in ${FILE3}"
