import platform
import os


#set the dir of the files
directory = (r"C:\Users\edmha\OneDrive\Desktop\Importants")

#checking if the directory exists
if os.path.exists(directory):
    #open directory
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file(): #read file type
                filename, extension = os.path.splitext(entry.name)
                print(f"File: {entry.name}, Extension: {extension}")
else:
    print("Please type an existing directory")

#create folders depending on file types existing in the dir
def create_folder():
    folder_path = directory / extension
    for extension in entries:
        if not folder_path.exists():
            #folder_path.mkdir()
            print(f"Folder '{extension}' created successfully in '{directory}'")
        else:
            print(f"Folder '{extension}' already exists in '{directory}'")
        
#put the files on the respective folders

create_folder()