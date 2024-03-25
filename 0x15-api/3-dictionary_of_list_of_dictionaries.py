#!/usr/bin/python3
"""
Script to retrieve TODO list progress for a given employee ID
using a REST API
"""

import json
import requests


def fetch_data(employee_id):
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    res = requests.get(user_url.format(employee_id))
    res.raise_for_status()
    return (res.json())


def fetch_todo(employee_id):
    tasks_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    res = requests.get(tasks_url.format(employee_id))
    res.raise_for_status()
    return (res.json())


def export_to_json():
    all_data = {}

    for employee_id in range(1, 11):
        user_data = fetch_data(employee_id)
        employee_name = user_data.get('username')
        tasks = fetch_todo(employee_id)

        employee_data = []
        for task in tasks:
            employee_data.append({"username": employee_name,
                                  "task": task.get('title'),
                                  "completed": task.get('completed')})

        # Extracting relevant info
        all_data[employee_id] = employee_data

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_data, json_file, separators=(',', ':'))

    # print("Data exported to todo_all_employees.json")


if __name__ == '__main__':
    export_to_json()
