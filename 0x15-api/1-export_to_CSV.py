#!/usr/bin/python3
"""
This script uses REST API for a given employee ID
"""

import csv
import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com"
    url_todos = "{url}/todos".format(url=url)
    url_users = "{url}/users/{id}".format(url=url, id=sys.argv[1])
    response_user = requests.get(url_users)
    response_todos = requests.get(url_todos, params={'userId': sys.argv[1]})
    response_todos_json = response_todos.json()
    response_user_json = response_user.json()
    with open(sys.argv[1] + ".csv", mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',',
                                     quotechar='"', quoting=csv.QUOTE_ALL)
        for todos in response_todos_json:
            employee_writer.writerow([sys.argv[1],
                                      response_user_json.get('username'),
                                      todos.get('completed'),
                                      todos.get('title')])
            