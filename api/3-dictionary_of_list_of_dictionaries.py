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
        'https://jsonplaceholder.typicode.com/users')
    users = request_users.json()
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId="
    """
    Data Preparation
    """
    main_dict = {}
    for u in users:
        payload_list = []
        userId = u.get('id')
        todos_updated_url = todos_url + str(userId)
        response_todos = requests.get(todos_updated_url)
        todos = json.loads(response_todos.text)
        for todo in todos:
            task = {}
            task['username'] = u.get('username')
            task['task'] = todo.get('title')
            task['completed'] = todo.get('completed')
            payload_list.append(task)
        main_dict.update({u.get('id'): payload_list})
    """
    Export to JSON
    """
    with open('todo_all_employees.json', 'w') as file:
        json.dump(main_dict, file)
