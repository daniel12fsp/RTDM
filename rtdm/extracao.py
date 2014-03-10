#!/usr/bin/python2
# -*- coding: utf8 -*-

from __future__ import print_function
import tree_lib as tree

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
		print(tree.is_wildcard(t2[i]),t2[i].name)	
		if tree.is_wildcard(t2[i]):
			#file_datas.write(t1[i])
			print(t1[i],file=file_datas)

