"""
Title : generate_testing_files.py
Author : Samuel FLORES

Generates a list of files and folders to test
the correct functioning of the program "smart_file_sorter.py".

!! Make sure to empty the folder before running this script.
No duplicate check !!
"""

from pathlib import Path
import sys

BASE_DIRECTORY = Path.cwd()
FOLDERS_TO_CREATE = ("the famous folder", "Docs")
FILES_TO_CREATE = (
    "cabinet.png",
    ".hidden",
    "invoice02.pdf",
    "fake image.png.pdf",
    "new file.txt",
    "new file_(copy).txt",
    "new file_(copy)_(copy).txt",
    "toto.afzfzef",
    "toto_(copy).afzfzef",
)

try:
    # Create empty folders
    for folder in FOLDERS_TO_CREATE:
        Path(BASE_DIRECTORY / folder).mkdir(exist_ok=False)

    # Create empty files
    for file in FILES_TO_CREATE:
        Path(BASE_DIRECTORY / file).touch(exist_ok=False)

    print("The script completed without any errors.")
except FileExistsError as e:
    print(e)
    sys.exit(1)
