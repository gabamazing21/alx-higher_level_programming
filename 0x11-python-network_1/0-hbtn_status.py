#!/usr/bin/python3
import urllib.request
"""Make network request"""
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    content = response.read()
print("Body response:")
print("    - type: ",  type(content))
print("    - content: ", content)
print(f"    - utf8 content: ", content.decode("utf-8"))
