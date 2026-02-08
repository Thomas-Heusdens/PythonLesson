while True:
    action = input("Enter add, show, edit, delete, or exit:")
    action = action.strip()
    if 'add' in action:
        todo = action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'show' in action or 'display' in action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            fstring = f"{index + 1}. {item}"
            print(fstring)
    elif 'edit' in action:
        number = int(action[5:])
        number -= 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Whats the new todo:")
        todos[number] = new_todo + "\n"

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'complete' in action or 'delete' in action:
        number = int(action[9:])
        number -= 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        old_todo = todos[number].strip("\n")
        todos.remove(todos[number])

        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        print(f"Todo '{old_todo}' was removed from the list of todos.")
    elif 'exit' in action:
        break
    else:
        print("command is not valid")

print("Bye")