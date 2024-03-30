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
#put the files on the respective folders
