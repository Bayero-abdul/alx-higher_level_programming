#!/bin/bash
# displays the size of the body of the response
curl -s 0.0.0.0:5000/route_1 | grep route_2 | tr -d '\n'| sed 's/.*\(route_2\).*/\1/' | sed -r 's/([a-z]+).([0-9]+)/\1 \2/' | sed 's/./\U&/'
