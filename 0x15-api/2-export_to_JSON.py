#!/usr/bin/python3
"""
Data in The JSON format
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/{}".format(uid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?usrId={}".format(uid)
    todo = requests.get(url, verify=False).json()
    name = user.get('username')
    t = [{"taask": t.get("title"),
        "username": name,
        "completed": t.get("completed")} for t in todo]
    bj = dict()
    bj[uid] = t
    with open("{}.json".form(uid), 'w') as filejs:
        json.dump(bj, filejs)
