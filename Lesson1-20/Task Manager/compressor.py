import FreeSimpleGUI as fsg

label1 = fsg.Text("Select files to compress")
input1 = fsg.Input()
button1 = fsg.FileBrowse("Choose")

label2 = fsg.Text("Select destination for compression")
input2 = fsg.Input()
button2 = fsg.FolderBrowse("Choose")

buttonCompress = fsg.Button("Compress")

window = fsg.Window("Compressor", layout=[[label1, input1, button1], [label2, input2, button2], [buttonCompress]])

window.read()
window.close()