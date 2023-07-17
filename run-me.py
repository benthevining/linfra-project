#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ======================================================================================
#  __    ____  __  __  ____  ___
# (  )  (_  _)(  \/  )( ___)/ __)
#  )(__  _)(_  )    (  )__) \__ \
# (____)(____)(_/\/\_)(____)(___/
#
#  This file is part of the Limes open source library and is licensed under the terms of the GNU Public License.
#
#  Commercial licenses are available; contact the maintainers at ben.the.vining@gmail.com to inquire for details.
#
# ======================================================================================

"""
Usage: run-me.py

This script replaces the following placeholders in all of the files in this repository:

%PROJECT_NAME%
%PROJECT_DESCRIPTION%
%PROJECT_URL%
%AUTHOR_EMAIL%
%AUTHOR_GIVEN_NAME%
%AUTHOR_FAMILY_NAME%
%AUTHOR_GH_USERNAME%

This script will interactively ask you for each of these values.

Finally, the script deletes itself and the readme in this directory.

TODO:
- license header text
- package.json: keywords, assets
"""

import os
import pathlib

REPO_ROOT = pathlib.Path (os.path.dirname (os.path.realpath (__file__)))

ALL_FILES = []

for root, dirs, files in os.walk (REPO_ROOT, topdown=True):
	dirs[:]  = [d for d in dirs  if d not in ".git"]
	files[:] = [f for f in files if f not in " .DS_Store"]

	root = pathlib.Path (root)

	for file in files:
		ALL_FILES.append (root / file)

#

def replace_placeholder (placeholder, newValue):
	# all placeholder values should be unquoted
	newValue = newValue.strip ('\"').strip ('\'').strip (' ')

	for file in ALL_FILES:
		new_lines = []

		with open (file, "rt") as fin:
			for line in fin:
				new_lines.append (line.replace (placeholder, newValue))

		with open (file, "wt") as fout:
			fout.write (''.join (new_lines))


def ask_and_replace (placeholder, question):
	new_value = input (question)

	replace_placeholder (placeholder=placeholder,
						 newValue=new_value)

	return new_value

#

PROJ_NAME = ask_and_replace (placeholder="%PROJECT_NAME%",
							 question="Please enter the project name: ")

ask_and_replace (placeholder="%PROJECT_DESCRIPTION%",
				 question="Please enter a short project description: ")

ask_and_replace (placeholder="%PROJECT_URL%",
				 question="Please enter the project's homepage URL: ")

ask_and_replace (placeholder=r"%AUTHOR_EMAIL%",
				 question="Please enter the project author's email address: ")

ask_and_replace (placeholder=r"%AUTHOR_GH_USERNAME%",
				 question="Please enter the project author's GitHub username: ")

author_full_name = input ("Please enter the project author's full name (eg. 'Ben Vining'): ")

res = author_full_name.split (' ', 1)

replace_placeholder (placeholder=r"%AUTHOR_GIVEN_NAME%",
					 newValue=res[0])

replace_placeholder (placeholder=r"%AUTHOR_FAMILY_NAME%",
					 newValue=res[1])

#

FILES_TO_DELETE = [os.path.realpath (__file__), REPO_ROOT / "README.md"]

for file in FILES_TO_DELETE:
	os.remove (file)

#

print (f"Success! The {PROJ_NAME} project is now configured for basic development using linfra.")
print ("You should commit these changes to version control before beginning other development.")
