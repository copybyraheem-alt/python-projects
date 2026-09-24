import os


def check_path(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            print(f"File found: {os.path.getsize(path)}")
        elif os.path.isdir(path):
            print(f"Folder found: {os.path.getsize(path)} bytes")
    else:
        print("Path not found")



check_path(".")
check_path("banking.py")