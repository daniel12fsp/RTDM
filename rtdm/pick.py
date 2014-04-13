import subprocess
import os
import random

def list_random_files(path_dir, size):
	command = "ls " + path_dir +"*.html |shuf -n "+str(size)
	return execute_bash(command).splitlines()

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
