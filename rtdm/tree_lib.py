"""
Modulo responsavel por manipular os nos das arvores

Funcoes

	remove_tag
	begin
	get_children
	length
	is_leaf
	print_children
	decodificar2utf8()
	post_order
"""

from bs4 import BeautifulSoup
import identical_sub_trees

def remove_tag(tree):
	[x.extract() for x in tree.findAll('script')]
	[x.extract() for x in tree.findAll('style')]
	[x.extract() for x in tree.findAll('link')]
	[x.extract() for x in tree.findAll('meta')]
	[x.extract() for x in tree.findAll('noscript')]

def decodificar2utf8(arq):
	return open(arq, mode="rb")

def file_to_tree(file_tree1, file_tree2):
	tree1 = BeautifulSoup(decodificar2utf8(file_tree1)).body.sel
	tree2 = BeautifulSoup(decodificar2utf8(file_tree2)).body.sel
	remove_tag(tree1)
	remove_tag(tree2)
	return tree1, tree2

def get_children(tree):
	return	tree.find_all(recursive=False)

def post_order(tree):
	post = []
	try:
		for child in tree.children:
			if child.name is not None:
				post += post_order(child)
				post += [child]
		return post
	except:
		return post

def length(tree):
	try:
		return 1+sum(1 for _ in tree.find_all(True))
	except:
		return 0

def is_leaf(node):
	return ((get_children(node))==[])
	
def equal(x,y):
	return (is_wildcard(x) and is_leaf(y))  or (is_wildcard(y) and is_leaf(x)) or (x.name == y.name)

def is_any_wildcard(x,y):
	return (is_wildcard(x) and is_leaf(y))  or (is_wildcard(y) and is_leaf(x))

def is_wildcard(x):
	wildcards = ["ponto","interrogacao","soma","asterisco"]
	print(x)
	if( type(x) is str): 
		return 	(x in wildcards)
	else:
		return 	(x.name in wildcards)
