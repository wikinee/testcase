#!/bin/bash

removable=0

for i in /sys/block/sd[a-z]/removable
do
  removable=$(cat "$i")
  if [ "$removable" = 0 ]; then
    echo "$i pass......"
  else
    echo "$i failed...."
  fi
done

