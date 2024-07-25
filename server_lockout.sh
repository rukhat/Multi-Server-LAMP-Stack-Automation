#!/bin/bash

ALLOWED_START=09
ALLOWED_END=17

CURRENT_HOUR=$(date +%-H)

if [ $CURRENT_HOUR -ge $ALLOWED_START ] && [ $CURRENT_HOUR -lt $ALLOWED_END ]; then
    exit 0
else
    exit 1
fi