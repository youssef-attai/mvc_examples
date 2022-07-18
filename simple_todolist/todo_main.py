from PySide6.QtWidgets import QApplication

from simple_todolist.todo_controller import ToDoController
from simple_todolist.todo_model import ToDoModel
from simple_todolist.todo_view import ToDoView


def main():
    todo_app = QApplication([])
    todo_model = ToDoModel()
    todo_view = ToDoView()
    todo_view.show()
    todo_controller = ToDoController(todo_view, todo_model)
    todo_app.exec()


if __name__ == '__main__':
    main()
