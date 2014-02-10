from bs4 import BeautifulSoup, Tag
import re
from tree_lib import is_wildcard

def op_s(i,j):
	return i-1,j-1,i

def op_i(i,j):
	return i,j-1,i

def op_d(i,j):
	return i-1,j,i

def mapeamento_array(M,O,ci,cj):
	i = len(M)-1
	j = len(M[0])-1
	mape = []
	fila = []
	tmp = None
	while(i>0 and j>0):
		eh_lista = type(M[i][j])==type(list())
		if("s" in O[i][j]):
			if eh_lista:
				tmp = M[i][j]
			else:
				tmp = (ci[i].name, cj[j].name)
			i, j, last_i = op_s(i, j)
		elif("d" in O[i][j]):
			if eh_lista:
				tmp = M[i][j]
			else:
				tmp = (ci[i].name,"0")
			i, j, last_i = op_d(i, j)
		elif("i" in O[i][j]):
			if eh_lista:
				tmp = M[i][j]
			else:
				tmp = ("0", cj[j].name)
			i, j, last_i = op_i(i, j)
		mape.insert(0, tmp)
	return [(ci[0].name,cj[0].name)] + [mape]
		
def head(ls):
	return ls[0][0]

def generate_template(ls):
	tree = BeautifulSoup("<html><head></head><body></body></html>")
	eh_interrogacao = False
	eh_ponto = False
	i = head(ls)
	if(type(i) == type(tuple())):
		return generate_template(ls[0])

	if(type(i) is str and i != "body"):
		tree.body.append(Tag(name=i))
	father = tree.find_all(i)[0]
	for i in ls[1:]:
		last = None
		print(i)
		if(i is tuple ):
			(x, y) = i
			last = Tag(name=x)
			father.append(last)
			# Falta implementar para os curingas
		else:
			last = generate_template(i)
			print(father,last)
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


mape = [[('estatua', 'estatua'), [('manaus', 'manaus')]]]
print(generate_template(mape))

