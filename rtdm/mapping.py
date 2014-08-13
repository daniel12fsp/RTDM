#!/usr/bin/python2
# -*- coding: utf8 -*-

from bs4 import BeautifulSoup, Tag
import re
from tree_lib import is_wildcard
from mapping_class import Mapping
import file


def op_s(i,j):
	return i-1,j-1

def op_i(i,j):
	return i,j-1

def op_d(i,j):
	return i-1,j

def mapping_matrix(M, O, father, ci, cj):
	#TODO
	"""
		Realmente precisa de M, posso passar tamanho pelo O
	"""
	i = len(M)-1
	j = len(M[0])-1
	mape = []
	fila = []
	tmp = None

	while(i>=0 and j>0):
		if("s" in O[i][j] or "~" in O[i][j]):
			left = ci[i]
			right = cj[j]
			i, j = op_s(i, j)
		elif("d" in O[i][j]):
			left = ci[i]
			right = "0"
			i, j = op_d(i, j)
		elif("i" in O[i][j]):
			left = "0"
			right = cj[j]
			i, j = op_i(i, j)
		one = Mapping.search_tuple(father, left, right)
		father.push_child(one)
		mape.insert(0, one)

	return father

def save_regex(file1, file2, operacoes):
	path_regex = file.get_path_file(file1, file2, ".regex")
	file_regex = open(path_regex, "w")
	file_regex.write(generate_template(operacoes))
	return path_regex

def generate_template(ls):
	tree = mapping_to_tree(ls)
	#tree = promocao_curingas(tree.html.prettify())



	return tree.html.prettify()

def mapping_to_tree(father):
	tree = BeautifulSoup("<html><head></head><body></body></html>")
	i = 0
	if(father.children):
		for child in father.children:
			subtree = mapping_to_tree(child)
			child.tag = subtree.body.findChild()
			father.tag.append(child.tag)
	tree.body.append(father.tag)
	return tree

def get_map_identical_subtree(father, node1, node2):
	if(father != None):
		children1 = node1.find_all(recursive=False)
		if(type(node2) == Tag):
			children2 = node2.find_all(recursive=False)
		else:
			children2 = []

		for i in range(0, len(children1)):
			child1 = children1[i]
			if(len(children2)>i):
				child2 = children2[i]
			else:
				child2 = "0"
			one = Mapping.search_tuple(father, child1, child2)
			father.append_child(one)
			c1 = child1.find_all(recursive=False)
			if(c1):
				get_map_identical_subtree( one, child1, child2)
	else:
		return None

def regex_tag(string,curinga = "\W*"):
	return "<"+string+">"+curinga+"</"+string+">"

def end_pattern():
	return "\W*"+regex_tag("interrogacao")+"\W*"+regex_tag("interrogacao")+"\W*"+regex_tag("interrogacao")

def promocao_curingas_substituicao(primeira_tag, promocao_tag, tree):
	regex = regex_tag(primeira_tag)+end_pattern()
	return re.sub(regex, regex_tag(promocao_tag, curinga=""), tree)

def promocao_curingas(tree):
	tree = promocao_curingas_substituicao("mais","mais",tree)
	tree = promocao_curingas_substituicao("ponto","mais",tree)
	tree = promocao_curingas_substituicao("interrogacao","asterisco",tree)
	tree = promocao_curingas_substituicao("asterisco","asterisco",tree)
	return tree
