import sqlite3


class ToDoModel:
    class ToDo:
        def __init__(self, todo_tuple):
            self.tid = todo_tuple[0]
            self.title = todo_tuple[1]
            self.done = bool(todo_tuple[2])

        def __repr__(self):
            return f'[{self.tid}] "{self.title}" ({"✔" if self.done else "❌"})'

    def __init__(self):
        self.connection = sqlite3.connect("todo.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS TODOS
(
    TID   INTEGER PRIMARY KEY AUTOINCREMENT,
    TITLE TEXT NOT NULL                            DEFAULT 'Untitled',
    DONE  INTEGER CHECK ( DONE == 0 OR DONE == 1 ) DEFAULT 0
);''')
        self.connection.commit()

    def new_todo(self, title):
        self.cursor.execute('''INSERT INTO TODOS (TITLE) VALUES (:title);''', {
            'title': title,
        })
        self.connection.commit()
        return ToDoModel.ToDo(self.cursor.execute('''SELECT * FROM TODOS ORDER BY TID DESC LIMIT 1;''').fetchall()[0])

    def remove_todo(self, tid):
        self.cursor.execute('''DELETE FROM TODOS WHERE TID = :tid;''', {
            'tid': tid,
        })
        self.connection.commit()

    def toggle_todo(self, tid):
        self.cursor.execute('''UPDATE TODOS SET DONE = NOT DONE WHERE TID = :tid;''', {
            'tid': tid,
        })
        self.connection.commit()

    def get_todos(self):
        return list(map(ToDoModel.ToDo, self.cursor.execute('''SELECT * FROM TODOS;''').fetchall()))

    def get_todo_by_tid(self, tid):
        return ToDoModel.ToDo(self.cursor.execute('''SELECT * FROM TODOS WHERE TID = :tid;''', {
            'tid': tid
        }).fetchall()[0])
