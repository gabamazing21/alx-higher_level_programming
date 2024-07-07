#!/bin/bash
#script to take url and give it's size using curl
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
