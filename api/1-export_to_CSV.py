#!/usr/bin/python3
""""Module"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
        request user info by employee ID.
    """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        convert json to dictionary.
    """
    employee = json.loads(request_employee.text)
    """
        extract username.
    """
    USERNAME = employee.get("username")

    """
        request user's TODO list.
    """
    request_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        dictionary to store task status(completed) in boolean format.
    """
    tasks = {}
    """
        convert json to list of dictionaries.
    """
    user_tasks = json.loads(request_tasks.text)
    """
        loop through dictionary & get completed tasks.
    """
    for dictionary in user_tasks:
        tasks.update({dictionary.get("completed"): dictionary.get("title")})

    """
        export to CSV.
    """
    with open('{}.csv'.format(argv[1]), mode='w') as file:
        csv_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for k, v in tasks.items():
            csv_writer.writerow([argv[1], USERNAME, k, v])
