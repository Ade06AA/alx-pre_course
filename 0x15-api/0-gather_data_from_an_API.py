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
    EMPLOYEE_NAME = data1.get("name")
    TOTAL_NUMBER_OF_TASKS = len(data2)
    NUMBER_OF_DONE_TASKS = 0
    for i in data2:
        if i.get("completed") is True:
            NUMBER_OF_DONE_TASKS += 1
    print(f"Employee {EMPLOYEE_NAME} is done with tasks" +
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for i in data2:
        if i.get("completed") is True:
            print("\t {}".format(i.get("title")))
