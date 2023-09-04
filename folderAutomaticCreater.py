import os
from tkinter.filedialog import askdirectory

def create_folders(folders: list, sub1_folder: str, sub2_folder: str):
    path = askdirectory()
    for folder in folders:
        try:
            targetPath = fr'{path}/{folder}'
            os.makedirs(targetPath)
            print(f"folder '{folder}' createated successfully")

            targetPath = fr'{path}/{folder}/{sub1_folder}'
            os.makedirs(targetPath)
            print(f"folder '{folder}/{sub1_folder}' createated successfully")

            targetPath = fr'{path}/{folder}/{sub2_folder}'
            os.makedirs(targetPath)
            print(f"folder '{folder}/{sub2_folder}' createated successfully")

            targetPath = fr'{path}/{folder}/{sub3_folder}'
            os.makedirs(targetPath)
            print(f"folder '{folder}/{sub3_folder}' createated successfully")

            targetPath = fr'{path}/{folder}/{sub4_folder}'
            os.makedirs(targetPath)
            print(f"folder '{folder}/{sub4_folder}' createated successfully")

            targetPath = fr'{path}/{folder}/{sub5_folder}'
            os.makedirs(targetPath)
            print(f"folder '{folder}/{sub5_folder}' createated successfully")

        except FileExistsError:
            print(f"Folder '{folder}' already exsists")


if __name__ == "__main__":
    folder_names = ['Folder1', 'folder2', 'folder3', 'folder4']
    sub1_folder: str = 'Drawings'
    sub2_folder: str = 'Electronic Test File'
    sub3_folder: str = 'Test_Report_(Text)'
    sub3_folder: str = 'Instructions'
    sub4_folder: str = 'Settings_(Text)'
    sub5_folder: str = 'Check_Sheets'
    create_folders(folder_names, sub1_folder, sub2_folder)
