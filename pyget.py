"""

Pyget:
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


# Basic Usage: ~/Pyget> python pyget.py
# Warning: If you received this program from any source other than
github, please check the source code! You may have
downloaded a file with malicious code injected. 
# App Version: 1.75
# System Requiremets: Windows 7+, Older widnows versions are not tested or supported on this program
# Python 3.6+ Older python versions are not tested or supported on this program
# Dependencies: Urllib, Requests, Winapp, SQlite3, regex

# Support for Linux and Mac
We are planning to release that, SOON.

Confused?
Contact Me: 
Discord: ImCool#0631


# CREDITS- :)
Setup: Aryan Mishra
Backend/Databases: Aryan Mishra
Frontend/UI: Aryan Mishra
Developing: Aryan Mishra
Testing: Aryan Mishta
Deploying: Aryan Mishra

"""


import os

def install_requirements():
	os.system("pip install -r requirements.txt")


# Use this DEBUG function to install all of the requiremnts/modules required for this to work(BE SURE TO NOT PLACE THIS AFTER THE IMPORTS)
# install_requirements()


import main


# RUN FUNCTION (TO TURN THE APP ON / OFF)\

def run():
	# Intialization the App
	pyget = main.Pyget()

	# App Loop
	while True:
		cmd = input("\nPlease input a command ('pyget' for help) [Q for exit]: ").lower()

		if cmd == "q":
			exit() 

		# Help
		elif cmd == "pyget":
			pyget.help_()

		# Listing apps
		elif cmd == "pyget list":
			print("\nLoading your apps this may take a while, depending on your PC...")
			for i in pyget.pyget_list():
				print("--", i.name)
			print()

		# Searching apps
		elif cmd == "pyget listsearch":
			pyget.search_installed_apps()

		# Uninstalling apps
		elif cmd == "pyget uninstall":
			pyget.uninstall_app()

		# Adding app to library
		elif cmd == "pyget add":
			pyget.add_app()

		# Installing app from library
		elif cmd == "pyget install":
			pyget.install_app()

		# Listing library apps
		elif cmd == "pyget myapps":
			pyget.lib_apps()

		# Removing app from library
		elif cmd == "pyget remove":
			pyget.remove_app()

		# Listing all downloads in downloads folder
		elif cmd == "pyget downloads":
			pyget.list_downloads()

		# Silent-Error-Out if not a command
		else:
			print("Unrecognized Command")


"""
Running the app. 
Comment out if want to turn the application OF. Uncomment if want to turn application ON.
"""

run()
