import zipfile

def extract_archive(archive_path, destination_path):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(destination_path)