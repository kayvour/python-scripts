A simple Python script that merges multiple PDF files in a folder into a single PDF. It sorts files alphabetically, merges them, and saves the output in the current working folder.

Usage:
Run the script with:
python pdf_merger.py [output_filename]

-[output_filename] (optional): Name of the final merged PDF file (e.g., final.pdf). If not provided, defaults to combined.pdf.

PDF Selection and Merge Order:
-All files with .pdf extension in the current directory will be included.
-Files are merged in alphabetical order by filename.

Output Location:
-The merged PDF file is saved in the same directory as the script.
-If a file with the same name already exists, it will be overwritten.

Error Handling:
-Ignores non-PDF files.
-Warns and exits if no PDF files are found.
-Catches and prints exceptions during merging or writing.

