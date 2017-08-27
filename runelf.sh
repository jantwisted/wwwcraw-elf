#!/bin/bash
#
# This script runs python script until it gives desired output.
#
# Author: jantwisted (janith@member.fsf.org)

while :
do
    python3 wwwcraw-elf.py
    if [ $? -eq 4 ]
    then
	break
    fi
    sleep 1
done
