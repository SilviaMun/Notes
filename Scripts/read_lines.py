import os

# Define the directory path where your text files are located
directory_path = 'F:\Data-Leaks'

# Define the string to search for
search_string = 'string'

# Initialize a list to store matching file paths
matching_files = []

# Recursively search for the string in all files within the directory
for root, _, files in os.walk(directory_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                lines = file.readlines()  # Read all lines in the file
                for line_number, line in enumerate(lines, start=1):
                    if search_string in line:
                        matching_files.append((file_path, line_number, line.strip()))
                        print(f"Found '{search_string}' in: {file_path}, Line {line_number}: {line.strip()}")
        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")

# Print the list of files, line numbers, and lines that contain the search string
if matching_files:
    print(f"Found '{search_string}' in the following files:")
    for file_path, line_number, line_content in matching_files:
        print(f"File: {file_path}, Line {line_number}: {line_content}")
else:
    print(f"'{search_string}' was not found in any of the files.")

# Add input() to keep the console window open after execution (optional)
input("Press Enter to exit...")
