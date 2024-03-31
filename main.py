import shutil
import os


#set the dir of the files
directory = (r"C:\Users\edmha\Downloads\test folder")

#create folders depending on file types existing in the dir
def create_folder(directory):
    with os.scandir(directory) as files: #get the files
        for file in files:
            if file.is_file(): #separate filename and extension
                filename, extension = os.path.splitext(file.name)
                extension = extension[1:]

                new_folder_name = os.path.join(directory, extension)
                if not os.path.exists(new_folder_name): #create a folder per extension if it does not exist
                    os.mkdir(new_folder_name)
                else:
                    print(f"Folder {extension} already exists")
                
                #put the files on the respective folders
                file_path = os.path.join(directory, file)
                shutil.move(file_path, new_folder_name)


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