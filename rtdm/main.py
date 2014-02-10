from __future__ import print_function
import rtdm
import tree_lib as tree
import os
from mapeamento import generate_template,get_list
from identical_sub_trees import get_classe_equivalencia
import file

def get_links(file_name):
	myfile = open(file_name, "r")
	files_names = myfile.readlines()
	global file_tree1
	file_tree1 = files_names[0][:-1]
	global file_tree2
	file_tree2 = files_names[1][:-1]
	global path_dir
	path_dir = files_names[2][:-1]

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

	print("Criando arquivo de log")
	file_log = file.create_file_dir_default(file1, file2, ".log")
	print("[Ok]")

	print("Comecando a executar o RTDM!", end="")
	rtdm.prepareRTDM(k, file_log)
	simi,M,mape = rtdm.RTDM(tree1, tree2)
	print("[Ok]")

	print(mape[1][0])
	print("Mapeamento",mape)
	file_log.write("%s %s %f" % (file1, file2, simi))
	print("\nt1 = "+file1, "\nt2 = "+file2, "\nSimilaridade\t\t->>>", simi,"<<<-")
	print("Carregando as")
	file_regex = file.create_file_dir_default(file1, file2, ".regex")
	print(file_regex)
	file_regex.write(generate_template(mape).html.prettify())

	file_log.close()
	file_regex.close()

"""
		Function: file_dir
			Compara um arquivo especifico com os demais de determinado diretorio
			Retorna a similaridades de cada par(modelo,outra_pagina)
"""
def file_dir():
	for one_files in  os.listdir(path_dir):
		if(one_files.endswith(".html") or one_files.endswith(".htm")):
			file_log = file_tree2+"-"+one_files+".log"
			log = open(file_log, "w")
			file_tree1 = one_files
			file_file(path_dir+file_tree1,file_tree2)

"""
Replace_choice
	1 - replace_no_no
	2 - replace_nos_t2
	3 - replace_mesma_quantidade_elementos 

"""
filename = os.path.dirname(os.path.realpath(__file__)) + "/../links.txt"

get_links(filename)
rtdm.replace_choice(3)
file_file(file_tree1, file_tree2)
#file_dir()
