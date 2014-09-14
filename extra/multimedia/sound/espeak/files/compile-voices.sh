#!/bin/bash

cd dictsource
export ESPEAK_DATA_PATH=..
for voice in $(../src/speak --voices | awk '{print $2}{print $5}' | egrep -v Language\|File\|/ | uniq); do \
    ../src/speak --compile=$voice; \
done
