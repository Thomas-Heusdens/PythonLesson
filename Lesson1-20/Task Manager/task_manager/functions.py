import time

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read the todos text file and return the to-do items."""
    with open(filepath, 'r') as file_get:
        todos_local = file_get.readlines()
    return todos_local

def post_todos(user_todos, filepath=FILEPATH):
    with open(filepath, 'w') as file_post:
        file_post.writelines(user_todos)

#condition to tell python to not run this print if this file is imported in the main file
"""Testing the get_todos function locally"""
if __name__ == "__main__":
    print(get_todos())
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print("it is", now)