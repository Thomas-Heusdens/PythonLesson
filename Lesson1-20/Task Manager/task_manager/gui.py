from modules import functions
import FreeSimpleGUI as fsg

label = fsg.Text("type in a todo")
input_box = fsg.InputText(tooltip="Enter a todo", key="todo")
add_button = fsg.Button("Add")

list_box = fsg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = fsg.Button("Edit")

window = fsg.Window("My todo app",
                    layout=[[label], [input_box, add_button], [list_box, edit_button]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.post_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo = values["todos"][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo)
            todos[index] = new_todo
            functions.post_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            todo = values["todos"][0]
            todo.replace("\n", "")
            window["todo"].update(value=todo)
        case fsg.WIN_CLOSED:
            break

window.close()