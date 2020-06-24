#!/bin/bash

# Description:
#  Add for test for get mouse position
# Dependency:
#  sudo apt install xdotool

# example 1
watch -n 0.1 "xdotool getmouselocation"

# example 2
# while true; do clear; xdotool getmouselocation; sleep 0.1; done
