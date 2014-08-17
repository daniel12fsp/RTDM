#!/usr/bin/python3
# -*- coding: utf8 -*-

import fnmatch
import os
import re
import sys
import random
import glob

def list_random_pages(path_dir):

	pages = glob.glob(path_dir + "*.html*")
	random.shuffle(pages)
	return pages


def list_sorted_pages(path_dir):

	pages = glob.glob(path_dir + "*.html*")
	return sorted(pages)

def take_one_file(diretory, extension):
	"""
		Retorna uma string com nome de algum arquivo da extensão de parametro no mesmo diretorio	
	"""
	try:
		return diretory+ take_files_same_extension(diretory, extension)[0]
	except:
		return None

def take_files_same_extension(diretory, extension):
	"""
		Retorna uma lista com os nomes dos arquivos de mesma extensão no mesmo diretorio
	"""

	try:
		return fnmatch.filter(os.listdir(diretory), "*"+extension)
	except:
		return None




def get_path():
	"""
		Pega as informações de um arquivo que serve de entrada ou do terminal
	"""
	filename = os.path.dirname(os.path.realpath(__file__)) + "/../links_rtdm.txt"
	path_file_folders = os.path.dirname(os.path.realpath(__file__)) + "/../links_rtdm.txt"
	file_folders = open(path_file_folders, "r")
	path_logs = file_folders.readline().strip()
	folders = file_folders.readlines()

	return path_logs, folders


def get_path_dir_from_file(name_file):
	"""
		Retorna o diretorio do arquivo do paramentro, em caso de erro envia None.
		Obs.:
		Se houver problemas poderá ser algo do path(Windows e Mac tem padroes diferentes), 
		verifique(Eu só uso Linux-Like)!
	"""
	try:
		return re.findall("(.*)/.*?$", name_file)[0]+"/"
	except:
		print("Provavelmente a variavel 'name_file' nao esta no formato unix de path(/)")
		return None


def get_name_from_files(file1, file2, extension):
	"""
		Retorna nome_do_file1 + nome_do_file2 + extensão do arquivo
	"""
	
	return get_name_file(file1) + "_" + get_name_file(file2) + extension


def get_name_file(name_file):
	"""
		Retorna o nome do arquivo. retira-se a extensão
		Ex.:
		nome do arquivo = "teste.pyc"
		get_name_file(teste.pys)	 == "teste"
	"""
	try:
		return re.findall(".*/(.*)\..*$",name_file)[0]
	except:
		print("Provavelmente a variavel 'name_file' nao esta no formato unix de path(/)")
		return ''


def get_name_file_with_extension(name_file):
	"""
		Retorna o nome do arquivo. retira-se a extensão
		Ex.:
		nome do arquivo = "teste.pyc"
		get_name_file(teste.pys)	 == "teste"
	"""
	try:
		return re.findall(".*/(.*)",name_file)[0]
	except:
		print("Provavelmente a variavel 'name_file' nao esta no formato unix de path(/)")
		return ''

def create_file(filename, extension):
	return  get_path_dir_from_file(filename) + get_name_file(filename) + extension

def create_file_dir_mod(path_dir, file1, file2, extension):
	"""
		Cria um arquivo conforme o diretorio do paramentro + nome_do_file1 + nome_do_file2 + extensão do arquivo
	"""

	name_file =  path_dir + get_name_from_files(file1, file2, extension)
	return open(name_file, "w")

def create_file_dir_default(file1, file2, extension):
	"""	
		Cria um arquivo conforme o diretorio default(eh o diretorio do primeiro arquivo)
	"""
	return create_file_dir_mod(get_path_dir_from_file(file1), file1, file2, extension)

def get_path_file(file1, file2, extension):
	"""
		Retorna o path formado pelo diretorio do file1 + nome_do_file1 + nome_do_file2 + extensão do arquivo
	"""
	return get_path_dir_from_file(file1) + get_name_from_files(file1, file2, extension)

