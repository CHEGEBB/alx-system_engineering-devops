#!/usr/bin/python3
"""
Scrript using REST API for a given employee ID
Returns information about his/her TODO list progress
"""

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
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for todos in response_todos_json:
        if todos.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1
        else:
            TOTAL_NUMBER_OF_TASKS += 1
    print("Employee {} is done with tasks({}/{}):".format
          (response_user_json.get('name'),
           NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for todos in response_todos_json:
        if todos.get('completed') is True:
            print("\t {}".format(todos.get('title')))
