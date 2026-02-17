from modules import functions
import FreeSimpleGUI as fsg

label = fsg.Text("type in a todo")
input_box = fsg.InputText(tooltip="Enter a todo")
add_button = fsg.Button("Add")
window = fsg.Window("My todo app", layout=[[label], [input_box, add_button]])


window.read()
window.close()