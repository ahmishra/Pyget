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

from __future__ import unicode_literals
from flask import Flask, render_template, url_for, redirect, request, flash
import winapps
from urllib.request import urlopen
import subprocess as sp
import os
from datetime import date
import random
import youtube_dl
import urllib
import shutil
import requests


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


	def video_download(self,  	link):
		try:
			if "youtube" in link.lower():
				ydl_opts = {'format': 'best'}
				with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				    ydl.download([link])
			else:
				urllib.request.urlretrieve(link, f'PygetVideo-{random.randint(0, 10000)}.mp4')
		except:
			return ValueError("Something went wrong")


	def image_download(self, link):
		filename = link.split("/")[-1]
		r = requests.get(link, stream = True)

		if r.status_code == 200:
		    r.raw.decode_content = True
		    with open(filename,'wb') as f:
		        shutil.copyfileobj(r.raw, f)
		else:
			return ValueError("Link Invalid")
		    



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

# Uninstall A App
@app.route("/uninstall_app/", methods=['GET', 'POST'])
def uninstall_app():
	if request.method == "POST":
		name = request.form.get("name")
		for i in winapps.list_installed():
			if name in i.name.lower():
				os.system(f"{i.uninstall_string}")
		return redirect(url_for('uninstalled'))

	return render_template("uninstall_app.html")



# Web Page To List All Of The Installed PC Apps
@app.route("/installed_apps")
def installed_apps():
	return render_template("installed-apps.html", apps=winapps.list_installed())




# Download Image
@app.route("/image_download", methods=["POST", "GET"])
def image_download():
	if request.method == "POST":
		image = request.form.get("image_url")
		try:
			helper.image_download(image)
			flash("Success!", "info")
		except:
			flash("Something Went Wrong, But We Dont Know What!", "danger")
			
		return redirect(url_for('downloaded'))

	return render_template("image_download.html")

# Video Download
@app.route("/video_download", methods=["POST", "GET"])
def video_download():
	if request.method == "POST":
		video = request.form.get("video_url")
		try:
			helper.video_download(video)
			flash("Success!", "info")
		except:
			flash("Something Went Wrong, But We Dont Know What!", "danger")
			
		return redirect(url_for('downloaded'))

	return render_template("video_download.html")




# Prompt When An App Was Download / Installed / Uninstalled
@app.route("/installed")
def installed():
	return render_template("installed.html")

@app.route("/uninstalled")
def uninstalled():
	return render_template("uninstalled.html")




# GET page after POST page to avoid resubmits
@app.route("/downloaded")
def downloaded():
	return render_template("downloaded.html")
