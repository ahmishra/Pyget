# Pyget


![python37](https://img.shields.io/badge/python-3.7-red)
![version1.7](https://img.shields.io/badge/app-v1.7-blue)
![platform_windpws](https://img.shields.io/badge/platform-windows-green)

Contents:

1. [About Pyget](#about-pyget)
2. [Installation](#installation)
3. [Basic Usage](#basic-usage)
4. [Basic Usage](#advanced-usage)
5. [System Requirements](#system-requirements)

## About PyGet:

Pyget is a low-level clone of Microsoft's WinGet / A CLI Download Manager
Pyget can perform many fucntions, for example:

- `pyget install`: For installing a new app
- `pyget uninstall`: For uninstalling a app
- `pyget list`: For listing all of the installed apps
- `pyget listsearch`: Search for an already installed program in your PC

- `pyget add`: Add a new app to your app library (the download URL of the app should be dynamic i.e. which can start the download by visting that linkrather than clicking on a button or which requires user input. If it requires user input or the link is not applicable the application will launch a Procedural install method.)

- `pyget remove`: Remove an app from your app library
- `pyget myapps`: For listing all of the apps in your app library
- `pyget downloads`: List all of the files in your downloads folder

## Installation:

PyGet requires a few dependencies that you can install in the using the `install_requirements` function slated inside `pyget.py`

Dependencies:
- Getting System Apps: Winapps
- Databases: SQlite3
- Lanaguage Scraping: Regex
- Web: requests, urllib
- Download Stuff: youtube_dl
    

<b>Main program installation:</b>

To install PyGet, `git clone https://github.com/ahmishra/Pyget.git` in your desired
installation directory (~/Pyget is recommended).  Ensure that pyget.py is 
executable next, you will have to cd into the folder
containing pyget.py and run ```python pyget.py``` that way. 

## Advanced usage:

Defaults:
Most users will find the default behavior of PyGet to be overly complicated for everyday
use.  Default behavior means prompting via the command prompt.  This is the method that 
has seen the testing.  To run PyGet with the default settings, cd 
into the directory where you have installed PyGet (most likely ~/Pyget), ensure
that the filename "pyget.py" is executable, and uncomment the `run_cli()` function and then execute
```python pyget.py```.  Follow the prompts and enjoy painless downloading.

## Basic usage:

Defaults:
Most users will find the default behavior of PyGet to be just fine for everyday
use.  Default behavior means prompting via the command prompt.  This is the method that 
has seen the testing.  To run PyGet with the basic settings, cd 
into the directory where you have installed PyGet (most likely ~/Pyget), ensure
that the filename "pyget.py" is executable, and uncomment the `run_gui()` function and then execute
```python pyget.py```.  Then go to the port it prompted back to you (i.e: `localhost:8000` most probably)


## System Requirements:

Windows 7+, Older widnows versions are not tested or supported on this program
Python 3.6+ Older python versions are not tested or supported on this program

<b>Support for Linux and Mac</b>
We are planning to release that, SOON.

## Credits :)
- Setup: Aryan Mishra
- Backend/Databases: Aryan Mishra
- Frontend/UI: Aryan Mishra
- Developing: Aryan Mishra
- Testing: Aryan Mishta
- Deploying: Aryan Mishra

<small><b>Warning: If you received this program from any source other than
github, please check the source code! You may have
downloaded a file with malicious code injected.<b></small>

<br>

# Thanks for Checking In!! ❤

<br>
