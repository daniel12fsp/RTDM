#!/usr/bin/python3
# -*- coding: utf8 -*-

import re

def get_links(file_name):
	
	myfile = open(file_name, "r")
	files_names = myfile.readlines()
	file_tree1 = files_names[0][:-1]
	file_tree2 = files_names[1][:-1]
	path_dir = files_names[2][:-1]
	return file_tree1, file_tree2, path_dir


def get_path_dir_from_files(name_file):
	try:
		return re.findall("(.*)/.*?$", name_file)[0]+"/"
	except:
		print("Provavelmente a variavel 'name_file' nao esta no formato unix de path(/)")
		return None


def get_name_from_files(file1, file2, extension):
	return get_name_file(file1) + "_" + get_name_file(file2) + extension


def get_name_file(name_file):
	try:
		return re.findall(".*/(.*)\..*$",name_file)[0]
	except:
		print("Provavelmente a variavel 'name_file' nao esta no formato unix de path(/)")
		return ''



def create_file_dir_mod(path_dir, file1, file2, extension):
	name_file =  path_dir + get_name_from_files(file1, file2, extension)
	return open(name_file, "w")

def create_file_dir_default(file1, file2, extension):
	"""
		O diretorio default eh o diretorio do primeiro arquivo
	"""
	return create_file_dir_mod(get_path_dir_from_files(file1), file1, file2, extension)

def get_path_file(file1, file2, extension):
	return get_path_dir_from_files(file1) + get_name_from_files(file1, file2, extension)

