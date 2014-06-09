##!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function
import rtdm
import tree_lib as tree
import os
from mapping import generate_template
from identical_sub_trees import get_classe_equivalencia
import file
import xpath
import sys
import os
import gc

max_operation = float("inf") # +infinito
min_operation = 000

def file_file( file_log, file1, file2, file_general_xpath):
	"""
			Function: file_file
				Compara dois arquivos html
				retorna a similaridades dentre eles
	"""

	
	print("Criando arquivo de log - [Ok]", end="", file = file_log )
	print("\nT1:%s \nT2:%s" % (file1,file2), file = file_log )
	print("Carregando as arvores(arquivos para arvores)", end="", file = file_log )
	#Lembrado que tree1 e tree2 jah comeca do body!
	tree1, tree2 = tree.files_to_trees(file1, file2)
	print("[Ok]", file = file_log)

	print("Calculando a classe de equivalencia", end="", file = file_log )
	k = get_classe_equivalencia(tree1, tree2)
	print("len classe de equivalencia", len(k),file = file_general_xpath )
	print("[Ok]", file = file_log )

	print("Comecando a executar o RTDM!", end="", file = file_log )
	rtdm.prepareRTDM(k, file_log)
	operacoes, mape = rtdm.RTDM(tree1, tree2)

	print("[Ok]", file = file_log )

	if(min_operation <= operacoes and operacoes <= max_operation):
		print("Construcao do template", end="", file = file_log )
		file_regex = file.create_file_dir_mod(path_log, file1, file2, ".regex" )
		file_regex.write(generate_template(mape))
		file_regex.close()

	print("\nMinimo de operacoes necessarias para similiridade:\t>>> %d <<< " % (operacoes), file = file_log )

	print("Fim!", file = file_log)

	return operacoes, path_log + file.get_name_from_files(file1, file2, ".regex")

def generate_xpath_file_random(path_dir, quant_elem, file_erro):
	picks = file.list_random_pages(path_dir)
	group = 0
	path_general_xpath = path_test + "general_xpath.txt" 
	file_general_xpath = open(path_general_xpath, "w", 0)
	while(len(picks) >= 2):
		gc.collect()
		page2 = picks.pop(0)
		pages_cmp_valid = [page2]
		select_pages = [page2]
		group += 1
		lca = ""
		valid_page = 2
		while(len(picks) > 0):
			page1 = picks.pop(0)
			aux = page2
			file_log = file.create_file_dir_mod(path_log, page1, page2, ".log")
			try:
				operacoes, page2 = file_file(file_log, page1, page2, file_general_xpath )
			except:
				print("Erro:",page1, page2, file = file_erro)
				print(sys.exc_info()[0])
				break;
			if(min_operation <= operacoes and operacoes <= max_operation ):
				print(page1, file = file_general_xpath)
				print(page2, file = file_general_xpath)
				print( "Operacoes <%d>" % (operacoes), file = file_general_xpath)
				lca = xpath.create(file_log, page2, file_general_xpath)
				pages_cmp_valid.append(page1)
				valid_page += 1
			else:
				page2 = aux
			file_log.close()
			if(valid_page > quant_elem):
				break
		print("Resultado Final", file = file_general_xpath)
		print(pages_cmp_valid, file = file_general_xpath)
		print("\t\t>>>"+lca+"<<<", file = file_general_xpath)
		print("----------------", file = file_general_xpath)

	file_general_xpath.close()

def exec_rtdm(file_erro):
	"""
	Replace_choice
		1 - replace_no_no
		2 - replace_nos_t2
		3 - replace_mesma_quantidade_elementos 

	"""
	rtdm.replace_choice(3)
	generate_xpath_file_random(path_pages, 5, file_erro)

def prepare_vars(_path_pages, _path_test, _path_log):
	global path_pages
	global path_test
	global path_log
	path_pages = _path_pages
	path_test = _path_test
	path_log = _path_log
