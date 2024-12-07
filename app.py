
from flask import Flask, request, jsonify, render_template
from main import TaskList

app = Flask(__name__)
db = TaskList()


@app.route('/') # main route to serve the HTML file
def index():
    return render_template('index.html')


@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()

    task_name = data.get('task_name')
    due_date = data.get('due_date')
    # completed = data.get('completed')

    db.execute_query('''INSERT INTO task_tracker (task_name, due_date) VALUES (?,?)''', (task_name, due_date))
    tasks = db.execute_query('''SELECT * FROM task_tracker''')
    # print(tasks)
    return jsonify({"message": "Task successfully added"}), 200


@app.route('/mark_task_complete', methods=['POST'])
def mark_task_complete():
    data = request.get_json() # get json data from request
    task_id = data.get('task_id') # extract task_id from JSON body

    if task_id is None:
        return jsonify({"message": "No task_id provided"}), 400

    db.execute_query('''UPDATE task_tracker SET completed = 1 WHERE task_id = ?''', (task_id,))

    return jsonify({"message": f"Task {task_id} marked as complete"}), 200


@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    tasks = db.execute_query('''SELECT * FROM task_tracker''')
    # print(tasks)
    if tasks:
        return jsonify(tasks), 200
    else:
        return jsonify([]), 200
        # return jsonify({"message": "No tasks in the list"}), 404
    



if __name__ == '__main__':
    app.run(debug=True)
    db.close_connection()

