A simple Python script that organizes files in a folder into subfolders based on their file extensions. For example, `.jpg` files are moved to a `jpg_files/` folder, `.pdf` to `pdf_files/`, and so on.

Usage
Run the script with:
python folder_organizer.py

You will be prompted to enter the path to the folder you want to organize.

How It Works
-All files in the specified folder are scanned.
-Each file is moved into a subfolder named `<extension>_files/`.
  -Example: `photo.jpg` → `jpg_files/photo.jpg`
-Subfolders are created automatically if they don’t exist.

Output Location
-Files are moved within the same folder you specify.
-Original files are no longer in the root; they reside in their new extension-based folders.
-Existing files with the same name in the destination folder will be overwritten.

Error Handling
-Warns if the provided path doesn’t exist.
-Ignores folders and only processes files.
-Automatically skips system files like `.DS_Store` or hidden files if needed (can be modified).
