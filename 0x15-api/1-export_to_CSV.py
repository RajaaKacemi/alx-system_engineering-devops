#!/usr/bin/python3
"""
This module fetches and exports the TODO list progress for a given employee ID
to a CSV file using a REST API.
"""

import csv
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetch and export the TODO list progress for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    try:
        # Fetch employee details
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        user_response = requests.get(user_url)
        user_data = user_response.json()

        if user_response.status_code != 200 or 'name' not in user_data:
            print(f"Employee with ID {employee_id} not found.")
            return

        employee_name = user_data.get('username')

        # Fetch employee's TODO list
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        if todos_response.status_code != 200:
            print(f"Failed to fetch TODO list for employee with ID {employee_id}.")
            return

        # Prepare CSV file name
        csv_file_name = f"{employee_id}.csv"

        # Write to CSV file
        with open(csv_file_name, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todos_data:
                writer.writerow([
                    employee_id,
                    employee_name,
                    task.get('completed'),
                    task.get('title')
                ])

        print(f"Data for employee ID {employee_id} has been exported to {csv_file_name}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
    except ValueError as e:
        print(f"Error processing data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)

