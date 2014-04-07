#!/usr/bin/python2
# -*- coding: utf8 -*-

from __future__ import print_function
import rtdm
import tree_lib as tree
import os
from mapping import generate_template
from identical_sub_trees import get_classe_equivalencia
import file


"""
		Function: file_file
			Compara dois arquivos html
			retorna a similaridades dentre eles
"""

def file_file(file1,file2):

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

	print("Construcao do template", end="")
	#file_log.write("\n\n\n"+str(mape))
	file_regex = file.create_file_dir_default(file1, file2, ".regex")
	file_regex.write(generate_template(mape))
	print("[Ok]")

	print("\nT1:%s \nT2:%s \nMinimo de operacoes necessarias para similiridade:\t>>> %d <<< " % (file1, file2, operacoes))
	file_log.write("\nT1:%s \nT2:%s \nMinimo de operacoes necessarias para similiridade:\t>>> %d <<< " % (file1, file2, operacoes))

	print("Fim!")
	print(mape.extration_value)
	file_log.close()
	file_regex.close()

"""
		Function: file_dir
			Compara um arquivo especifico com os demais de determinado diretorio
			Retorna a similaridades de cada par(modelo,outra_pagina)
"""
def file_dir():
	for one_file in  os.listdir(path_dir):
		if(one_file.endswith(".html") or one_file.endswith(".htm")):
			file_tree1 = one_file
			print(file_tree2)
			file_file(path_dir+file_tree1,file_tree2)

	print("Fim do file_dir")

"""
Replace_choice
	1 - replace_no_no
	2 - replace_nos_t2
	3 - replace_mesma_quantidade_elementos 

"""

filename = os.path.dirname(os.path.realpath(__file__)) + "/../links_rtdm.txt"
file_tree1, file_tree2, path_dir = file.get_links(filename)
rtdm.replace_choice(3)
#file_file(file_tree1, file_tree2)

file_dir()
