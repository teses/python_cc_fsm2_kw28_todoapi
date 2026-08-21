

import sqlite3


DATABASE = "todo.db"

def create_database():
    connection = sqlite3.connect(DATABASE)
    connection.execute("PRAGMA foreign_keys = ON")

    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
            todo_title TEXT NOT NULL,
            todo_description TEXT NOT NULL DEFAULT '',
            todo_created_at TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)

    cursor.execute("""
        CREATE TABLE tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            todo_id INTEGER NOT NULL,
            task_title TEXT NOT NULL,
            task_description TEXT NOT NULL DEFAULT '',
            task_status TEXT NOT NULL DEFAULT 'open' CHECK(task_status IN ('open', 'in_progress', 'done')),
            task_priority TEXT NOT NULL DEFAULT 'medium' CHECK(task_priority IN ('low', 'medium', 'high')),
            task_created_at TEXT DEFAULT (datetime('now', 'localtime')),
            task_due_date TEXT ,
            FOREIGN KEY (todo_id) REFERENCES todos(todo_id) ON DELETE CASCADE
        )
    """)

    connection.commit()
    connection.close()
    print("Datenbank wurde erfolgreich erstellt.")


if __name__ == "__main__":
    create_database()

