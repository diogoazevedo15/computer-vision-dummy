import os

def log_message(message, log_file_path):
    """
    Writes a message to the specified log file.
    """
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{message}\n")

def read_files_from_directory(directory_path):
    """
    Reads all files from the given directory and returns their contents.
    """
    file_contents = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                file_contents.append(content)
    return file_contents