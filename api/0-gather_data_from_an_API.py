#!/usr/bin/python3
"""
    python script that returns TODO list progress for a given employee ID.
"""
import json
from pip._vendor import requests
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
        extract employee name.
    """
    employee_name = employee.get("name")

    """
        request user's TODO list.
    """
    request_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        dictionary to store task status in boolean format.
    """
    tasks = {}
    """
        convert json to list of dictionaries.
    """
    employee_todos = json.loads(request_tasks.text)
    """
        loop through dictionary & get completed tasks.
    """
    for dictionary in employee_todos:
        tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        return name, total number of tasks & completed tasks.
    """
    
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for k, v in tasks.items():
        if v is True:
            print("\t {}".format(k))