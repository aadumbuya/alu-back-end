#!/usr/bin/python3
"""
Gathering data using REST API
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
    Main module
    """
    request_users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    )
    users = json.loads(request_users.text)
    EMPLOYEE_NAME = users['name']
    todos = json.loads(request_todos.text)
    tasks = {}
    for i in todos:
        tasks.update({i.get('title'): i.get('completed')})
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
    ))
    for k, v in tasks.items():
        if v is True:
            print("\t {}".format(k))
