#!/usr/bin/python3
"""
Accessing a REST API for todo lists of
employees and exporting to CSV
"""

from collections import OrderedDict
import json
import requests
import sys


if __name__ == '__main__':
    # Check for the correct number of command-line args

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    user_url = url + '/' + employee_id

    res_user = requests.get(user_url)
    # res_user.raise_for_status()

    # user_id = res_user.json().get('id')
    user_n = res_user.json().get('user_n')
    # print("User ID: {} / Username: {}".format(user_id, user_n))

    todo_url = user_url + '/todos'
    res_todo = requests.get(todo_url)
    # res_todo.raise_for_status()

    tasks = res_todo.json()
    # sorted_tasks = sorted(tasks, key=lambda x: x['title'])
    diction = OrderedDict({employee_id: []})
    for task in tasks:
        diction[employee_id].append(OrderedDict({"task": task.get('title'),
                                                 "completed":
                                                 task.get('completed'),
                                                 "username": user_n}))

    # sorted_entries = sorted(diction[employee_id], key=lambda x: x['task'])
    # diction[employee_id] = sorted_entries

    with open('{}.json'.format(employee_id), 'w') as filename:
        json.dump(diction, filename)
