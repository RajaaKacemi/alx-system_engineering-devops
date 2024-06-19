#!/usr/bin/python3
"""
This module fetches and exports the TODO list progress for all employees
to a JSON file using a REST API.
"""

import json
import requests


def fetch_all_employees_todo_progress():
    """
    Fetch and export the TODO list progress for all employees.

    Returns:
        None
    """
    try:
        # Fetch all users
        users_url = 'https://jsonplaceholder.typicode.com/users'
        users_response = requests.get(users_url)
        users_data = users_response.json()

        if users_response.status_code != 200:
            print("Failed to fetch users.")
            return

        all_tasks = {}

        # Iterate through each user
        for user in users_data:
            employee_id = user.get('id')
            employee_name = user.get('username')

            # Fetch employee's TODO list
            todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            if todos_response.status_code != 200:
                print(f"Failed to fetch TODO list for employee with ID {employee_id}.")
                return

            tasks = []
            for task in todos_data:
                tasks.append({
                    "username": employee_name,
                    "task": task.get('title'),
                    "completed": task.get('completed')
                })

            all_tasks[str(employee_id)] = tasks

        # Write to JSON file
        json_file_name = "todo_all_employees.json"
        with open(json_file_name, mode='w') as json_file:
            json.dump(all_tasks, json_file)

        print(f"Data for all employees has been exported to {json_file_name}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError as e:
        print(f"Error processing data: {e}")


if __name__ == "__main__":
    fetch_all_employees_todo_progress()
