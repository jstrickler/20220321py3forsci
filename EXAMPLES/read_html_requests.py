#!/usr/bin/env python
import requests

response = requests.get("https://www.python.org", timeout=10)  # <1>

if response.status_code == requests.codes.OK:

    for header, value in sorted(response.headers.items()): # <2>
        print("{:20.20s} {}".format(header, value))
    print()
    # response.contents for raw bytes

    print(response.text[:200])   # <3>
    print('...')
    print(response.text[-200:])   # <4>
