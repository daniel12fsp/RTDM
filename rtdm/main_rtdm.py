##!/usr/bin/env python
#-*- coding:utf-8 -*-

from __future__ import print_function
from __future__ import division
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

def generate_xpath(path_dir, quant_elem):
	files = file.list_random_pages(path_dir)[:quant_elem]
	path_general_xpath = path_dir + "general_xpath.txt" 
	file_general_xpath = open(path_general_xpath, "w", 0)
	while(len(files) >= 2):
		page2 = files.pop()
		select_pages = [page2]
		lca = ""
		valid_page = 2  
		while(len(files) > 0):
			page1 = files.pop()
			aux = page2
			operacoes, page2 = rtdm.create_regex(page1, page2)
			if(min_operation <= operacoes and operacoes <= max_operation ):
				print(page1)
				print(page2)
				print( "Operacoes <%d>" % (operacoes))
				tree1, tree2 = tree.files_to_trees(page1, page2)
				print("Len T1: %d \t Len T2: %d" % (tree.length(tree1),tree.length(tree2)))
				porcentagem_relativa = (((operacoes)/(tree.length(tree1)))*100)
				print("Poncentagem Relativa: %2.2f" % (porcentagem_relativa))
				lca = xpath.create(page2)
				select_pages.append(page1)
				valid_page += 1
			else:
				page2 = aux
			if(valid_page > quant_elem):
				break

		print("Resultado Final", file = file_general_xpath)
		print(select_pages, file = file_general_xpath)
		print("\t\t>>>"+lca+"<<<", file = file_general_xpath)
		print("----------------", file = file_general_xpath)

	file_general_xpath.close()

path_pages = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/notebooks/submarino_notebook/";
generate_xpath(path_pages, 5)
