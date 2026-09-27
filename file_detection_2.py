import os

def check_expected_files(folder_path, expected_files):
    if  os.path.exists(folder_path)==False:
        return print("Folder does not exsist")
    

    if os.path.isdir(folder_path) == False:
        return print("Not a valid folder")

    found =[]
    missing=[]

    for filename in expected_files:
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            found.append(filename)
        else:
            missing.append(filename)


    print("=== File Check Results===")
    print(f"Found: {found}")
    print(f"Missing: {missing}")



check_expected_files(".", ["test.txt", "data.csv", "notes.md", "test.py"])
check_expected_files("fake_folder", ["file1.txt"])



    