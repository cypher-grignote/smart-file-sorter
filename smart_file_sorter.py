"""
Title : smart_file_sorter.py
Author : Samuel FLORES

Allows sorting the contents of a directory into appropriate folders.
Does not modify hidden items (those beginning with a dot).


Music : aac, alac, flac, m4a, mp3, ogg, wma

Video : avi, flv, m4v, mkv, mov, mp4, webm

Picture : ai, bmp, gif, heic, heif, jpeg, jpg, png, psd, raw, svg, tiff, webp,
xcf

Spreadsheet : csv, ods, xls, xlsm, xlsx

PowerPoint : key, odp, ppt, pptx

Document : docx, fb2, md, odt, pages, pdf, rtf, rtfd, tex, txt

Archive : 7z, bz2, gz, rar, tar, zip

Ebook : azw3, epub, mobi, prc

Development: c, cpp, cs, css, go, h, html, ipynb, java, js, json, php, py, rs, sh,
ts, tsx, xml, yaml, yml

Application : appimage, bat, deb, dmg, exe, img, iso, msi, snap, vbs

Miscellaneous : other

Directory : directories
"""

from os import access, W_OK
import sys
from pathlib import Path


def create_directory(new_directory: Path) -> None:
    """Allows to create a directory by checking if it already exists.

    Args:
        new_directory (Path): Absolute path of the directory to be created.
    """
    if not new_directory.is_dir():
        Path(new_directory).mkdir()
        print(f"The folder '{new_directory.name}' has been created.")


def display_move(src_name: str, dest_name: str) -> None:
    """Displays the name change when moving a file.

    Args:
        src_name (str): Filename before moving.
        dest_name (str): Filename after moving.
    """
    if src_name != dest_name:
        print(f"'{src_name}' → '{dest_name}'\n")


def white_list(name: str, WHITE_LIST: set, FORMATS: dict) -> bool:
    """Prevents modification of the folders used for sorting, hidden
     elements, and the script itself.

    Args:
        name (str): Filename.
        WHITE_LIST (set): List of names not to touch.
        FORMATS (dict): Folder names used for sorting.

    Returns:
        bool: True if the file is whitelisted, False if it is not.
    """
    return name in WHITE_LIST or name.startswith(".") or name in FORMATS.keys()


def f_base_directory(args: tuple[str, ...]) -> Path:
    """Retrieves the directory to sort. This can be the current directory, the
    first argument, or it displays an error.

    Args:
        args (tuple[str, ...]): Tuple containing the args (sys.argv).

    Returns:
        Path: Returns the path of the directory to be sorted. Terminates
        the program if an error occurs.
    """
    nb_args = len(args) - 1
    if not nb_args:
        BASE_DIRECTORY = Path.cwd()
    elif nb_args == 1:
        BASE_DIRECTORY = Path(args[1])  # Convert str to path
    else:  # If more than one arg
        error("Invalid number of arguments: 0 or a single argument expected.")
    base_directory_errors(BASE_DIRECTORY)
    return BASE_DIRECTORY


def base_directory_errors(BASE_DIRECTORY: Path) -> None:
    """Displays an error if the directory is invalid or if the program does not
    have write permission.

    Args:
        BASE_DIRECTORY (Path): Path of the directory to be sorted.
    """
    if not BASE_DIRECTORY.exists() or not BASE_DIRECTORY.is_dir():
        error("Error: The directory provided as an argument is invalid.")
    if not access(BASE_DIRECTORY, W_OK):
        error(
            f"""Error: The program does not have write permissions on the
             directory {BASE_DIRECTORY}"""
        )


def file_name_existing_without_extension(new_directory: Path, new_file: Path) -> Path:
    """Checks if a file WITHOUT an extension or a folder already exists before
    moving it. If it already exists, appends _(copy) to the name.

    Args:
        new_directory (Path): Destination directory.
        new_file (Path): Absolute path of the file before moving.

    Returns:
        Path: Absolute path of the file with the new name.
    """
    if new_file.exists():
        print(f"The file '{new_file.name}' already exists.")
    while new_file.exists():
        new_file = new_directory / f"{new_file.name}_(copy)"
    return new_file


def file_name_existing_with_extension(
    new_directory: Path, new_file: Path, extension: str
) -> Path:
    """Checks if a file WITH an extension already exists before moving it.
    If it already exists, appends _(copy) to the name.

    Args:
        new_directory (Path): Destination directory.
        new_file (Path): Absolute path of the file before moving.
        extension (str): File extension. Example: '.png'.

    Returns:
        Path: Absolute path of the file with the new name.
    """
    if new_file.exists():
        print(f"The file '{new_file.name}' already exists.")
    while new_file.exists():
        stem = new_file.stem
        new_file = new_directory / f"{stem}_(copy){extension}"
    return new_file


def error(msg: str):
    """Displays an error message. Pauses so the user can read it.
    Then terminates the program with an error code.

    Args:
        msg (str): Error message to display.
    """
    print(msg)
    input("Press Enter to exit...")
    sys.exit(1)


def success():
    """Displays a message when the program executes successfully.
    Then terminates the program.
    """
    print("Sorting completed successfully.")
    input("Press Enter to exit...")
    sys.exit(0)


PYTHON_SCRIPT_NAME = Path(sys.argv[0]).name
WHITE_LIST = {
    "Directory",
    "Miscellaneous",
    PYTHON_SCRIPT_NAME,
    "generate_testing_files.py",
}
args = sys.argv
FORMATS = {
    "Music": {".aac", ".alac", ".flac", ".m4a", ".mp3", ".ogg", ".wma"},
    "Video": {".avi", ".flv", ".m4v", ".mkv", ".mov", ".mp4", ".webm"},
    "Picture": {
        ".ai",
        ".bmp",
        ".gif",
        ".heic",
        ".heif",
        ".jpeg",
        ".jpg",
        ".png",
        ".psd",
        ".raw",
        ".svg",
        ".tiff",
        ".webp",
        ".xcf",
    },
    "Spreadsheet": {".csv", ".ods", ".xls", ".xlsm", ".xlsx"},
    "PowerPoint": {".key", ".odp", ".ppt", ".pptx"},
    "Document": {
        ".docx",
        ".fb2",
        ".md",
        ".odt",
        ".pages",
        ".pdf",
        ".rtf",
        ".rtfd",
        ".tex",
        ".txt",
    },
    "Archive": {".7z", ".bz2", ".gz", ".rar", ".tar", ".zip"},
    "Ebook": {".azw3", ".epub", ".mobi", ".prc"},
    "Development": {
        ".c",
        ".cpp",
        ".cs",
        ".css",
        ".go",
        ".h",
        ".html",
        ".ipynb",
        ".java",
        ".js",
        ".json",
        ".php",
        ".py",
        ".rs",
        ".sh",
        ".ts",
        ".tsx",
        ".xml",
        ".yaml",
        ".yml",
    },
    "Application": {
        ".appimage",
        ".bat",
        ".deb",
        ".dmg",
        ".exe",
        ".img",
        ".iso",
        ".msi",
        ".snap",
        ".vbs",
    },
}
BASE_DIRECTORY = f_base_directory(tuple(args))

for element in BASE_DIRECTORY.iterdir():
    name = element.name

    if white_list(name, WHITE_LIST, FORMATS):
        continue

    name_without_extension = element.stem
    extension = element.suffix.lower()

    if not extension:
        if element.is_dir():
            new_directory = Path(BASE_DIRECTORY / "Directory")
            create_directory(new_directory)
            new_file = new_directory / name
            new_file = file_name_existing_without_extension(new_directory, new_file)
            element.rename(new_file)
            display_move(name, new_file.name)

        else:
            new_directory = Path(BASE_DIRECTORY / "Miscellaneous")
            create_directory(new_directory)
            new_file = new_directory / name
            new_file = file_name_existing_without_extension(new_directory, new_file)
            element.rename(new_file)
            display_move(name, new_file.name)
    else:
        for directory, extensions in FORMATS.items():
            if extension in extensions:
                new_directory = Path(BASE_DIRECTORY / directory)
                create_directory(new_directory)
                new_file = new_directory / name
                new_file = file_name_existing_with_extension(
                    new_directory, new_file, extension
                )
                element.rename(new_file)
                display_move(name, new_file.name)
                break

# To sort the elements with unknown extension
for element in BASE_DIRECTORY.iterdir():
    name = element.name
    if white_list(name, WHITE_LIST, FORMATS):
        continue
    if not element.is_file():
        continue

    extension = element.suffix.lower()
    name_without_extension = element.stem

    new_directory = Path(BASE_DIRECTORY / "Miscellaneous")
    create_directory(new_directory)
    new_file = new_directory / name
    new_file = file_name_existing_with_extension(new_directory, new_file, extension)
    element.rename(new_file)
    display_move(name, new_file.name)
success()
