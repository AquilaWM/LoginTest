#!/usr/bin/env python3

import requests, json

with open("login.json") as f:
    data = f.read()
    json_data = json.loads(data)
    url = json_data["url"]
    uname = json_data["uname"]
    passwd = json_data["passwd"]

with open("mfa.token") as f:
    token = f.readline()

body = {"username" : uname, "password" : passwd, "token" : token}

# Test login
response = requests.post(url, body)
