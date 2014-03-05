from bs4 import BeautifulSoup, Tag
import re
from tree_lib import is_wildcard
import composicao_curingas

def op_s(i,j):
	return i-1,j-1

def op_i(i,j):
	return i,j-1

def op_d(i,j):
	return i-1,j

def mapeamento_array(M,O,ci,cj):
	
	i = len(M)-1
	j = len(M[0])-1
	mape = []
	fila = []
	tmp = None
	while(i>=0 and j>0):
		eh_lista = (type(M[i][j]) is list)
		if("s" in O[i][j] or "~" in O[i][j]):
			if eh_lista:
				tmp = M[i][j]
			else:
				tmp = (ci[i], cj[j])
			i, j = op_s(i, j)
		elif("d" in O[i][j]):
			if eh_lista:
				tmp = M[i][j]
			else:
				tmp = (ci[i], Tag(name = "0"))
			i, j = op_d(i, j)
		elif("i" in O[i][j]):
			if eh_lista:
				tmp = M[i][j]
			else:
				tmp = (Tag( name = "0"), cj[j])
			i, j = op_i(i, j)

		mape.insert(0,tmp)

	ls = [(ci[0],cj[0])] + [mape]

	return ls

		
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
			
def generate_template(ls):
	tree = mape_to_tree(ls)
	tree = promocao_curingas(tree.html.prettify())
	return tree
	
def is_list_list(ls):
	result = True
	for i in ls:
		result = result or type(i) is list

	return result

def mape_to_tree(ls):
	tree = BeautifulSoup("<html><head></head><body></body></html>")
	h = head(ls)
	if(type(h) is str and h != "body"):
		tree.body.append(Tag(name=h))
	father = tree.find_all(h.name)
	for i in generate_list(ls):
		last = None
		if(type(i) is tuple or  not is_list_list(i)):
			if(type(i) is tuple):	
				i = [i]
			for node in i:
				node_name = get_name_node(node[0], node[1])
				last = Tag(name = node_name)
				father.append(last)
		else:
			last = mape_to_tree(i)
			father.append(last.body.findChild())
	return tree
	
def get_mape_identical_subtree(node):
	ls = [(node.name, node.name)]
	children = []
	if(str(type(node)) == "<class 'bs4.element.Tag'>"):
		for i in node.children:
			tmp = get_mape_identical_subtree(i)
			if(tmp):
				children += [tmp] 
			else:
				continue
		return ls+children
	return None

def get_name_node(n1,n2):


	if(n1 == "0" or n2 == "0"):
		return "interrogacao"

	if(not is_wildcard(n1) and not is_wildcard(n2) and n1 != n2 ):
		return "ponto"
	
	if(not is_wildcard(n1) and not is_wildcard(n2) and n1 == n2 ):
		return n1

	if(is_wildcard(n1) and not is_wildcard(n2)):
		return n1
	
	if(is_wildcard(n2) and not is_wildcard(n1)):
		return n2	
		
	return composicao_curingas.get_curinga(n1, n2)
	
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

