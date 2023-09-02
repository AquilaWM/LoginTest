#!/usr/bin/env python3

import requests, json

with open("login.json") as f:
    data = f.read()
    json_data = json.loads(data)
    url = json_data["url"]
    uname = json_data["uname"]

# Don't want to store the password in plain text in a file. Should be fine here
passwd = "SuP3Rs3cREt_P455wd*!"

body = {"username" : uname, "password" : passwd}

# Test login
response = requests.post(url, body)

# Will implement MFA later