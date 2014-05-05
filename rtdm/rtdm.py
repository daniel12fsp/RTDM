#!/usr/bin/python2
# -*- coding: utf8 -*-

from utils import get_elem, exist_elem
import tree_lib as tree
from mapping import mapping_matrix, get_map_identical_subtree
from mapping_class import Mapping
from identical_sub_trees import get_classe_equivalencia

def tree_operation(t1, t2):
	i  = 0
	cust_insert = 0
	cust_delete = 0
	cust_replace = 0
	if(t1 is not None and t2 is not None) and (not tree.equal(t1,t2)):
		t2_length = tree.length(t2)
		cust_insert += t2_length
		cust_delete += tree.length(t1)
		cust_replace += t2_length
		return cust_insert, cust_delete, cust_replace

	c1 = tree.get_children(t1)
	c2 = tree.get_children(t2)
	while(i < len(c1) and i < len(c2)):
		node1 = get_elem(c1, i)
		node2 = get_elem(c2, i)
		cust_insert, cust_delete, cust_replace = tree_operation(node1, node2)
		i += 1

	if(i<len(c2)):
		for j in range(i, len(c2)):
			cust_insert += tree.length(get_elem(c2, j))

	if(len(c1)>0):
		for j in range(i, len(c1)):
			cust_delete += tree.length(get_elem(c1, j))

	return cust_insert, cust_delete, cust_replace

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
	operacoes,_,_,mape = _RTDM(None, t1, t2)
	log.write("\n"+str(mape))
	return operacoes, mape

def calc_similaridade(page_fixa, page2):
	tree1, tree2 = tree.str_to_tree(page_fixa, page2)
	k = get_classe_equivalencia(tree1, tree2)
	replace_choice(3)
	prepareRTDM(k, None)
	operacoes, _ = RTDM(tree1, tree2)
	return operacoes

def replace_choice(option):
	pass
	
def _RTDM(father, t1, t2):
	c1 = [t1]+t1.find_all(recursive=False)
	c2 = [t2]+t2.find_all(recursive=False)

	m = len(c1)
	n = len(c2)

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
	

	father = Mapping.search_tuple(father, c1[0], c2[0])

	for i in range(1, m):
		for j in range(1, n):
			
			aux_mape = None
			operacao = None
			cust_insert, cust_delete, cust_replace =  tree_operation(c1[i], c2[j])
			d = M[i-1][j] + cust_delete
			a = M[i][j-1] + cust_insert
			s = M[i-1][j-1] 
			aux = [] 
			if(tree.is_any_wildcard(c1[i],c2[j]) or k[id(c1[i])]==k[id(c2[j])] ):
				M[i][j] = s
				O[i][j] = "s"#O[i-1][j-1]
				if(not tree.is_leaf(c1[i]) or not tree.is_leaf(c2[j])):
					new_father = Mapping.search_tuple(father, c1[i], c2[j])
					get_map_identical_subtree(new_father, c1[i], c2[j])
				continue
			elif(not tree.equal(c1[i],c2[j])):
				s += cust_replace

				if tree.is_leaf(c1[i]) and not tree.is_leaf(c2[j]):
					s += cust_insert

				elif tree.is_leaf(c2[j]) and not tree.is_leaf(c1[i]):
					s += cust_delete

			else:
				num_op, operacao, _, _ = _RTDM(father, c1[i], c2[j])
				#d = sys.maxint
				#a = sys.maxint
				operacao = operacao + "~"
				s += num_op 

			M[i][j] = min(d, a, s) 
			O[i][j] = menor_operacao(d, a, s) if (operacao== None) else operacao
			"""
			Caso queira ver a operacao escolhido entre dois elementos

 			log.write("\n\tM[%d][%d](%s x %s)\t\n \t\t\tR: i:%d,d:%d,s:%d \n\t\t\tA: i:%d,d:%d,s:%d" % 

 					(i, j, c1[i].name, c2[j].name, a - M[i][j-1], d - M[i-1][j], s - M[i-1][j-1], a, d, s))
			"""
	"""
	Caso queira ver a matriz construida
	for x in range(0, m):
		log.write("\n")
		for y in range(0, m):
				log.write("{m:d}{o:1s} ".format(x, m=M[x][y], o=O[x][y]))
	"""


	matrix =  mapping_matrix(M, O, father, c1, c2)
	return M[m-1][n-1], O[m-1][n-1],M, matrix
