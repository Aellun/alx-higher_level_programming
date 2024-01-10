#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
# only display a body of code 200

curl -sL "$1"
