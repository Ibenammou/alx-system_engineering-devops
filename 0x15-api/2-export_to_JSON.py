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
    url = "https://jsonplaceholder.typicode.com/users"
    user_url = "{}/{}".format(url, employee_id)

    try:
        res_user = requests.get(user_url)
        res_user.raise_for_status()
        user_data = res_user.json()
        user_name = user_data.get('name')
    except requests.RequestException as e:
        print("Error fetching user data:", e)
        sys.exit(1)

    todo_url = "{}/{}/todos".format(url, employee_id)

    try:
        res_todo = requests.get(todo_url)
        res_todo.raise_for_status()
        tasks = res_todo.json()
    except requests.RequestException as e:
        print("Error fetching TODO list:", e)
        sys.exit(1)

    todo_list = []
    for task in tasks:
        todo_list.append(OrderedDict({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_name
        }))

    output_data = OrderedDict({employee_id: todo_list})

    try:
        with open('{}.json'.format(employee_id), 'w') as filename:
            json.dump(output_data, filename, indent=4)
        print("Data exported to {}.json".format(employee_id))
    except IOError as e:
        print("Error writing to file:", e)
