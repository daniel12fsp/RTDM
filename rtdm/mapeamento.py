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
		eh_lista = (type(M[i][j]) is list)
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
	tree = BeautifulSoup("<html><head></head><body></body></html>")
	eh_interrogacao = False
	eh_ponto = False
	h = head(ls)
	print(h)
	if(type(h) is str and h != "body"):
		print("if-1")
		tree.body.append(Tag(name=h))
	father = tree.find_all(h)[0]
	for i in generate_list(ls):
		print("For")
		last = None
		print(i)
		if(type(i) is tuple ):
			print("eh tuple")
			(x, y) = i
			last = Tag(name = x)
			father.append(last)
			print("if-2 then",last)
			# Falta implementar para os curingas
		else:
			last = generate_template(i)
			print("if-2 else",last)
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

mape = [('body', 'body'), [[('div', 'div'), [('ul', 'ul'), [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]], [('li', 'li'), [('a', 'a'), [('b', 'b')]]]], [('div', 'div')]]], [[('hr', 'hr')]]]


#print(generate_list(mape))
#print(generate_list(generate_list(mape)))
