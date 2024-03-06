# Import necessary modules for testing
import pytest
from app import app, tasks

# Define test functions for the Flask application
def test_index_route():
    # Create a test client for the Flask application
    client = app.test_client()
    # Send a GET request to the '/' route
    response = client.get('/')
    # Check if the response status code is 200 (OK)
    assert response.status_code == 200
    # Check if the response contains expected content
    assert b'Task Management System' in response.data

def test_add_task_route():
    # Create a test client for the Flask application
    client = app.test_client()
    # Define the data to be sent in the POST request
    data = {'title': 'New Task', 'description': 'Description of the new task'}
    # Send a POST request to the '/add' route with the defined data
    response = client.post('/add', data=data, follow_redirects=True)
    # Check if the response status code is 200 (OK) after redirection
    assert response.status_code == 200
    # Check if the new task is added to the tasks list
    assert any(task['title'] == 'New Task' for task in tasks)

# Run pytest to execute the test functions
if __name__ == '__main__':
    pytest.main()
