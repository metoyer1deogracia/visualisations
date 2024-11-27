import os
import shutil

# Define files and directories to be removed
files_to_delete = [
    "organize_files.py",
    "setup_project.py",
    "automate_dashboard_setup.py",
    "automate_refactoring.py",
    "dashboard_generator.py"
]

dirs_to_delete = [
    "prvsnl_cmptbl/src"
]

# Delete files
for file in files_to_delete:
    if os.path.isfile(file):
        os.remove(file)
        print(f"Deleted file: {file}")
    else:
        print(f"File not found: {file}")

# Delete directories
for directory in dirs_to_delete:
    if os.path.isdir(directory):
        shutil.rmtree(directory)
        print(f"Deleted directory: {directory}")
    else:
        print(f"Directory not found: {directory}")
