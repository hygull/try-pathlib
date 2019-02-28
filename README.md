# Python's pathlib - usage examples

This documenation presents basic usage examples of Python's pathlib library. Before trying examples in this page make sure to check your Python version by reading the below note or [visit here](https://pypi.org/project/pathlib/?fbclid=IwAR0-Jk14-IkTLCNldiHXvv5HAzhE_C71YDMdv9vmfT0QtlILYZku_7gLKSM) to check.


![Pathlib-inheritance](./images/pathlib-inheritance.png)

## Note

+ Python **3.2** or later is recommended, but pathlib is also usable with Python **2.7** and **2.6**.

+ In Python **3.4**, pathlib is now part of the standard library. For Python **3.3** and earlier, `easy_install pathlib` or `pip install pathlib` should do the trick.


&raquo; Mean to say

| Python 2.6 - Python3.3 | >= Python 3.4 |
| --- | --- |
| pip install pathlib | No installation is required just try as it the part of standard library |
| easy_install pathlib ||

> Mine is Python **3.7.2** and I am trying it on **MAC OS Mojave**.


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

#### &raquo; Listing out directories and files of current directory separately

```python 
>>> from pathlib import Path
>>> 
>>> root = Path(".")
>>> root
PosixPath('.')
>>> 
```

```python
>>> directories = [dir_content for dir_content in root.iterdir() if dir_content.is_dir()]
>>> directories
[PosixPath('go'), PosixPath('python'), PosixPath('js'), PosixPath('cpp'), PosixPath('c')]
>>>
```

```python 
>>> files = [dir_content for dir_content in root.iterdir() if dir_content.is_file()]
>>> files
[PosixPath('doc.md'), PosixPath('main.md')]
>>> 

```

#### &raquo; Getting absoute path of `root` directory

```python
>>> root.absolute()
PosixPath('/Users/hygull/Projects/Python3/try-pathlib/root')
>>> 

```

#### &raquo; Getting `home` directory's absolute path

```python
>>> root.home()
PosixPath('/Users/hygull')

```

#### &raquo; Listing out all python files present in any of the directories availble under current directory

```python
>>> list(root.glob("**/*.py"))
[PosixPath('go/docs/loop.py'), PosixPath('python/hello.py'), PosixPath('js/try/examples/dict-example.py')]
>>> 


```


#### &raquo; Navigating to `root/python/examples/go` and lisiting out its content(s).

+ Brief look using terminal.

```bash
Rishikeshs-MacBook-Air:root hygull$ 
Rishikeshs-MacBook-Air:root hygull$ ls python/examples/
go
Rishikeshs-MacBook-Air:root hygull$ ls python/examples/go/
slice.go
Rishikeshs-MacBook-Air:root hygull$ cat python/examples/go/slice.go 
package main 

import "fmt"

func main() {
	a := []int{12, 5, 6, 8}
	fmt.Print(a)
}

```

+ Prgramatically navigating to `root/python/examples/go` by verifying the navigated location's existence.

```python
>>> root
PosixPath('.')
>>> 
>>> python = root / "python"
>>> python
PosixPath('python')
>>> 
>>> python.exists()
True
>>> 
>>> examples = python / "examples"
>>> examples
PosixPath('python/examples')
>>> 
>>> examples.exists()
True
>>> 
>>> go = examples / "go"
>>> go
PosixPath('python/examples/go')
>>> 
>>> go.exists()
True
>>> 

```

+ Lisiting out content(s) of **go** directory.

```python
>>> list(go.iterdir())
[PosixPath('python/examples/go/slice.go')]
>>> 
```

+ Single line to navigate to go directory - `go = root / "python" / "examples" / "go"`

```python
>>> examples = root / "examples"
>>> examples.exists()
False
>>> 
>>> examples = root / "python" / "examples"
>>> examples.exists()
True
>>> 
```

```python
>>> go = root / "python" / "examples" / "go"
>>> go.exists()
True
>>> 

```

#### &raquo; Getting URI

```python
>>> python
PosixPath('python')
>>> 
```

```python
>>> python.as_uri()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/pathlib.py", line 714, in as_uri
    raise ValueError("relative path can't be expressed as a file URI")
ValueError: relative path can't be expressed as a file URI
>>> 
```

```python
>>> python = python.resolve()
>>> python
PosixPath('/Users/hygull/Projects/Python3/try-pathlib/root/python')
>>> 
```

```python
>>> python.as_uri()
'file:///Users/hygull/Projects/Python3/try-pathlib/root/python'
>>> 

```


#### &raquo; Printing parent directories and checking their existence

```python
>>> go = go.resolve()
>>> go.as_uri()
'file:///Users/hygull/Projects/Python3/try-pathlib/root/python/examples/go'
>>>

```

```python
>>> examples = go.parent
>>> examples
PosixPath('/Users/hygull/Projects/Python3/try-pathlib/root/python/examples')
>>> 
>>> examples.exists()
True
>>> 

```

```python
>>> python = examples.parent
>>> python
PosixPath('/Users/hygull/Projects/Python3/try-pathlib/root/python')
>>> 
>>> python.exists()
True
>>> 
```




## References

+ https://python.readthedocs.io/en/stable/library/pathlib.html

+ https://pypi.org/project/pathlib/?fbclid=IwAR0-Jk14-IkTLCNldiHXvv5HAzhE_C71YDMdv9vmfT0QtlILYZku_7gLKSM

+ https://realpython.com/python-pathlib/
