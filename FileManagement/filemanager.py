import os
import shutil

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if os.path.isfile(full_path):
            ext = filename.split('.')[-1].lower()
            target_folder = os.path.join(folder_path, ext + "_files")

            if not os.path.exists(target_folder):
                os.mkdir(target_folder)

            shutil.move(full_path, os.path.join(target_folder, filename))

    print("Files organized successfully.")

if __name__ == "__main__":
    path = input("Enter the folder path to organize: ")
    organize_folder(path)
