"""
	{
		"date_created": "4 march 2019, Mon",
		"aim": "Creating directories whose names are mentioned in a text file",
		"created_by": "Rishikesh Agrawani",
		"description": "First program will check if directory named `created_directories` exists or not
					   If it does exist it creates that and after that it reads a text file 
					   `../docs/texts/directory_names.txt` to read list of directory names and create 
					   those directories inside `created_directories` directory.
					   
					   Here I have not coded for validations etc. so assume that I have valid names in 
					   the text file (check it)"
	}
"""

from pathlib import Path 


cwd = Path(".").resolve()
created_directories_dir_path = cwd / "created_directories"

if not created_directories_dir_path.exists():
	created_directories_dir_path.mkdir()
	print("Directory successfully created")

# Getting path of the file to be read
directory_names_file_path = cwd.parent / "docs" / "texts" / "directory_names.txt"

print(directory_names_file_path) 
print(directory_names_file_path.exists())
print(directory_names_file_path.is_file())

directory_names = directory_names_file_path.read_text().split('\n')

# ['Gayle', 'Sachin', 'Sehwag', 'Garry', 'Dhoni', 'Ricky', 'Adam', 'Ken', 'Dennis', 'Wes']
print(directory_names) 

for directory_name in directory_names:
	directory_path = created_directories_dir_path / directory_name.strip()
	directory_path.mkdir()
	print("Created", directory_path)

# Storing absolute path of all the newly created directories
new_dir_paths = [str(new_dir_path) for new_dir_path in created_directories_dir_path.iterdir() if new_dir_path.is_dir()]
print(new_dir_paths)
# ['/Users/hygull/Projects/Python3/try-pathlib/src/created_directories/Sehwag', '/Users/hygull/Projects/Python3/try-pathlib/src/created_directories/Dennis', '/Users/hygull/Projects/Python3/try-pathlib/src/created_directories/Dhoni', '/Users/hygull/Projects/Python3/try-pathlib/src/created_directories/Ricky', '/Users/hygull/Projects/Python3/try-pathlib/src/created_directories/Garry', '/Users/hygull/Projects/Python3/try-pathlib/src/created_directories/Gayle', '/Users/hygull/Projects/Python3/try-pathlib/src/created_directories/Wes', '/Users/hygull/Projects/Python3/try-pathlib/src/created_directories/Sachin', '/Users/hygull/Projects/Python3/try-pathlib/src/created_directories/Ken', '/Users/hygull/Projects/Python3/try-pathlib/src/created_directories/Adam']