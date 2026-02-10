def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

while True:
    action = input("Enter add, show, edit, delete, or exit:")
    action = action.strip()
    if action.startswith('add'):
        todo = action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif action.startswith('show') or action.startswith('display'):
        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            fstring = f"{index + 1}. {item}"
            print(fstring)
    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("Whats the new todo:")
            todos[number] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid. Please use a number to refer to the todo you want to edit.")
            continue

    elif action.startswith('complete'):
        try:
            number = int(action[9:])
            number -= 1

            todos = get_todos()
            old_todo = todos[number].strip("\n")
            todos.remove(todos[number])

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            print(f"Todo '{old_todo}' was removed from the list of todos.")
        except IndexError:
            print("There is no item with that number.")
            continue
    elif action.startswith('exit'):
        break
    else:
        print("command is not valid")

print("Bye")