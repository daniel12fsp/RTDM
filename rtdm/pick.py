import subprocess
import os
import random

def list_random_files(path_dir, size):
	return ['/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/ColetaUFAM/ColetaNova/notebooks/submarino_notebook/115401269.html', '/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/ColetaUFAM/ColetaNova/notebooks/submarino_notebook/111235494.html']
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
