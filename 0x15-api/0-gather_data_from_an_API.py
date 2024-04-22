#!/usr/bin/env python3
"""This script returns information about an employee's TODO list progress"""
import urllib.request
import urllib.error
import json
import sys

def fetch_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        with urllib.request.urlopen(user_url) as response:
            user_data = json.loads(response.read().decode())

        with urllib.request.urlopen(todos_url) as response:
            todos_data = json.loads(response.read().decode())

        completed_tasks = [task['title'] for task in todos_data if task['completed']]
        total_tasks = len(todos_data)
        num_completed_tasks = len(completed_tasks)
        
        print(f"Employee {user_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task}")

    except urllib.error.URLError as e:
        print("Error: ", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_todo_progress(employee_id)
