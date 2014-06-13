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

	def __init__(self, i, path ,page):

		self.path = path + str(i) + "/"
		try:
			os.mkdir(self.path)
		except:
			pass

		tam = cal_qtd_tags(page)
		self.quant = 0
		self.soma = 0 
		self.meio = 0
		self.add(page, tam)
	
	def add(self, page, qtd):
		name_page = name_from_path(page)
		os.rename(page, self.path + name_page)
		self.soma += qtd
		self.meio = 0
		self.quant += 1

	def entra_grupo(self, qtd_page):
		meio = int(self.soma / self.quant)
		lim = 100
		return (qtd_page > lim - meio  and qtd_page < lim + meio)

	def __repr__(self):
		print([i for i in self.pages])
		print(self.medias)
		print(self.meio)
		return ""

def name_from_path(page):
	result = re.search(".*/(.*?)$",page)
	return result.group(1)

def remove_tag_re(html):
	#tag script
	tag_re = "(?is)(<script[^>]*>)(.*?)(</script>)"
	html = re.sub(tag_re, "", html)
	#tag comentario html
	tag_re = "<!--.*?-->"
	html = re.sub(tag_re, "", html)
	tags = ["style", "link", "meta", "noscript"]
	for tag in tags:
		tag_re = "<%s[^>]*>[^>]*>" % (tag)
		html = re.sub(tag_re, "", html)
	return html

def cal_classe_equiv(page):
	tree1, _ = tree.files_to_trees(page, None)
	class_eq = get_classe_equivalencia(tree1, None)
	tree1 = None
	return len(class_eq)

def cal_qtd_tags(page):
	page = open(page)
	html = page.read()
	page.close()
	html = remove_tag_re(html)
	result = re.findall('<.*?>', html, re.DOTALL)
	return len(result)

def cal_qtd_tags(page):
	page = open(page)
	html = page.read()
	page.close()
	html = remove_tag_re(html)
	result = re.findall('<.*?>', html, re.DOTALL)
	return len(result)

# Algoritmo de Clustering

_, paths = file.get_path()
clusters = []

for path in paths:
	path = path.strip()
	pages = glob( path + "*html*")
	c = Cluster(len(clusters), path, pages.pop())
	clusters.append(c)
	for page in pages:
		agrupado = False
		qtd = cal_qtd_tags(page)
		for cluster in clusters:
			if(cluster.entra_grupo(qtd)):
				agrupado = True
				cluster.add(page, qtd)
				break
		if(agrupado == False):
			clusters.append(Cluster(len(clusters), path, page))

