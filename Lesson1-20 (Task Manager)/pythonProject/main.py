while True:
    action = input("Enter add, show, edit, delete, or exit:")
    action = action.strip()
    match action:
        case 'add':
            todo = input("Enter a todo:") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show' | 'display':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                fstring = f"{index + 1}. {item}"
                print(fstring)
        case 'edit':
            number = int(input("Type number of the todo:"))
            number -= 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Whats the new todo:")
            todos[number] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete' | 'delete':
            number = int(input("Type number of the todo you want to delete:"))
            number -= 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            old_todo = todos[number].strip("\n")
            todos.remove(todos[number])

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            print(f"Todo '{old_todo}' was removed from the list of todos.")
        case 'exit':
            break
        case _:
            print("Try and learn to write properly please")

print("Bye")