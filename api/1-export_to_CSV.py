#!/usr/bin/python3

"""import the necessary libraries."""

import json
import csv
import requests
from sys import argv


if __name__ == "__main__":

    request_name = requests.get('https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    name_object = json.loads(request_name.text)
    USERNAME = name_object.get('username')
    
    USER_ID = name_object.get('id')
    
    request_tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    tasks_object = json.loads(request_tasks.text)

    tasks = {}
    for dictionary in tasks_object:
        tasks.update({dictionary.get('completed'): dictionary.get('title')})

    with open("{}.csv".format(USER_ID), 'w') as file:
        csv_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)

        for k, v in tasks.items():
            csv_writer.writerow([USER_ID, USERNAME, k, v])
