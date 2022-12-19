#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -sI 0.0.0.0:5000/route_4 | grep Allow | sed -r 's/\S*[[:space:]](.*)/\1/'
