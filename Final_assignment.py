import os
import shutil

def scan_directory(dir_path):
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    return files

def group_files_by_extension(files):
    file_groups = {}
    for file in files:
        extension = os.path.splitext(file)[1]
        if extension not in file_groups:
            file_groups[extension] = []
        file_groups[extension].append(file)
    return file_groups

def move_files_to_folders(file_groups, dir_path):
    for extension in file_groups:
        folder_path = os.path.join(dir_path, extension[1:]) 
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        for file in file_groups[extension]:
            shutil.move(os.path.join(dir_path, file), os.path.join(folder_path, file))

def main():
    dir_path = '/path/to/your/directory' 
    files = scan_directory(dir_path)
    file_groups = group_files_by_extension(files)
    move_files_to_folders(file_groups, dir_path)

if __name__ == "__main__":
    main()
