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
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1])
    )
    users = json.loads(request_users.text)
    EMPLOYEE_NAME = users['name']
    username = users.get('username')
    todos = json.loads(request_todos.text)
    tasks = {}
    for i in todos:
        tasks.update({i.get('title'): i.get('completed')})
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    """
    Data preparation
    """
    user_tasks = []
    for item in todos:
        task = {}
        task['task'] = item.get('title')
        task['completed'] = item.get('completed')
        task['username'] = username
        user_tasks.append(task)
    """
    Exporting to JSON
    """
    with open('{}.json'.format(argv[1]), 'w') as json_f:
        json.dump({argv[1]: user_tasks}, json_f)
