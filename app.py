
from flask import Flask, request, jsonify, render_template
from backend.main import TaskList

app = Flask(__name__, static_folder='frontend', template_folder='frontend')
db = TaskList()


@app.route('/') # main route to serve the HTML file
def index():
    return render_template('index.html')


@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()

    task_name = data.get('task_name')
    due_date = data.get('due_date')
    completed = data.get('completed')

    db.execute_query('''INSERT INTO task_tracker (task_name, due_date, completed) VALUES (?,?,?)''', (task_name, due_date, completed,))

    return jsonify({"message": "Task successfully added"}), 200


@app.route('/mark_task_complete', methods=['POST'])
def mark_task_complete(task_id):
    
    db.execute_query('''UPDATE task_tracker SET is_complete = 1 WHERE task_id = ?''', (task_id,))


@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    tasks = db.execute_query('''SELECT * FROM task_tracker''')

    if tasks:
        return jsonify(tasks), 200
    else:
        return jsonify({"message": "No tasks in the list"}), 404
    



if __name__ == '__main__':
    app.run(debug=True)
    db.close_connection()

