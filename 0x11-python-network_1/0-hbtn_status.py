#!/usr/bin/env python3
"""fetches https://alx-intranet.hbtn.io/status."""

import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    body = response.read()
    print(f'Body response:\n\t\
- type: {type(body)}\n\t\
- content: {body}\n\t\
- utf8 content: {body.decode("utf-8")}')
