import os


def check_path(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            try:
                print(f"File found: {os.path.getsize(path)} bytes")
            except OSError:
                print("File found")
        elif os.path.isdir(path):
            try:
                print(f"Folder found: {os.path.getsize(path)} bytes")
            except OSError:
                print("Folder found")
        else:
            print("Path exists")
    else:
        print("Path not found")


if __name__ == "__main__":
    check_path(".")
    check_path("banking.py")
