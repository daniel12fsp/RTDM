#!/usr/bin/python3
# -*- coding: utf8 -*-

import re

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
		return None



def create_file_dir_mod(path_dir, file1, file2, extension):
	name_file =  path_dir + get_name_from_files(file1, file2, extension)
	return open(name_file, "w")

def create_file_dir_default(file1, file2, extension):
	"""
		O diretorio default eh o diretorio do primeiro arquivo
	"""
	return create_file_dir_mod(get_path_dir_from_files(file1), file1, file2, extension)

