
import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "../db/task_tracker.db")

class TaskList:
    def __init__(self):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self._initialize_database()

    def _initialize_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS task_tracker (
                            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            task_name TEXT,
                            due_date DATE,
                            completed BOOLEAN)''') # YYYY-MM-DD
        self.connection.commit()

    def execute_query(self, query, data=None):
        
        if not data:
            try:
                self.cursor.execute(query)
            except sqlite3.IntegrityError:
                print(f"SQL error!\nQuery: {query}")
        else:
            try:
                self.cursor.execute(query, data)
            except sqlite3.IntegrityError:
                print(f"SQL error!\nQuery: {query}\nData: {data}")

    def close_connection(self):
        self.connection.close()
        print("connection to task_tracker terminated")