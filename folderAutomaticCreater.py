import os
from tkinter.filedialog import askdirectory

def create_folders(folders):
    path=askdirectory()
    for folder in folders:
        try:
            os.makedirs(folder)
            print(f"folder '{folder}' createated successfully")
        except FileExistsError:
            print(f"Folder '{folder}' already exsists")

if __name__ == "__main__":
    folder_names =['Folder1', 'folder2', 'folder3', 'folder4']
    create_folders(folder_names)

