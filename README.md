# Pyget


![version 0.28](https://img.shields.io/badge/version-0.28-green.svg)
![python 2.7.2](https://img.shields.io/badge/python-2.7.2-yellow.svg)
![dependencies progressbar](https://img.shields.io/badge/dependencies-progressbar-green.svg)
![license GPLv2](https://img.shields.io/badge/license-GPLv2-green.svg)
![platform linux](https://img.shields.io/badge/platform-linux-green.svg)

Contents:

1. [About Pyget](#about-pyget)
2. [Installation](#installation)
3. [Basic Usage](#basic-usage)
4. [Advanced Usage](#advanced-usage)
5. [System Requirements](#system-requirements)

## About PyGet:

Pyget is a low-level clone of Microsoft's WinGet / A CLI Download Manager
Pyget can perform many fucntions, for example:

-- `pyget install`: For installing a new app
-- `pyget uninstall`: For uninstalling a app
-- `pyget list`: For listing all of the installed apps
-- `pyget listsearch`: Search for an already installed program in your PC

-- `pyget add`: Add a new app to your app library (the download URL of the app should be dynamic i.e. which can start the download by visting that link
--  rather than clicking on a button or which requires user input. If it requires user input or the link is not applicable the application will
--  launch a Procedural install method.)

-- `pyget remove`: Remove an app from your app library
-- `pyget myapps`: For listing all of the apps in your app library
-- `pyget downloads`: List all of the files in your downloads folder

## Installation:

PyGet requires a few dependencies that you can install in the using the `install_requirements` function slated inside `pyget.py`

Dependencies:
    Getting System Apps: Winapps
    Databases: SQlite3
    Lanaguage Scraping: Regex
    Web: requests, urllib
    

Main program installation:

To install PyGet, `git clone placeholder` in your desired
installation directory (~/git/pyget is recommended).  Ensure that pyget.py is 
executable (as user, chmod +x pyget.py) and then symlink pyget.py to /usr/bin/pyget 
for convenience.  If the last step is not followed, you will have to cd into the folder
containing pyget.py and run './pyget.py' that way. 

## Basic usage:

Defaults:
Most users will find the default behavior of PyGet to be just fine for everyday
use.  Default behavior means prompting via the command prompt.  This is the method that 
has seen the most extensive testing.  To run PyGet with the default settings, cd 
into the directory where you have installed PyGet (most likely ~/Pyget), ensure
that the filename "pyget.py" is executable, and execute
```python pyget.py```.  Follow the prompts and enjoy painless downloading.

## System Requirements:

Windows 7+, Older widnows versions are not tested or supported on this program
Python 3.6+ Older python versions are not tested or supported on this program

##### Support for Linux and Mac
We are planning to release that, SOON.

# Thanks for Checking In! ❤