#!/usr/bin/python2
# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import re
from tree_lib import is_wildcard
from mapping_class import Mapping

composicao_curingas = {
	"asterisco,asterisco" : "asterisco",
	"asterisco,mais" : "asterisco",
	"asterisco,interrogacao" : "asterisco",
	"asterisco,ponto" : "asterisco",
	"mais,mais" : "mais",
	"mais,ponto" : "mais",
	"mais,interrogacao" : "asterisco",
	"ponto,ponto" : "ponto",
	"ponto,interrogacao" : "interrogacao",
	"interrogacao,interrogacao" : "interrogacao"
}



def op_s(i,j):
	return i-1,j-1

def op_i(i,j):
	return i,j-1

def op_d(i,j):
	return i-1,j

def mapping_matrix(M, O, father, ci, cj):
	
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

def generate_template(ls):
	tree = mapping_to_tree(ls)
	tree = promocao_curingas(tree.html.prettify())
	return tree

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
	children1 = node1.find_all(recursive=False)
	children2 = node2.find_all(recursive=False)

	for i in range(0, len(children1)):
		child1 = children1[i]
		child2 = children2[i]
		one = Mapping.search_tuple(father, child1, child2)
		father.append_child(one)
		c1 = child1.find_all(recursive=False)
		c2 = child2.find_all(recursive=False)
		if(c1):
			get_map_identical_subtree( one, child1, child2)

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


def get_curinga(n1, n2):
	if(type(n1) is str):
		return composicao_curingas[n1+","+n2]
	else:
		return composicao_curingas[n1.name+","+n2.name]

	
