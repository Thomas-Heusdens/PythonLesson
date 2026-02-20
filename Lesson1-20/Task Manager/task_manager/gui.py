import functions
import FreeSimpleGUI as fsg
import os

if not os.path.exists(functions.FILEPATH):
    with open(functions.FILEPATH, "w") as file:
        pass

fsg.theme("Black")

label = fsg.Text("type in a todo")
input_box = fsg.InputText(tooltip="Enter a todo", key="todo")
add_button = fsg.Button("Add")

list_box = fsg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete",
                             size=10,
                             #image_source="complete.png",
                             key="Complete",
                             tooltip="Complete the todo")

exit_button = fsg.Button('Exit')

window = fsg.Window("My todo app",
                    layout=[[label], [input_box, add_button], [list_box, edit_button, complete_button], [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            new_todo = values["todo"].strip()
            if new_todo:
                todos = functions.get_todos()
                todos.append(new_todo + "\n")
                functions.post_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo'].strip() + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.post_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item to edit first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_delete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_delete)
                functions.post_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                fsg.popup("Please select an item to complete first.", font=("Helvetica", 20))
        case "todos":
            todo = values["todos"][0]
            todo = todo.strip()
            window["todo"].update(value=todo)
        case "Exit" | fsg.WIN_CLOSED:
            break

window.close()