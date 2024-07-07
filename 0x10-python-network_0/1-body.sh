#!/bin/bash

#output body if status code is 200
STATUS_CODE=$(curl -sI "$1" | grep -i HTTP | awk '{print $2}')
if [ "$STATUS_CODE" -eq 200 ]; then
	curl -s "$1"
fi
