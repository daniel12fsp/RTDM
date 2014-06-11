#!/usr/bin/env python
# encoding: utf-8

from identical_sub_trees import get_classe_equivalencia
from glob import glob
import file
import tree_lib as tree
import re
import os

class Cluster(object):

	"""Cluster Class definition"""

	def __init__(self, i, path ,page1):
		i = str(i)
		try:
			os.mkdir(path + i)
		except:
			pass
		self.pages = [page1]
		self.path = path + i
		tam = cal_qtd_tags(page1)
		tree1 = None
		self.medias = [tam]
		self.soma = tam 
		self.meio = 0
	
	def add(self, page, class_eq):
		result = re.search(".*/(.*?)$",page)
		result = result.group(1)
		os.rename(page, self.path +"/" + result)

		self.pages.append(page)
		self.medias.append(class_eq)
		self.soma += class_eq
		self.meio = 0

	def entra_grupo(self, qtd_page):
		meio = self.medias[ self.meio ] 
		lim = 100
		return (qtd_page > lim - meio  and qtd_page < lim + meio)


	def __repr__(self):
		print([i for i in self.pages])
		print(self.medias)
		print(self.meio)
		return ""

def cal_classe_equiv(page):
	tree1, _ = tree.files_to_trees(page, None)
	class_eq = get_classe_equivalencia(tree1, None)
	tree1 = None
	return len(class_eq)


def cal_qtd_tags(page):
	page = open(page)
	result = re.findall('<.*?>', page.read(),re.DOTALL)
	page.close()
	return len(result)

# Algoritmo de Clustering

_, paths = file.get_path()
clusters = []

for path in paths:
	path = path.strip()
	pages = glob( path + "*.html")
	c = Cluster(len(clusters), path, pages.pop())
	clusters.append(c)
	for page in pages:
		print(page)
		agrupado = False
		qtd = cal_qtd_tags(page)
		for cluster in clusters:
			if(cluster.entra_grupo(qtd)):
				agrupado = True
				cluster.add(page, qtd)
				break
		if(agrupado == False):
			clusters.append(path, Cluster(len(clusters), path, page))

