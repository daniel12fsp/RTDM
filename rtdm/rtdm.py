from utils import get_elem, exist_elem
import os
import tree_lib as tree
from mapeamento import mapeamento_matrix, get_mape_identical_subtree, mapeamento_node
import sys
import node
def delete(t1, t2):
	i  = 0
	c1 = tree.get_children(t1)
	c2 = tree.get_children(t2)
	custo_delete = 0
	if(t1 is not None and t2 is not None) and ( not tree.equal(t1,t2)):
		custo_delete += tree.length(t1)
		return custo_delete

	while(i < len(c1) and i < len(c2)):

		node1 = get_elem(c1, i)
		node2 = get_elem(c2, i)
		custo_delete += delete(node1, node2)
		i += 1
	if(len(c1)>0):
		for j in range(i, len(c1)):
			custo_delete += tree.length(get_elem(c1, j))
	return custo_delete

def insert(t1, t2):
	i  = 0
	c1 = tree.get_children(t1)
	c2 = tree.get_children(t2)
	custo_insert = 0
	if(t1 is not None and t2 is not None) and ( not tree.equal(t1,t2)):
		custo_insert += tree.length(t2)
		return custo_insert

	while(i < len(c1) and i < len(c2)):
		node1 = get_elem(c1, i)
		node2 = get_elem(c2, i)
		custo_insert += insert(node1, node2)
		i += 1

	if(i<len(c2)):
		for j in range(i, len(c2)):
			custo_insert += tree.length(get_elem(c2, j))
	return custo_insert


"""
	Funcao: replace_no_no

		Verifica somente se a raiz da subarvore eh diferente, caso afirmativo returna 1, se nao 0
"""
def replace_no_no(t1, t2):
	return 1 if not tree.equal(t1,t2) else 0

"""
	Funcao: replace_nos_t2

		Retorna o valor de todos os nos da subarvore t2
"""
def replace_nos_t2(t1, t2):
	r = 0
	for j in tree.get_children(t2):
			r += tree.length(j)
	return r
"""
	Funcao: replace_mesma_quantidade_elementos

		Retorna o valor de elementos iguais nas posicoes equivalentes nas arvores
"""
def replace_mesma_quantidade_elementos(t1, t2):
	i  = 0
	c1 = tree.get_children(t1)
	c2 = tree.get_children(t2)
	custo_replace = 0
	if(t1 is not None and t2 is not None) and not tree.equal(t1,t2):
		custo_replace += tree.length(t2)

	while(i < len(c1) and i < len(c2)):
		node1 = get_elem(c1, i)
		node2 = get_elem(c2, i)
		custo_replace += replace_mesma_quantidade_elementos(node1, node2)
		i += 1
	return custo_replace

"""
	Funcao: replace_choice(option)
		
		Define qual funcao de replace sera utilizada dentre estas:
			1 - replace_no_no
			2 - replace_nos_t2
			3 - replace_mesma_quantidade_elementos 
"""
def replace_choice(option):
	print("A opcao de replace foi: %s" % (option))
	global replace
	if(option==1):
		replace = replace_no_no
	elif(option==2):
		replace = replace_nos_t2
	elif(option==3):
		replace = replace_mesma_quantidade_elementos

def prepareRTDM(k_parament, log_parament):
	global k
	k = k_parament
	global log
	log = log_parament

def menor_operacao(d,i,s):
	res = ""
	if(d >= i) and (s >= i):
		res += "i"
	if(i >= d) and (s >= d):
		res += "d"
	if(i >= s) and (d>= s):
		res += "s"
	return res

def RTDM(t1, t2):
	operacoes,_,_,mape = _RTDM(t1, t2, None)
	log.write("\n"+str(mape))
	return operacoes, mape
	
def _RTDM(t1, t2, grandfa):
	c1 = [t1]+t1.find_all(recursive=False)
	c2 = [t2]+t2.find_all(recursive=False)

	m = len(c1)
	n = len(c2)

	mape = []

	M = [[0 for x in range(n)] for x in range(m)]
	O = [["" for x in range(n)] for x in range(m)]

	O[0][0]="s"

	for i in range(1, m):
		M[i][0] = M[i-1][0]+tree.length(c1[i])
		O[i][0] = "d"

	for j in range(1, n):
		M[0][j] = M[0][j-1]+tree.length(c2[j])
		O[0][j] = "i"

	aux = []
	i = j = 0

	father = node.node(grandfa, c1[0], c2[0])


	for i in range(1, m):
		for j in range(1, n):
			
			aux_mape = None
			operacao = None
			d = (M[i-1][j]+delete(c1[i], c2[j]))
			a = (M[i][j-1]+insert(c1[i], c2[j]))
			s = M[i-1][j-1]
			aux = [] 

			if(tree.is_any_wildcard(c1[i],c2[j]) or k[id(c1[i])]==k[id(c2[j])] ):
				M[i][j] = s
				O[i][j] = "s"#O[i-1][j-1]
			#	mape = [get_mape_identical_subtree(c1[i])]
				continue
			elif(not tree.equal(c1[i],c2[j])):
				s += replace(c1[i], c2[j])

				if tree.is_leaf(c1[i]) and not tree.is_leaf(c2[j]):
					s += insert(c1[i], c2[j])

				elif tree.is_leaf(c2[j]) and not tree.is_leaf(c1[i]):
					s += delete(c1[i], c2[j])

			else:
				num_op, operacao,_, aux_mape = _RTDM(c1[i], c2[j], father)

				mape = aux_mape + mape
				#d = sys.maxint
				#a = sys.maxint
				operacao = operacao + "~"
				s += num_op 

			M[i][j] = min(d, a, s) 
			O[i][j] = menor_operacao(d, a, s) if (operacao== None) else operacao

	for x in range(0, m):
		log.write("\n")
		for y in range(0, n):
				log.write("{m:4d}{o:1s} ".format(x, m=M[x][y], o=O[x][y]))

	#log.write("\nMape:"+ str(mape))
	matrix =  mapeamento_matrix(M, O, father, c1, c2)

	if( mape != [] and matrix[-1] == mape[0]):
		ls  = [father] + matrix[:-1] + mape 
	else:
		ls  = [father] + matrix + mape

	log.write("\n"+str(ls))
	return M[m-1][n-1], O[m-1][n-1],M, ls

def print_tuple(ls):
	res = []
	for i in ls:
			#print(i)
			res += (i[0].name,i[1].name) 
	
	return str(res)


def last(ls):
	if( type(ls[-1]) is list ):
		return last(ls[-1])
	else:
		return ls[-1]

def last_elem_list(origin, ls, mape):
	if( list in [ type(i) for i in ls] ):
		last_elem_list(origin, ls[-1], mape)
	else:
		ls.pop()
		origin += [mape]


def is_list_list(ls):
	result = True
	for i in ls:
		result = result or type(i) is list

	return result

