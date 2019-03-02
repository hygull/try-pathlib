"""
	{
		"date_created": "2 march 2019, Sat",
		"aim": "Creating files with contents (few lines)",
		"created_by": "Rishikesh Agrawani",
		"description": "First the code will check if there is a directory 
						named `created_files` in the current working
						if it exists, it will create files inside that
						it it doesn't exist, create the folder first and then create file
						named `message.txt` inside that"

	}
"""

from pathlib import Path 


cwd = Path(".")
created_files_dir = cwd / "created_files"

if not created_files_dir.exists():
	created_files_dir.mkdir()

file = created_files_dir / "message.txt"

lines = [
	"It is better to learn programming for solving complex problems.",
	"Python, Java, Go, C, JavaScript, Ruby, PHP are popular.",
	"So finally, we all are in a right place"
]

file.write_text('\n'.join(lines))
