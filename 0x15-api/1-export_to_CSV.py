#!/usr/bin/python3
"""
Accessing a REST API for todo lists of
employees and exporting to CSV
"""

import sys
import requests
import certifi

if __name__ == '__main__':
    # Check for the correct number of command-line args
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    import certifi  # Move certifi import here

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    user_url = url + '/' + employee_id

    try:
        # Make the request with SSL verification
        res_user = requests.get(user_url, verify=certifi.where())

        # Check if the request was successful
        res_user.raise_for_status()

        user_n = res_user.json().get('username')

        todo_url = user_url + '/todos'
        res_todo = requests.get(todo_url, verify=certifi.where())

        # Check if the request was successful
        res_todo.raise_for_status()

        tasks = res_todo.json()

        with open('{}.csv'.format(employee_id), 'w') as file:
            for task in tasks:
                file.write('"{}","{}","{}","{}"\n'.format(employee_id,
                           user_n, task.get('completed'), task.get('title')))

        print("Data exported to {}.csv".format(employee_id))

    except requests.RequestException as e:
        print("Error:", str(e))

