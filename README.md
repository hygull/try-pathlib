# Python's pathlib - usage examples

This documenation presents basic usage examples of Python's pathlib library. Before trying examples in this page make sure to check your Python version by reading the below note or [visit here](https://pypi.org/project/pathlib/?fbclid=IwAR0-Jk14-IkTLCNldiHXvv5HAzhE_C71YDMdv9vmfT0QtlILYZku_7gLKSM) to check, mine is Python3.7.2.

![Pathlib-inheritance](./images/pathlib-inheritance.png)

## Note

+ Python 3.2 or later is recommended, but pathlib is also usable with Python 2.7 and 2.6.

+ In Python 3.4, pathlib is now part of the standard library. For Python 3.3 and earlier, `easy_install pathlib` or `pip install pathlib` should do the trick.


## Directory structure of working directory

We will be working on [root](./root) directory. This directory has the following structure.

```bash
Rishikeshs-MacBook-Air:try-pathlib hygull$ pwd
/Users/hygull/Projects/Python3/try-pathlib
Rishikeshs-MacBook-Air:try-pathlib hygull$ tree root/

```

```bash
root/
├── c
│   └── examples
│       ├── c-main.md
│       └── hello.c
├── cpp
│   ├── docs
│   │   └── notes.md
│   └── hello.cpp
├── doc.md
├── go
│   ├── docs
│   │   ├── links.md
│   │   └── loop.py
│   ├── hello.go
│   └── images
│       ├── go-slices-usage-and-internals_slice-2.png
│       ├── go.jpeg
│       ├── rishikesh.jpeg
│       └── rishikesh.png
├── js
│   ├── hello.js
│   └── try
│       └── examples
│           └── dict-example.py
├── main.md
└── python
    ├── examples
    │   └── go
    │       └── slice.go
    ├── hello.py
    └── images
        ├── python.jpeg
        └── rishikesh.webp

```

## Getting started

Now, let's move/navigate to **root** directory which is to be assumed as the working directory in this documentation.

```bash
Rishikeshs-MacBook-Air:try-pathlib hygull$ cd root/
Rishikeshs-MacBook-Air:root hygull$ ls
c	cpp	doc.md	go	js	main.md	python
Rishikeshs-MacBook-Air:root hygull$

```

```bash 
Rishikeshs-MacBook-Air:root hygull$ python3
Python 3.7.2 (default, Jan 13 2019, 12:50:01) 
[Clang 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

We are done, let's start.

### Example 1

```python 
>>> from pathlib import Path
>>> 
>>> root = Path(".")
>>> root
PosixPath('.')
>>> 
>>> directories = [dir_content for dir_content in root.iterdir() if dir_content.is_dir()]
>>> directories
[PosixPath('go'), PosixPath('python'), PosixPath('js'), PosixPath('cpp'), PosixPath('c')]
>>> 
>>> files = [dir_content for dir_content in root.iterdir() if dir_content.is_file()]
>>> files
[PosixPath('doc.md'), PosixPath('main.md')]
>>> 

```







## References

+ https://python.readthedocs.io/en/stable/library/pathlib.html

+ https://pypi.org/project/pathlib/?fbclid=IwAR0-Jk14-IkTLCNldiHXvv5HAzhE_C71YDMdv9vmfT0QtlILYZku_7gLKSM

+ https://realpython.com/python-pathlib/
