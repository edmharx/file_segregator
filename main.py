import platform
import os


#set the dir of the files
directory = (r"C:\Users\edmha\OneDrive\Desktop\Importants")

#create folders depending on file types existing in the dir
def create_folder(directory):
    with os.scandir(directory) as entries: #get the files
        for entry in entries:
            if entry.is_file(): #separate filename and extension
                filename, extension = os.path.splitext(entry.name)
                extension = extension[1:]

        new_folder_name = os.path.join(directory, extension)
        if not new_folder_name.exists(): #create a folder per extension if it does not exist
            new_folder_name.mkdir()

        #put the files on the respective folders
        move_to_folder = os.path.join (new_folder_name, filename)
        move_to_folder()

if os.path.exists(directory):
    create_folder(directory)
    print("Folders are created succcessfully")
else:
    print ("Please use a valid directory")


#get the directory
#get the files
#separate filename and extension
#create a folder per extension if it does not exist
#move the file to the respective folder