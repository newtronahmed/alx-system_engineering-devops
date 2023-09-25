#!/usr/bin/python3
""" using this REST API, for a given employee ID"""

import requests
import sys

if __name__ == "__main__":
    employeeId = int(sys.argv[1])
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(employeeId))
    employee_name = employee.json().get("name")

    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(employeeId))
    completed_todos = 0
    for todo in todos.json():
        if todo.get("completed"):
            completed_todos += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, completed_todos, len(todos.json())))

    print("\n".join(["\t " + todo.get("title") for todo in todos.json()]))
