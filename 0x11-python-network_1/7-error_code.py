#!/usr/bin/python3
"""Python script that:
        takes in a URL
        sends a request to the URL
        displays the body of the response.
description:
    HTTP status code is greater than or equal to 400
    print: Error code: followed by the value of the HTTP status code
Usage: ./7-error_code.py <URL>
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
