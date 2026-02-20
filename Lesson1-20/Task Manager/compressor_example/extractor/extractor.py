import FreeSimpleGUI as fsg
from zip_extractor import extract_archive

fsg.theme("Black")

label1 = fsg.Text("Select Archive:")
input1 = fsg.Input()
button1 = fsg.FileBrowse("Choose", key="archive")

label2 = fsg.Text("Select Destination:")
input2 = fsg.Input()
button2 = fsg.FolderBrowse("Choose", key="destination")

extract_button = fsg.Button("Extract")
output_label = fsg.Text(key="output")

window = fsg.Window("Extractor", layout=[[label1, input1, button1], [label2, input2, button2], [extract_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Extract":
            extract_archive(values["archive"], values["destination"])
            window["output"].update(value="Extraction completed")
        case fsg.WIN_CLOSED:
            break

window.close()