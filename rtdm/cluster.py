#!/usr/bin/env python
# encoding: utf-8

from identical_sub_trees import get_classe_equivalencia
from glob import glob
import file
import tree_lib as tree

class Cluster(object):

	"""Cluster Class definition"""

	def __init__(self, page1):
		self.pages = [page1]
		tree1, _ = tree.files_to_trees(page1, None)
		eq = len(get_classe_equivalencia(tree1, None))
		tree1 = None
		self.medias = [eq]
		self.meio = 0
	
	def add(self, page, class_eq):
		self.pages.append(page)
		self.medias.append(class_eq)


	def __repr__(self):
		print(self.pages)
		print(self.medias)
		print(meio)

def cal_classe_equiv(cluster, page):
	tree1, _ = tree.files_to_trees(page, None)
	class_eq = get_classe_equivalencia(tree1, None)
	meio = cluster.medias[ cluster.meio ] 
	tree1 = None
	tree2 = None
	lim = 100
	return len(class_eq), (class_eq == meio or class_eq == lim + meio or class_eq == lim - meio)
	
# Algoritmo de Clustering

_, paths = file.get_path()
for path in paths:
	pages = glob(path.strip() + "*.html")
	c = Cluster(pages.pop())
	clusters = [c]
	for page in pages:
		agrupado = False
		for cluster in clusters:
			qtd , mesma_class = cal_classe_equiv(cluster, page)
			if(mesma_class):
				agrupado = True
				cluster.add(page, qtd)
				break
			if(agrupado == False):
				clusters.append(Cluster(page))
