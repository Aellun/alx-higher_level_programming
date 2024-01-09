#!/bin/bash
# A Bash script that takes in a URL, sends a GET request, and displays only the body of a 200 status code response

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send GET request and extract the status code
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")

echo "$status_code"
