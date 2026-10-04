import os


def folder(folder_path):
    size = -1
    file_name = None
    file_size = None

    if not os.path.exists(folder_path):
        print("The folder does not exist")
        return

    if not os.path.isdir(folder_path):
        print("The path is not a folder")
        return

    try:
        entries = os.listdir(folder_path)
    except OSError as e:
        print(f"Error reading folder: {e}")
        return

    if not entries:
        print("The folder is empty")
        return

    for filename in entries:
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            try:
                full_size = os.path.getsize(full_path)
            except OSError:
                continue

            if full_size > size:
                size = full_size
                file_name = filename
                file_size = full_size

    if file_name is None:
        print("There is no file in the folder")
    else:
        print(f"The biggest file in {folder_path} is {file_name} with size {file_size} bytes")


if __name__ == "__main__":
    folder(".")
    folder("txt.py")
