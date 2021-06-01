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



# Imports / Modules
import winapps
import sqlite3
import requests
import re
from urllib.request import urlopen
import subprocess as sp
import os


class Pyget():
	# Intial / Intialization Function
	def __init__(self):
		self.conn = sqlite3.connect("databases\\apps.db")
		self.cur = self.conn.cursor()


	# Help commands
	def help_(self):
		print("\n-- `pyget install`: For installing a new app")
		print("-- `pyget uninstall`: For uninstalling a app")
		print("-- `pyget list`: For listing all of the installed apps")
		print("-- `pyget listsearch`: Search for an already installed program in your PC\n")
		print("-- `pyget add`: Add a new app to your app library (the download URL of the app should be dynamic i.e. which can start the download by visting that link\n--  rather than clicking on a button or which requires user input. If it requires user input or the link is not applicable the application will\n--  launch a Procedural install method.)")
		print("\n-- `pyget remove`: Remove an app from your app library")
		print("-- `pyget myapps`: For listing all of the apps in your app library")
		print("-- `pyget downloads`: List all of the files in your downloads folder\n")


	# List all the already installed system apps
	def pyget_list(self):
		list_apps = []

		for item in winapps.list_installed():
			list_apps.append(item)

		return list_apps


	# Search for an already installed app on your PC
	def search_installed_apps(self):
		search = str(input("\nWhat would you like to search from your installed apps: "))
		for i in self.pyget_list():
			if search in i.name.lower():
				print("Name:", i.name)
				print("Version:", i.version)
				print("App Location:", i.install_location)
				print("Date Installed:", i.install_date)
				print("Publisher:", i.publisher, "\n")


	# Uninstall an app from your system
	def uninstall_app(self):
		search = str(input("\nWhich would you like to uninstall from your system: "))
		for i in self.pyget_list():
			if search in i.name.lower():
				print("Name:", i.name)
				print("Version:", i.version)
				print("App Location:", i.install_location)
				print("Date Installed:", i.install_date)
				print("Publisher:", i.publisher, "\n")

				yn = str(input("Are You Sure You Want To Uninstall This App [Y/N]: ")).lower()
				if yn == "y":
					print("Uninstalling...")
					os.system(f"{i.uninstall_string}")
					print("Success! Your app was deleted from your PC")
				else:
					print("Declined\n")


	# Helper function for f(add_app), f(data_entry)
	def create_table(self):
		self.cur.execute("CREATE TABLE IF NOT EXISTS AvailableApps (Name TEXT, URL TEXT)")


	# Helper function for f(add_app)
	def data_entry(self, name, url):
		self.cur.execute("""INSERT INTO AvailableApps(Name, URL) VALUES(?, ?)""", (name, url))
		self.conn.commit()


	# Add an app to the app library
	def add_app(self):
		name = str(input("The Name Of The App By Which You Want To Access It (Make it memorable): ")).lower()
		url = str(input("URL of The App: ")).lower()
		regex = "((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)"
		self.create_table()
		self.data_entry(name, url)
		

	# Install an app by opening the URL provided in the database fetched by name
	def install_app(self):
		name = str(input("The Name of the App you want to download from your app library: ")).lower()
		f_name = str(input("What would you name your file: "))
		self.cur.execute("""SELECT * FROM AvailableApps WHERE Name=?""", (name, ))
		for i in self.cur.fetchall():
			url = i[-1]

		filename = "downloads\\" + f_name

		def download(url, dst_file):
			content = urlopen(url).read()
			outfile = open(dst_file, "wb")
			outfile.write(content)
			outfile.close()

		def install(prog):
			process = sp.Popen(prog, shell=True)
			process.wait()

		def main():
			download(url, filename)
			install(filename)

		try:
			print("Installing...")
			main()
			print("Success")
		except:
			print("Failure!")
			print("\nThis type of file/URL is not applicable with our application so will be launching the Procedural install.")
			os.system(f"start {url}")
			print("Success!")


	# List all of the apps in app library
	def lib_apps(self):
		self.cur.execute("SELECT * FROM AvailableApps")
		for i in self.cur.fetchall():
			print("Name:", i[0].capitalize(), "\tURL:", i[-1])


	# Remove an app from app library
	def remove_app(self):
		search = str(input("\nWhat app would you like to delete from your app library: ")).lower()
		yn = str(input("Are you sure you want to delete this app from your app library[Y/N]: ")).lower()
		if yn == "y":
			self.cur.execute("""DELETE FROM AvailableApps WHERE Name=?""", (search, ))
			print("Success! Your app was deleted from your app library")
		else:
			print("Declined\n")


	# List all the files in downloads folder
	def list_downloads(self):
		print()
		for i in os.walk("downloads"):
			if i[-1] != []:
				for j in i[-1]:
					print(f"-- {j}")
			else:
				print("No Files Present in downloads!")
