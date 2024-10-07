import os
import shutil


def copy_files(source_path, destination_path):
    
    os.mkdir(destination_path)
    print(f"File with destination {destination_path} created")

    files_in_source = os.listdir(source_path)

    for file in files_in_source:
        file_path = os.path.join(source_path, file)
        
        if os.path.isfile(file_path):
            shutil.copy(file_path,destination_path)
            print(f"{file_path} copied to {destination_path}")
        
        else:
            copied_to = os.path.join(destination_path, file)
            print(f"Recursively copy files of directory {file_path}")
            copy_files(file_path, copied_to)

