#!/usr/bin/python2
# -*- coding: utf8 -*-

from __future__ import print_function
import tree_lib as tree
import os
import file

def file_dir():
	for one_file in  os.listdir(path_dir):
		if(one_file.endswith(".html") or one_file.endswith(".htm")):
			file_tree1 = one_file
			extracao(path_dir+"/"+file_tree1,file_templete)

	print("Fim do file_dir")


def extracao(page,templete):
	print(templete,page)
	print("Carregando os arquivo e calculando o vetor associativo...")
	tree1, tree2 = tree.file_to_tree(page,templete)
	name_file_datas = page+"-datas.xml"
	file_datas = open(name_file_datas, "w")
	t1 = [tree1] + tree1.find_all()
	t2 = [tree2] + tree2.find_all()
	print("Tree1 -- [OK]")
	print("Tree2 -- [OK]")
	print(len(t2))
	print(len(t1))
	for i in range(0, len(t2)):
		if tree.is_wildcard(t2[i]):
			try:
				print(t1[i],file=file_datas)			
			except:
				print("Nao Existe")			


filename = os.path.dirname(os.path.realpath(__file__)) + "/../links_extration.txt"
file_tree1, file_templete, path_dir = file.get_links(filename)
file_dir()
