#!/usr/bin/python3
"""Get the necessary libraries."""

from pip._vendor import requests
from sys import argv
import json


if __name__ == "__main__":
    request_name = requests.get('https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    name_object = json.loads(request_name.text)
    name = name_object.get('name')
    
    request_tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos/'.format(argv[1]))
    tasks_object = json.loads(request_tasks.text)

    tasks = {}
    for dictionary in tasks_object:
        tasks.update({dictionary.get('title'): dictionary.get('completed')})
    
    completed_tasks = []
    for i in tasks.values():
        if i is True:
            completed_tasks.append(i)
    
    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(tasks)

    print('Employee {} is done with tasks({}/{}):'.format(name, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for k, v in tasks.items():
        if v is True:
            print('\t {}'.format(k))