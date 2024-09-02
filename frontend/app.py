from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

API_URL = os.environ.get('API_URL', 'http://backend:8000')

@app.route('/')
def index():
    tasks = requests.get(f'{API_URL}/tasks').json()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    owner = request.form['owner']
    task_name = request.form['task_name']
    requests.post(f'{API_URL}/tasks', json={"owner": owner, "task_name": task_name})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    requests.delete(f'{API_URL}/tasks/{task_id}')
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    task_name = request.form['task_name']
    requests.put(f'{API_URL}/tasks/{task_id}', json={"task_name": task_name})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
