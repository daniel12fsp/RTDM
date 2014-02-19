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
	while(i>0 and j>0):
		eh_lista = (type(M[i][j]) is list)
		if("s" in O[i][j]):
			if eh_lista:
				tmp = M[i][j]
			else:
				tmp = (ci[i].name, cj[j].name)
			i, j = op_s(i, j)
		elif("d" in O[i][j]):
			if eh_lista:
				tmp = M[i][j]
			else:
				tmp = (ci[i].name,"0")
			i, j = op_d(i, j)
		elif("i" in O[i][j]):
			if eh_lista:
				tmp = M[i][j]
			else:
				tmp = ("0", cj[j].name)
			i, j = op_i(i, j)

		mape.insert(0,tmp)

	if(type(tmp) is tuple):
		return [(ci[0].name,cj[0].name)] + [tmp]
	else:
		return [(ci[0].name,cj[0].name)] + mape
		
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
	
def mape_to_tree(ls):
	tree = BeautifulSoup("<html><head></head><body></body></html>")
	eh_interrogacao = False
	eh_ponto = False
	h = head(ls)
	#print(h)
	if(type(h) is str and h != "body"):
		#print("if-1")
		tree.body.append(Tag(name=h))
	father = tree.find_all(h)[0]
	for i in generate_list(ls):
		#print("For")
		last = None
		#print(i)
		if(type(i) is tuple ):
			#print("eh tuple")
			last = Tag(name = i)
			father.append(last)
			# Falta implementar para os curingas
		else:
			last = mape_to_tree(i)
			#print("if-2 else",last)
			father.append(last.body.findChild())
	return tree
	
def get_list(node):
	ls = [(node.name, node.name)]
	children = []
	if(str(type(node)) == "<class 'bs4.element.Tag'>"):
		for i in node.children:
			tmp = get_list(i)
			if(tmp):
				children += [tmp] 
			else:
				continue
		return ls+children
	return None

def get_name_node(n1,n2):

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

def tag(string,curinga = "\W*"):
	return "<"+string+">"+curinga+"</"+string+">"

def end_pattern():
	return "\W*"+tag("interrogacao")+"\W*"+tag("interrogacao")+"\W*"+tag("interrogacao")

def promocao_curingas_substituicao(primeira_tag, promocao_tag, tree):
	regex = tag(primeira_tag)+end_pattern()
	return re.sub(regex, tag(promocao_tag, curinga=""), tree)
	

def promocao_curingas(tree):
	tree = promocao_curingas_substituicao("mais","mais",tree)
	tree = promocao_curingas_substituicao("ponto","mais",tree)
	tree = promocao_curingas_substituicao("interrogacao","asterisco",tree)
	tree = promocao_curingas_substituicao("asteristico","asterisco",tree)
	return tree

