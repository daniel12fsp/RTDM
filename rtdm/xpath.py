#!/bin/python
from __future__ import print_function
from lxml import etree
import file
import re
import mapping
from unidecode import unidecode
import json
import xml.sax.saxutils as saxutils



def lxml_parser(file_tree):
	return etree.parse(file_tree, parser=etree.HTMLParser(encoding="utf8"))

def create(regex):

	page_regex = open(regex)
	tree = lxml_parser(page_regex)
	xpaths = {}
	def _create_single(page_regex, wildcard):
		for elem in tree.xpath("//" + wildcard):
			xpath = tree.getpath(elem.getparent())
			#TODO
			"""
				Criar os padroes de forma estatica
			"""
			xpath = re.sub("\[\d+\]","", xpath)
			if(xpaths.get(xpath) == None):
				xpaths[xpath] = 0
			xpaths[xpath] = xpaths[xpath] + int(elem.text) + 1
			

	_create_single(page_regex, "ponto")
	_create_single(page_regex, "interrogacao")

	#print(xpaths)

	xpaths = xpaths.items()

	try:
		
		"""
			As tres linhas a seguim serao tiradas
			servem como comparacao
		"""
		xpath_max_1 = max(xpaths, key = lambda x : x[1])
		lca = xpath_max_1[0]
		lca = xpath = re.sub("\[\d+\]","",lca)
		print(lca + "//*")
		'''
		xpath_max_len = max(xpaths, key = lambda x : len(x[0]))
		xpath_max_0 = max(xpaths, key = lambda x : x[0])

		print("xpath_max_len" + str(xpath_max_len))
		print("xpath_max_0(Key)" + str(xpath_max_0))
		print("xpath_max_1(Valor)" + str(xpath_max_1))
		'''
		"""
		Operacao custosa retire em futuro proximo
		
		ordem = list(xpaths)
		ordem.sort(key = lambda x: x[1], reverse = True)
		for (xp, qtd) in ordem:
			xp = re.sub("\[\d+\]","",xp)
			print(xp, qtd)
		"""

		print("#################")
		page_regex.close()
	except:
		print("Com as paginas informadas nao foi possivel gerar o xpath")
		return "xpath_erro"

	return lca + "//*"


def remove_espacos_acentos(data):
	data = re.sub("(\t|\r|\n)","",data)
	data = re.sub("^ *","",data)
	data = re.sub(" *$","",data)
	data = unidecode(unicode(data)).lower()
	data = saxutils.unescape(data)
	return data
	
#Modificar
def extraction(lca, page_target, id_file, file_json):
	page_target = open(page_target)
	tree = lxml_parser(page_target)
	page_target.close()
	attrs = {}
	#lca_path = lca[:-4]
	for tag in tree.xpath(lca):
		xpath_tag = re.sub("\[\d+\]","", tree.getpath(tag.getparent()))
		if(tag.text):
			value = re.sub("\s{2,}", "", tag.text)
			if(tag.getprevious() == None):
				key = remove_espacos_acentos(value)
				tmp = ""
				path_now = tree.getpath(tag.getparent())
				for sib in tree.xpath(path_now + "//text()")[1:]:
					if(sib!=tag.text):
						tmp += remove_espacos_acentos(sib)
				attrs[key] = [tmp]
	
	file_json.write("""{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True)))
	#print("Erro", page_target, "Error")
