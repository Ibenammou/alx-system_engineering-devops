#!/usr/bin/python3
"""
Accessing a REST API for todo lists of
employees and exporting to JSON
"""

from collections import OrderedDict
import json
import requests
import sys


if __name__ == '__main__':
    # Check for the correct number of command-line args
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = ("https://jsonplaceholder.typicode.com/users/"
                "{}".format(employee_id))

    res_user = requests.get(user_url)
    res_user.raise_for_status()

    user_id = res_user.json().get('id')

    todo_url = "{}/todos".format(user_url)
    res_todo = requests.get(todo_url)
    res_todo.raise_for_status()

    tasks = res_todo.json()

    diction = OrderedDict({user_id: []})
    for task in tasks:
        diction[user_id].append(OrderedDict({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": res_user.json().get('username')
        }))

    with open('{}.json'.format(user_id), 'w') as filename:
        json.dump(diction, filename)
