import os

def check_expected_files(folder_path, expected_files):
    if not os.path.exists(folder_path):
        print("Folder does not exist")
        return None

    if not os.path.isdir(folder_path):
        print("Not a valid folder")
        return None

    found = []
    missing = []

    for filename in expected_files:
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            found.append(filename)
        else:
            missing.append(filename)

    print("=== File Check Results ===")
    print(f"Found: {found}")
    print(f"Missing: {missing}")
    return {"found": found, "missing": missing}



check_expected_files(".", ["test.txt", "data.csv", "notes.md", "test.py"])
check_expected_files("fake_folder", ["file1.txt"])



    