import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["input"] + "\n"
    todos.append(new_todo)
    functions.post_todos(todos)

st.title("My todo app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.post_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo to add", on_change=add_todo, key="input")