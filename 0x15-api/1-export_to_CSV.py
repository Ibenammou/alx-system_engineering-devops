#!/usr/bin/python3
"""
Accessing a REST API for todo lists of
employees and exporting to CSV
"""

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

    # print("Number of tasks in CSV:", len(tasks))

    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(employee_id,
                       user_n, task.get('completed'), task.get('title')))

    # print("Data exported to {}.csv".format(employee_id))
