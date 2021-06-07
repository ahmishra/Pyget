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
# App Version: 1.71
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


from flask import Flask, render_template, url_for, redirect, request, flash
import winapps
from urllib.request import urlopen
import subprocess as sp
import os
from datetime import date
import random


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class Helper:
	def write_file(self, url, dst_file):
		content = urlopen(url).read()
		outfile = open(dst_file, "wb")
		outfile.write(content)
		outfile.close()

	def install_file(self, program):
		process = sp.Popen(program, shell=True)
		process.wait()

	def download(self, url, filename):
		self.write_file(url, filename)
		self.install_file(filename)


helper = Helper()

# Home Page / Download App Page
@app.route("/", methods=["POST", "GET"])
def home():
	if request.method == "POST":
		url = request.form.get("url")
		filename = f"""Pyget {date.today().strftime("%b-%d-%Y")}-{random.randint(0, 10000)}.{url[-3:]}"""
		try:
			helper.download(url, filename)
			flash("Success!", "info")
			return redirect(url_for("installed"))

		except ValueError as e:
			flash(f"Invalid URL- {str(e).capitalize()}", "danger")
			return redirect(url_for("home"))

	return render_template("home.html")



# Prompt When A App Was Download / Installed
@app.route("/installed")
def installed():
	return render_template("installed.html")


# Web Page To List All Of The Installed PC Apps
@app.route("/installd_apps")
def installed_apps():
	return render_template("installed-apps.html", apps=winapps.list_installed())
