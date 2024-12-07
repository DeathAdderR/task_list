
import sqlite3
import os

class TaskList:
    def __init__(self):
        self.connection = sqlite3.connect('task_tracker.db', check_same_thread=False)
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
        
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)

            if query.strip().lower().startswith('select'):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return None
        except sqlite3.IntegrityError as e:
            print(f"SQL ERROR!\nQuery: {query}\nData: {data if data else ''}\nError: {e}")
        

    def close_connection(self):
        self.connection.close()
        print("connection to task_tracker terminated")

