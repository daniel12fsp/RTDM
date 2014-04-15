#!/usr/bin/python2
# -*- coding: utf8 -*-

from __future__ import print_function
import rtdm
import tree_lib as tree
import os
from mapping import generate_template
from identical_sub_trees import get_classe_equivalencia
import file
import xpath
import pick

max_operation = 800
min_operation = 100

def file_file(file1,file2):
	"""
			Function: file_file
				Compara dois arquivos html
				retorna a similaridades dentre eles
	"""
	print("\nT1:%s \nT2:%s" % (file1,file2))
	print("Carregando as arvores(arquivos para arvores)", end="")
	#Lembrado que tree1 e tree2 jah comeca do body!
	tree1, tree2 = tree.file_to_tree(file1, file2)
	print("[Ok]")

	print("Calculando a classe de equivalencia", end="")
	k = get_classe_equivalencia(tree1, tree2)
	print("[Ok]")

	print("Criando arquivo de log", end="")
	file_log = file.create_file_dir_default(file1, file2, ".log")
	print("[Ok]")

	print("Comecando a executar o RTDM!", end="")
	rtdm.prepareRTDM(k, file_log)
	operacoes, mape = rtdm.RTDM(tree1, tree2)

	print("[Ok]")

	if(operacoes > min_operation and operacoes <= max_operation):
		print("Construcao do template", end="")
		file_regex = file.create_file_dir_default(file1, file2, ".regex")
		file_regex.write(generate_template(mape))
		file_regex.close()
		print("[Ok]")
	else:
		print("Paginas nao similares! ")

	print("\nMinimo de operacoes necessarias para similiridade:\t>>> %d <<< " % (operacoes))
	file_log.write("\nT1:%s \nT2:%s \nMinimo de operacoes necessarias para similiridade:\t>>> %d <<< " % (file1, file2,operacoes))

	print("Fim!")
	file_log.close()

	return operacoes, file.get_path_file(file1, file2, ".regex")



def file_dir(page_comp, path_dir):
	"""
			Function: file_dir
				Compara um arquivo especifico com os demais de determinado diretorio
				Retorna a similaridades de cada par(modelo,outra_pagina)
	"""
	for one_file in os.listdir(path_dir):
		if(one_file.endswith(".html") or one_file.endswith(".htm")):
			file_tree1 = one_file
			file_file(path_dir+file_tree1,file_tree2)

	print("Fim do file_dir")

def generate_xpath_file_pick(path_dir, quant_elem):
	picks = pick.list_random_files(path_dir, quant_elem)
	print(picks)
	i = 0
	page2 = picks[i]
	while(i+1 < len(picks)):
		page1 = picks[i+1]
		aux = page2
		operacoes, page2 = file_file(page1, page2)
		if(operacoes > min_operation and operacoes <= max_operation ):
			last_regex = page2
			pass
			file_xpath = file.create_file(page2, ".xpath")
			xpath.create( page2, file_xpath)
		else:
			page2 = picks[i]
		i += 1
	
	file_xpath = path_dir + "extraction.xpath"
	xpath.create( last_regex, file_xpath)

	print("Fim do file_pick")




"""
Replace_choice
	1 - replace_no_no
	2 - replace_nos_t2
	3 - replace_mesma_quantidade_elementos 

"""

filename = os.path.dirname(os.path.realpath(__file__)) + "/../links_rtdm.txt"
pick.execute_bash(open( os.path.dirname(os.path.realpath(__file__))+"/remove.sh").read())
path_dir = file.get_links(filename)
rtdm.replace_choice(3)
generate_xpath_file_pick(path_dir, 2)
#file_dir()
