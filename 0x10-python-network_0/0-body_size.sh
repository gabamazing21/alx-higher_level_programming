#!/bin/bash
#script to take url and give it's size using curl
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

curl -sI "$1" | grep -i Content-Length | awk '{print $1}'
