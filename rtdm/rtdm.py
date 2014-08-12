#!/usr/bin/python2
# -*- coding: utf8 -*-
from __future__ import print_function
from utils import get_elem, exist_elem
import tree_lib as tree
from mapping import mapping_matrix, get_map_identical_subtree
from mapping_class import Mapping
from identical_sub_trees import get_classe_equivalencia
import numpy as np
import gc
#from hashlib  import md5# para teste

def op_ins_del_rep(t1, t2):
	i  = 0
	c1 = tree.get_children(t1)
	c2 = tree.get_children(t2)
	#Custos
	cd = ci = cr = 0
	if(not tree.equal(t1,t2)):
		ci += tree.length(t2)
		cd += tree.length(t1)
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

	if(i<len(c2)):
		for j in xrange(i, len(c2)):
			ci += tree.length(get_elem(c2, j))

	if(len(c1)>0):
		for j in xrange(i, len(c1)):
			cd += tree.length(get_elem(c1, j))

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


def dist_rtdm(filename1, filename2):
	tree1, tree2 = tree.files_to_trees(filename1, filename2)
	#k = get_classe_equivalencia(tree1, tree2)
	#prepareRTDM(k, None)
	operacoes = _dist_rtdm(tree1, tree2)
	return operacoes

def _dist_rtdm(t1, t2):
	c1 = [t1] + t1.find_all(recursive=False)
	c2 = [t2] + t2.find_all(recursive=False)
	
	m = len(c1)
	n = len(c2)

	line = np.zeros((n), dtype=np.int)

	for j in xrange(1, n):
		line[j] = line[ j - 1] + tree.length(c2[j])

	for i in xrange(1, m):
		diagonal = line[0]
		line[0] +=  tree.length(c1[i])
		left = line[0]
		for j in xrange(1, n):
			up = line[j]
			"""
			#Pre-processamento
			if(tree.is_any_wildcard(c1[i],c2[j]) or k[id(c1[i])]==k[id(c2[j])]):
				#print("oi")
				left = diagonal	
				line[j] = left
				diagonal = up
				continue
	
			el
			"""
			if(tree.equal(c1[i],c2[j])):
				left = diagonal + _dist_rtdm(c1[i], c2[j])	
				line[j] = left
				diagonal = up
				continue
			else:
				ti, td, tr = op_ins_del_rep(c1[i], c2[j])
				d = up + td
				a = left + ti
				r = diagonal
				r += tr
				if tree.is_leaf(c1[i]) and not tree.is_leaf(c2[j]):
					r += ti
				elif tree.is_leaf(c2[j]) and not tree.is_leaf(c1[i]):
					r += td
			left = min(d, a, r)
			line[j] = left
			diagonal = up

	return line[n - 1]
	
def calc_similaridade(filename1, filename2):
	tree1, tree2 = tree.files_to_trees(filename1, filename2)
	k = get_classe_equivalencia(tree1, tree2)
	prepareRTDM(k, None)
	operacoes, _ , _ = _RTDM(None, tree1, tree2)
#	gc.collect()
	return operacoes
	
def _RTDM(father, t1, t2):
	c1 = [t1]+t1.find_all(recursive=False)
	c2 = [t2]+t2.find_all(recursive=False)

	m = len(c1)
	n = len(c2)

	"""
		Aqui deve ser possivel otimizar essas duas linhas !
	"""
	M = [[0 for x in xrange(n)] for x in xrange(m)]
	O = [["" for x in xrange(n)] for x in xrange(m)]

	O[0][0]="s"

	for i in xrange(1, m):
		M[i][0] = M[i-1][0]+tree.length(c1[i])
		O[i][0] = "d"

	for j in xrange(1, n):
		M[0][j] = M[0][j-1]+tree.length(c2[j])
		O[0][j] = "i"

	aux = []
	i = j = 0
	
	father = Mapping.search_tuple(father, c1[0], c2[0])
	matrix = None
	for i in xrange(1, m):
		for j in xrange(1, n):
			aux_mape = None
			operacao = None
			ti, td, tr = op_ins_del_rep(c1[i], c2[j])
			d = M[i-1][j] + td
			a = M[i][j-1] + ti
			r = M[i-1][j-1]
			aux = [] 
			if(tree.is_any_wildcard(c1[i],c2[j]) or k[id(c1[i])]==k[id(c2[j])] ):
				M[i][j] = r
				O[i][j] = "s"#O[i-1][j-1]
				if(not tree.is_leaf(c1[i]) or not tree.is_leaf(c2[j])):
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
				num_op, operacao, _ = _RTDM(father, c1[i], c2[j])
				operacao = operacao + "~"
				r += num_op 
				a = d = r
			
			M[i][j] = min(d, a, r)
			if (operacao== None):
				O[i][j] = menor_operacao(d, a, r) 
			else:
				O[i][j] = operacao
		matrix =  mapping_matrix(M, O, father, c1, c2)

	return M[m-1][n-1], O[m-1][n-1], matrix
