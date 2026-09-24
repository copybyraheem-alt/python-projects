import os

def analyze_directory(dir_path):
    if os.path.exists(dir_path)== False:
        print("Directory does not exist")
        return None
    if os.path.isdir(dir_path)== False:
        print("Not a directory")
        return None

    file_count=0
    folder_count = 0
    total_size = 0

    for x in os.listdir(dir_path):
        full_path=os.path.join(dir_path, x)
        if os.path.isfile(full_path):
            file_count+=1
            total_size += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            folder_count+=1
        

    print(f"Files: {file_count}")
    print(f"Folders: {folder_count}")
    print(f'Total file size: {total_size}')
    return total_size



analyze_directory(".")
analyze_directory("fake_folder")

        
    

    
        