# Smart File Sorter

A simple Python script to automatically sort the contents of a directory into categorized folders.
It organizes files by type (music, video, documents, pictures, archives, etc.) and handles duplicates by appending `_(copy)`.

---

## Features
- Sorts files into predefined categories (Application, Archive, Development, Directory, Document, Ebook, Miscellaneous, Music, Picture, PowerPoint, Spreadsheet, Video).
- Supports a wide range of file extensions (see source code for the full list).
- Automatically creates destination folders if they do not exist.
- Prevents overwriting by renaming duplicates with `_(copy)`.
- Skips hidden files and the script itself.

---

## Usage

### Sort files
1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/your-username/smart-file-sorter.git
   cd smart-file-sorter
   ```
2. Run the script on the current directory:
    ```bash
    python smart_file_sorter.py
    ```
3. Or run it on a specific directory:
    ```bash
    python smart_file_sorter.py /path/to/directory
    ```

### Run prebuilt executables
If you don’t have Python installed, you can use the prebuilt binaries:

- **Windows**: `smart-file-sorter-windows-x64.zip`
- **Linux**: `smart-file-sorter-linux-x64.zip`
- **macOS (arm64)**: `smart-file-sorter-macos-arm64.zip`

Example on Linux:
```bash
./linux_smart_file_sorter ~/Downloads
```

Example on macOS:
```bash
./macos_smart_file_sorter ~/Downloads
```

Example on Windows (PowerShell):
```powershell
.\win_smart_file_sorter.exe "C:\Users\$env:USERNAME\Downloads"
```
Or just double-click on it to sort its own directory.

On macOS, you may need to allow the binary in System Settings → Privacy & Security → Full Disk Access, or remove quarantine flags:
```bash
xattr -dr com.apple.quarantine ./macos_smart_file_sorter
```

---

## Generate test files
A helper script `generate_testing_files.py` is provided.
It creates sample files/folders in the current directory so you can quickly test sorting.

Run it with:
```bash
python generate_testing_files.py
```
Make sure the directory is empty before running this script (no duplicate checks).

---

## Project structure

```
.
├── smart_file_sorter.py        # Main script
├── generate_testing_files.py   # Script to generate test files
├── README.md                   # Documentation
└── LICENSE                     # License (MIT)
```
Prebuilt executables for Windows, Linux and macOS are available in the [Releases](../../releases) section.

---

## License

This project is licensed under the [MIT License](LICENSE).


Copyright (c) 2025 Cypher Grignote


