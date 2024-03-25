#!/usr/bin/python3
"""
Script to retrieve TODO list progress for a given employee ID
using a REST API
"""

import requests
from sys import argv


def fetch_data(employee_id):
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    res = requests.get(user_url.format(employee_id))
    res.raise_for_status()
    return (res.json().get('name'))


def fetch_todo(employee_id):
    tasks_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    res = requests.get(tasks_url.format(employee_id))
    res.raise_for_status()
    return (res.json())


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    try:
        employee_name = fetch_data(employee_id)
        tasks = fetch_todo(employee_id)

        done = 0
        done_tasks = []

        # Extracting relevant info
        for task in tasks:
            if task.get('completed'):
                done_tasks.append(task)
                done += 1

        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, done, len(tasks)))

        for task in done_tasks:
            print("\t {}".format(task.get('title')))

    except requests.RequestException as e:
        print("Error fetching data:", str(e))
