#!/usr/bin/python3
"""
using a n api
"""

import requests
from sys import argv
from json import loads, dumps


if __name__ == "__main__" and len(argv) == 2:
    responce1 = requests.get("https://jsonplaceholder.typicode.com" +
                             "/users/{}".format(argv[1]))
    responce2 = requests.get("https://jsonplaceholder.typicode.com" +
                             "/todos?user_Id={}".format(argv[1]))
    data1 = responce1.json()
    data2 = responce2.json()
    USERNAME = data1.get("name")
    with open(f"{argv[1]}.csv", "w") as file:
        for i in data2:
            status = i.get("completed")
            title = i.get("title")
            text = f'"{argv[1]}","{USERNAME}","{status}","{title}"\n'
            file.write(text)
