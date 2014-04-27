import subprocess
import os
import random
import glob

def list_random_pages(path_dir):
	pages = glob.glob(path_dir + "*.html")
	random.shuffle(pages)
	return pages

def list_size_order_files():
	#errado
	"""
	files = []
	for one in tmp:
		split = one.split()
		length = int(split[4])
		name = split[8]
		files.append((length, name))ommand = "ls " + path_dir +"*.html -lS"
	return None
	"""

def execute_bash(command):
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
	(output, err) = proc.communicate()
	return output
