def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


def append_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)


def list_files(directory):
    import os
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def create_directory(directory):
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)


def delete_file(file_path):
    import os
    if os.path.isfile(file_path):
        os.remove(file_path)