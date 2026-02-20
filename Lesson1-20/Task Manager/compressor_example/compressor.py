import FreeSimpleGUI as fsg
from zip_creator import make_archive

label1 = fsg.Text("Select files to compress")
input1 = fsg.Input(key="input_files")
button1 = fsg.FilesBrowse("Choose", key="source")

label2 = fsg.Text("Select destination for compression")
input2 = fsg.Input(key="input_folder")
button2 = fsg.FolderBrowse("Choose", key="destination")

output_label = fsg.Text(key="output")
buttonCompress = fsg.Button("Compress")

window = fsg.Window("Compressor", layout=[[label1, input1, button1], [label2, input2, button2], [buttonCompress, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Compress":
            filepaths = values["source"].split(";")
            folder = values["destination"]
            make_archive(filepaths, folder)
            window["output"].update(value="Compression Completed")
        case fsg.WIN_CLOSED:
            break

window.close()