#!/usr/bin/python2
# -*- coding: utf8 -*-
from __future__ import print_function
from utils import get_elem, exist_elem
import tree_lib as tree
from mapping import mapping_matrix, get_map_identical_subtree
from mapping_class import Mapping
from identical_sub_trees import get_classe_equivalencia
import numpy as np

#from hashlib  import md5# para teste

def op_ins_del_rep(t1, t2):
	i  = 0
	c1 = tree.get_children(t1)
	c2 = tree.get_children(t2)
	#Custos
	cd = 0
	ci = 0
	cr = 0
	if(not tree.equal(t1,t2)):
		cd += tree.length(t1)
		ci += tree.length(t2)
		cr += 1
		return ci, cd, cr

	while(i < len(c1) and i < len(c2)):

		node1 = get_elem(c1, i)
		node2 = get_elem(c2, i)
		ti, td, tr = op_ins_del_rep(node1, node2)
		ci += ti
		cd += td
		cr += tr
		i += 1

	if(len(c1)>0):
		for j in range(i, len(c1)):
			cd += tree.length(get_elem(c1, j))

	if(i<len(c2)):
		for j in range(i, len(c2)):
			ci += tree.length(get_elem(c2, j))

	return ci, cd, cr


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

def RTDM(t1, t2, tree_regex=False):	
	operacoes,_,_,mape = _RTDM(None, t1, t2, tree_regex)
	#log.write("\n"+str(mape))
	return operacoes, mape

def calc_similaridade(page1, page2):
	tree1, tree2 = tree.files_to_trees(page1, page2)
	k = get_classe_equivalencia(tree1, tree2)
	prepareRTDM(k, None)
	operacoes, _ = RTDM(tree1, tree2)
	return operacoes
	
def _RTDM(father, t1, t2, tree_regex):
	c1 = [t1]+t1.find_all(recursive=False)
	c2 = [t2]+t2.find_all(recursive=False)

	m = len(c1)
	n = len(c2)

	M = np.zeros(shape=(len(c1), len(c2)), dtype=np.uint)
	O = np.zeros(shape=(len(c1), len(c2)), dtype='|S4')

	O[0][0]="s"

	for i in range(1, m):
		M[i][0] = M[i-1][0]+tree.length(c1[i])
		O[i][0] = "d"

	for j in range(1, n):
		M[0][j] = M[0][j-1]+tree.length(c2[j])
		O[0][j] = "i"

	aux = []
	i = j = 0
	
	if(tree_regex):
		father = Mapping.search_tuple(father, c1[0], c2[0])

	for i in range(1, m):
		for j in range(1, n):
			
			aux_mape = None
			operacao = None
			td, ti, tr = op_ins_del_rep(c1[i], c2[j])
			d = M[i-1][j] + td
			a = M[i][j-1] + ti
			r = M[i-1][j-1]
			aux = [] 
			if(tree.is_any_wildcard(c1[i],c2[j]) or k[id(c1[i])]==k[id(c2[j])] ):
				M[i][j] = r
				O[i][j] = "s"#O[i-1][j-1]
				if(not tree.is_leaf(c1[i]) or not tree.is_leaf(c2[j])):
					new_father = None
					if(tree_regex):
						new_father = Mapping.search_tuple(father, c1[i], c2[j])
					get_map_identical_subtree(new_father, c1[i], c2[j])
				continue
			elif(not tree.equal(c1[i],c2[j])):
				r += tr

				if tree.is_leaf(c1[i]) and not tree.is_leaf(c2[j]):
					r += ti
				elif tree.is_leaf(c2[j]) and not tree.is_leaf(c1[i]):
					r += td
			else:
				num_op, operacao, _, _ = _RTDM(father, c1[i], c2[j], tree_regex)
				operacao = operacao + "~"
				r += num_op 
				a = d = r
			
			M[i][j] = min(d, a, r) 

			if (operacao== None):
				O[i][j] = menor_operacao(d, a, r) 
			else:
				O[i][j] = operacao
			'''
			"""As parte comentada sao informacoes uteis para debug"""
			"""
			#Caso queira ver a operacao escolhido entre dois elementos - comeco
			#print de cada celula da matriz

 			print("\n\tM[%d][%d](%s x %s)\t\n \t\t\tR: i:%d,d:%d,s:%d \n\t\t\tA: i:%d,d:%d,s:%d" % 

 					(i, j, c1[i].name, c2[j].name, a - M[i][j-1], d - M[i-1][j], s - M[i-1][j-1], a, d, s))
			"""
	
			#Caso queira ver a operacao escolhido entre dois elementos - fim

	#MD5 - comeco
	x =  tree.md5_node(c1[0])
	y =  tree.md5_node(c2[0])
	
	if(x > y):
		print(x, y, M[m-1][n-1])
	else:
		print(y, x, M[m-1][n-1])
	#MD5 - fim
	
	#imprimir o codigo fonte das subarvores que fazem parte da matriz - comeco
	print(x)
	print(c1[0].prettify().encode('utf-8'))
	print(y)
	print(c2[0].prettify().encode('utf-8'))
	#imprimir o codigo fonte das subarvores que fazem parte da matriz - fim

	#Caso queira ver a matriz construida - comeco
	print("t1 =", c1[0].name, c1[0].get("id"), x)
	print("t2 =", c2[0].name, c2[0].get("id"), y)
	print(M[i][j])
	'''

	for x in range(0, m):
		print()
		for y in range(0, n):
				print("{m:3d}{o:5s} ".format(x, m=M[x][y], o=O[x][y][:2]), end=" ")
	print("\n"+"-"*40)
	#Caso queira ver a matriz construida - fim

	if(tree_regex):
		matrix =  mapping_matrix(M, O, father, c1, c2)
	else:
		matrix = None

	return M[m-1][n-1], O[m-1][n-1],M, matrix
