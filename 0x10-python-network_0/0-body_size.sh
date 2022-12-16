#!/usr/bin/env bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -I 0.0.0.0:5000 | grep Content-Length |  cut -d " " -f 2
