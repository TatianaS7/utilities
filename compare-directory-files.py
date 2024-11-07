# By default, this script is ignoring the file extension when comparing the files in the directories

import os

missing_files = []

def compare_folders(dir1, dir2):
    dir1_files = [os.path.splitext(file)[0] for file in os.listdir(dir1)]
    dir2_files = [os.path.splitext(file)[0] for file in os.listdir(dir2)]

    # To compare the files with extension, use the below code
    # dir1_files = os.listdir(dir1)
    # dir2_files = os.listdir(dir2)
    
    for file in dir1_files:
        if file not in dir2_files:
            missing_files.append(file)

    for file in dir2_files:
        if file not in dir1_files:
            missing_files.append(file)


if __name__ == "__main__":
    dir1 = ""
    dir2 = ""

    compare_folders(dir1, dir2)

if missing_files:
    print(f"Found {len(missing_files)} missing files")

    for file in missing_files:
        print(f"File {file} is missing in one of the directories")