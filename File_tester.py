
import os


def folder(folder_path):
        size=0

        File_name= None
        File_size=None

        if os.path.exists(folder_path)==False:
                print("The folder does not exist")
                return

        elif os.path.isfile(folder_path):
                print("The folder is a file")
                return

        elif os.listdir(folder_path)== []:
                print("The folder is empty")
                return

        else:
                for filename in os.listdir(folder_path):

                        full_path = os.path.join(folder_path, filename)


                        if os.path.isfile(full_path):
                                full_size=os.path.getsize(full_path)

                                if full_size > size:
                                        size=full_size
                                        File_name= filename
                                        File_size=full_size

                if File_name==None:
                        print("There is no file in the folder")

                else:
                        print(f"The biggest file in {folder_path} is {File_name} with size {File_size} bytes")

folder(".")
folder("txt.py")