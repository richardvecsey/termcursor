[![Generic badge](https://img.shields.io/badge/Version-1.0.0-blue)](https://shields.io/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/termcursor)
![GitHub](https://img.shields.io/github/license/richardvecsey/termcursor)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/richardvecsey/termcursor/main)
![PyPI - Status](https://img.shields.io/pypi/status/termcursor)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/termcursor)
[![Downloads](https://pepy.tech/badge/termcursor)](https://pepy.tech/project/termcursor)
![PyPI - Downloads](https://img.shields.io/pypi/dm/termcursor)

# termcursor

Hiding or showing the console cursor on Windows and Unix platforms with the Python Standard Library only

## Quickstart

### Requirements

This module use Python Standard Library only. Python version should be higher than *3.10*

### Install

```
pip install termcursor
```

### How to Use

This code works as module not a script.

#### Module level import

```
import termcursor

# hiding the console cursor
termcursor.hidecursor()

# showing the console cursor
termcursor.showcursor()
```

#### Function level import

```
from termcursor import hidecursor, showcursor

# hiding the console cursor
hidecursor()

# showing the console cursor
showcursor()
```

#### Help

```
import termcursor

help(termcursor)
```

### Examples

#### Module level import

Example is available in the [example.py](https://github.com/richardvecsey/termcursor/blob/main/example.py)

#### Function level import

Example is available in the [example2.py](https://github.com/richardvecsey/termcursor/blob/main/example2.py)

## License

The content of this repository is licensed under *MIT license*. For more details, check [LICENSE](https://github.com/richardvecsey/termcursor/blob/main/LICENSE)
