#!/bin/bash
while read -r line || [[ -n ${line} ]]
do
echo "$line"
sleep 1
done < tasklist.txt
echo "end..............."
