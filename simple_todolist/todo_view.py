from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea, QPushButton, QLineEdit, QHBoxLayout, QLabel, QCheckBox

from simple_todolist.todo_model import ToDoModel


class ToDoView(QWidget):
    class ToDoWidget(QWidget):
        def __init__(self, todo: ToDoModel.ToDo, parent=None):
            super().__init__(parent)

            self.tid = todo.tid
            self.setLayout(QHBoxLayout(self))

            self.title_label = QLabel(todo.title, self)
            self.done_checkbox = QCheckBox(self)
            self.done_checkbox.setChecked(todo.done)
            self.delete_button = QPushButton("Delete", self)

            self.layout().addWidget(self.title_label)
            self.layout().addWidget(self.done_checkbox)
            self.layout().addWidget(self.delete_button)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(400, 400)
        self.setLayout(QVBoxLayout(self))

        self.todos_scroll = QScrollArea(self)
        self.todos_scroll.setWidgetResizable(True)
        self.todos_widget = QWidget(self)
        self.todos_widget.setLayout(QVBoxLayout(self.todos_widget))
        self.todos_widget.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        self.todos_scroll.setWidget(self.todos_widget)

        self.new_todo_title_linedit = QLineEdit(self)
        self.new_todo_button = QPushButton("New ToDo", self)

        self.layout().addWidget(self.todos_scroll)
        self.layout().addWidget(self.new_todo_title_linedit)
        self.layout().addWidget(self.new_todo_button)
