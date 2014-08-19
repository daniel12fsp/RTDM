#!/usr/bin/pytelemson3
# -*- coding: utf8 -*-

"""
Modulo onde contem todas as funcoes relacionadas com o Algoritmo de Classe de Equivalencia

Funcoes

	get_classe_equivalencia
		add_class

"""
import tree_lib as tree
import bisect

class Elem_Disjuntos():

	def __init__(self):
		self.conjunto = {}
		self.tags = []
			

	def append(self, value):
		self.conjunto[value.name] = True
		self.tags.append(value)

	def search(self, wanted):
		return self.conjunto.get(wanted.name, False) 


def add_class(t, elems, k, next_class):
	for one in t:
		if(not elems.search(one)):
			elems.append(one)
			k[id(one)] = next_class
			next_class += 1
			continue

		k1 = [one]+tree.post_order(one)
		for node in elems.tags:
			identicalNodes = False
			k2 = [node] + tree.post_order(node)
			if(compara_lista(k1, k2)):
				identicalNodes = True
				elems.append(one)
				k[id(one)] = k[id(node)]
				break

		if(not(identicalNodes)):
			elems.append(one)
			k[id(one)] = next_class
			next_class += 1
	return next_class

def get_classe_equivalencia(t1, t2):
	elems = Elem_Disjuntos()
	k = dict()
	next_class = 0
	post1 = tree.post_order(t1)
	post2 = tree.post_order(t2)
	next_class = add_class(post1, elems, k, next_class)
	add_class(post2, elems, k, next_class)
	return k

def compara_lista(node1, node2):
	if(len(node1)!=len(node2)):
		return False
	else:
		#TODO melelemsorar execucao do for
		for i in xrange(0, len(node1)):
			if( not tree.equal(node1[i], node2[i])):
				return False
	return True
