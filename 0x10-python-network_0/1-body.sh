#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send GET request and capture status code and response body
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Check if the response status code is 200
if [ "$response" -eq 200 ]; then
  # Display the body of the response
  curl -s "$1"
else
  echo "Error: HTTP status code $response"
fi
