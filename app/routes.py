from flask import render_template, redirect, url_for, request
from app import app

# Define dummy data for demonstration
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'Description of Task 1',
        'due_date': '2023-01-01',
        'priority': 'High',
        'completed': False,
        'project_id': 1,
        'project_name': 'Project 1'
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'Description of Task 2',
        'due_date': '2023-02-01',
        'priority': 'Medium',
        'completed': True,
        'project_id': 1,
        'project_name': 'Project 1'
    },
    {
        'id': 3,
        'title': 'Task 3',
        'description': 'Description of Task 3',
        'due_date': '2023-03-01',
        'priority': 'Low',
        'completed': False,
        'project_id': 2,
        'project_name': 'Project 2'
    }
]

projects = [
    {
        'id': 1,
        'name': 'Project 1',
        'description': 'Description of Project 1',
        'task_count': 2
    },
    {
        'id': 2,
        'name': 'Project 2',
        'description': 'Description of Project 2',
        'task_count': 1
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', tasks=tasks)

@app.route('/task/<int:task_id>')
def task_details(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return render_template('task_details.html', task=task)
    else:
        return 'Task not found'

@app.route('/project-management')
def project_management():
    return render_template('project_management.html', projects=projects)

@app.route('/user-profile')
def user_profile():
    user = {'username': 'JohnDoe', 'email': 'johndoe@example.com'}
    return render_template('user_profile.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
