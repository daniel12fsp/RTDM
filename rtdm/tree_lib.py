#!/usr/bin/python2
# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
import identical_sub_trees
import bs4
from hashlib  import md5# para teste

def remove_tags(tree):
	"""
		Parametro:
			tree - arvore, type BeautifulSoup
		Tira as tags desnecessarias para comparacao como script, style, link
	meta e noscript

	"""
	[x.extract() for x in tree.findAll('script')]
	[x.extract() for x in tree.findAll('style')]
	[x.extract() for x in tree.findAll('link')]
	[x.extract() for x in tree.findAll('meta')]
	[x.extract() for x in tree.findAll('noscript')]

	return tree

def md5_node(tree):
	return	md5(tree.prettify().encode('utf-8')).hexdigest()

def search_md5_node(tree, m):
	"""
		Nao use essa funcao

		Funcao para testes somente
	"""

	for n in tree.find_all():
		if(md5_node(n) == m):
			return n

	return "Nao achou"
			


def preprare_tree(arq):
	"""
		Parametro:
			arq - nome do arquivo
		Retorno:
			a arvore apontando para noh body

		Prepara a arvore:
			1 - Carrega os elementos para memoria
			2 - Retira os elementos indesejados veja a funcao remove_tags
			3 - A arvore eh inicializada no campo body
	"""
	if(arq != None):
		tree = BeautifulSoup(open(arq, mode="rb"))
		"""
			Modificado para teste, por favor retire.....
		"""
		return remove_tags(tree).body
	else:
		return None
	
def files_to_trees(file_tree1, file_tree2):
	"""
		Paramentro:
			file_tree1 - nome do arquivo 1
			file_tree2 - nome do arquivo 2
		Retorno:
			a arvore1 apontando para noh body
			a arvore2 apontando para noh body
	"""
	return preprare_tree(file_tree1), preprare_tree(file_tree2) # Retorna a arvore do body
	id_ = "pane0"
	a = preprare_tree(file_tree1).find(id=id_) # Retorna a arvore pelo id
	b = preprare_tree(file_tree2).find(id=id_)

#	a = preprare_tree(file_tree1).find(id=id_).find_all(recursive=False)[5]
#	b = preprare_tree(file_tree2).find(id=id_).find_all(recursive=False)[5]
	return a,b


def str_to_tree(str_tree1, str_tree2):
	tree1 = preprare_tree()
	tree2 = BeautifulSoup(str_tree2).body
	remove_tag(tree1)
	remove_tag(tree2)
	return tree1, tree2



def get_children(tree):
	return	tree.find_all(recursive=False)

def post_order(tree):
	post = []
	for child in tree.children:
		if child.name is not None:
			post.extend(post_order(child))
			post.append(child)
	return post

def length(tree):
	try:
		return 1+sum(1 for _ in tree.find_all(True))
	except:
		return 0

def is_leaf(node):
	return ((get_children(node))==[])
	
def equal(x,y):
	return (is_wildcard(x) and is_leaf(y))  or (is_wildcard(y) and is_leaf(x)) or ((x.name == y.name) and (x.string == y.string))

def is_any_wildcard(x,y):
	return (is_wildcard(x) and is_leaf(y))  or (is_wildcard(y) and is_leaf(x))

def is_wildcard(x):
	wildcards = ["ponto","interrogacao","soma","asterisco"]
	if( type(x) is str): 
		return 	(x in wildcards)
	else:
		return 	(x.name in wildcards)
