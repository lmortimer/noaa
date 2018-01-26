#!/usr/bin/python3

import sys
import requests

result = requests.get(sys.argv[1])

if result.status_code == requests.codes.ok:
    sys.stdout.write(result.text)
    sys.stdout.flush()
else:
    sys.exit(1)