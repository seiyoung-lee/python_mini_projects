import os
from pathlib import Path
import shutil

previous_directory = os.getcwd()
split_directory = previous_directory.split("/")
downloads_directory = f"/{split_directory[1]}/{split_directory[2]}/Downloads"
desktop_directory = f"/{split_directory[1]}/{split_directory[2]}/Desktop"

os.chdir(downloads_directory)

files_change = []
ready_files = {}
directories = {}

for file in os.listdir():
    if file[0] != ".":
        path = file.split("&&")
        if path[0] == "readymove":
            desktop_directory_curr = desktop_directory
            for p in path:
                if p == "readymove":
                    continue
                if len(p.split(".")) > 1:
                    continue
                desktop_directory_curr = desktop_directory_curr + "/" + p
                if not os.path.isdir(desktop_directory_curr):
                    os.mkdir(desktop_directory_curr)
            f = Path(file)

            f.rename(f"{path[len(path) - 1]}")
            shutil.move(f"{path[len(path) - 1]}", desktop_directory_curr)



