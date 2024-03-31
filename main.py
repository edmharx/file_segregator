import platform
import os


#set the dir of the files
directory = (r"C:\Users\edmha\Downloads\test folder")

#create folders depending on file types existing in the dir
def create_folder(directory):
    with os.scandir(directory) as entries: #get the files
        for entry in entries:
            if entry.is_file(): #separate filename and extension
                filename, extension = os.path.splitext(entry.name)
                extension = extension[1:]

                new_folder_name = os.path.join(directory, extension)
                if not os.path.exists(new_folder_name): #create a folder per extension if it does not exist
                    os.mkdir(new_folder_name)
                else:
                    print(f"Folder {new_folder_name} already exists")
                    
                file_path = os.path.join(directory, filename)

                #put the files on the respective folders
                new_file_path = os.path.join (new_folder_name, filename)
                os.rename (file_path, new_file_path)

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