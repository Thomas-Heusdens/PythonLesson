import zipfile
import pathlib

def make_archive(filepaths, destination_directory):
    dest_path = pathlib.Path(destination_directory, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for file in filepaths:
            filepath = pathlib.Path(file)
            archive.write(filepath, arcname=filepath.name)