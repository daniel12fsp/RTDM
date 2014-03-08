from bs4 import BeautifulSoup, Tag
import re
from tree_lib import is_wildcard
import composicao_curingas
from node import Node

def op_s(i,j):
	return i-1,j-1

def op_i(i,j):
	return i,j-1

def op_d(i,j):
	return i-1,j

def mapeamento_matrix(M, O, father, ci, cj):
	
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
		
		one = Node(father, left, right)
		father.add_child(one)
		mape.insert(0, one)

	return [father]+ mape

"""		
def head(ls):
	if(type(ls) is tuple):
		return ls[0]
	else:
		return head(ls[0])

def generate_list(ls):
	if((type(ls)) is list and len(ls)== 1):
		return generate_list(ls[0])
	
	if type(ls) is list and len(ls)>=2 :
		return ls[1:]
	
	return []
"""
			
def generate_template(ls):
	tree = mape_to_tree(ls)
	tree = promocao_curingas(tree.html.prettify())
	return tree

"""
def is_list_list(ls):
	result = True
	for i in ls:
		result = result or type(i) is list

	return result

"""

def mape_to_tree(ls):
	tree = BeautifulSoup("<html><head></head><body></body></html>")
	i = 0
	for father in ls:
		if(father.children):
			for child in father.children:
				subtree = mape_to_tree([child])
				child.tag = subtree.body.findChild()
				father.tag.append(child.tag)
	tree.body.append(father.tag)
	return tree

"""
def children_node(father, ls):
	i = father.children
	result = []
	for j in ls:
		if(i != 0): break
		if(j.father == father):
			result += [j]
			i -= 1
	return result
"""	
def get_mape_identical_subtree(father, no1):
	ls = []
	for i in no1.find_all(recursive=False):
		one = Node(father, i)
		ls += [one]
		father.add_child(one)
		children = i.find_all(recursive=False)
		if(children):
			ls += get_mape_identical_subtree( one, i)[1:]
	print("#no", father)
	return ls

	
def mapeamento_node(aux_mape, n1, n2):
	node = get_name_node(n1,n2) 
	if aux_mape == None :
		return [(node,node)]
	else: 
		return aux_mape

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
	tree = promocao_curingas_substituicao("asteristico","asterisco",tree)
	return tree





		
