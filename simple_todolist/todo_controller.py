from simple_todolist.todo_model import ToDoModel
from simple_todolist.todo_view import ToDoView


# The controller sets up the view, and controls it entirely.
# The view is dumb, it does nothing on its own.
# The controller also connects the view and the model by updating the view according to the model.
class ToDoController:
    def __init__(self, view: ToDoView, model: ToDoModel):
        self.model = model
        self.view = view

        # Fetch the ToDos from the model and update the view accordingly.
        for todo in self.model.get_todos():
            self.create_todo_widget(todo)

        # Set up the dumb view that does nothing on its own.
        self.view.new_todo_button.pressed.connect(self.new_todo)
        self.view.new_todo_title_linedit.returnPressed.connect(self.view.new_todo_button.click)
        self.view.new_todo_title_linedit.setFocus()

    def new_todo(self):
        title = self.view.new_todo_title_linedit.text()
        self.view.new_todo_title_linedit.setText('')
        # Update the model according to action done by user via the view.
        todo = self.model.new_todo(title)
        # Update the view to be consistent with the model.
        self.create_todo_widget(todo)
        self.view.new_todo_title_linedit.setFocus()

    def delete_todo(self, todo_widget):
        # Update the model.
        self.model.remove_todo(todo_widget.tid)
        # Update the view to be consistent with the model.
        todo_widget.setParent(None)

    def create_todo_widget(self, todo):
        # This is more of "helper" method, it only updates the view.
        todo_widget = ToDoView.ToDoWidget(todo)
        todo_widget.delete_button.pressed.connect(lambda tw=todo_widget: self.delete_todo(tw))
        todo_widget.done_checkbox.stateChanged.connect(lambda checked, tw=todo_widget: self.toggle_todo(tw))
        self.view.todos_widget.layout().addWidget(todo_widget)

    def toggle_todo(self, todo_widget):
        # Update the model
        self.model.toggle_todo(todo_widget.tid)
        # If needed we would have updated the view here to be consistent with model,
        # but in this specific case the view is already consistent with the model.
