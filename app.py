from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False # Sensitive

# Dummy data to simulate tasks
tasks = [
    {"id": 1, "title": "Task 1", "description": "Complete assignment"},
    {"id": 2, "title": "Task 2", "description": "Prepare presentation"},
    {"id": 3, "title": "Task 3", "description": "Prepare presentation"},
    {"id": 4, "title": "Task 4", "description": "Prepare presentation"}
]

# Route to display all tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    tasks.append({"id": len(tasks) + 1, "title": title, "description": description})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
