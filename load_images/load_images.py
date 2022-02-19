#!/usr/bin/python

import sys
from pathlib import Path

import requests

API = "http://127.0.0.1:8000/upload-file/"

if __name__ == '__main__':
    path = Path(sys.argv[1])
    files = [("files", open(file, 'rb')) for file in path.iterdir()]
    resp = response = requests.post(API, files=files)
    print(response.json())
