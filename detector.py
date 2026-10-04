import os


def analyze_directory(dir_path):
    if not os.path.exists(dir_path):
        print("Directory does not exist")
        return None
    if not os.path.isdir(dir_path):
        print("Not a directory")
        return None

    file_count = 0
    folder_count = 0
    total_size = 0

    try:
        entries = os.listdir(dir_path)
    except OSError as e:
        print(f"Error accessing directory: {e}")
        return None

    for x in entries:
        full_path = os.path.join(dir_path, x)
        if os.path.isfile(full_path):
            file_count += 1
            try:
                total_size += os.path.getsize(full_path)
            except OSError:
                pass
        elif os.path.isdir(full_path):
            folder_count += 1

    print(f"Files: {file_count}")
    print(f"Folders: {folder_count}")
    print(f"Total file size: {total_size}")
    return total_size


if __name__ == "__main__":
    analyze_directory(".")
    analyze_directory("fake_folder")
