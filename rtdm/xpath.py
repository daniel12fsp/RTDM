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
	return etree.parse(file_tree, parser=etree.HTMLParser(encoding="UTF-8"))

def create(file_log, filename_regex, file_general_xpath):

	file_regex = open(filename_regex)
	page_regex = open(filename_regex).read()
	tree = lxml_parser(file_regex)
	xpaths = {}
	def _create_single(page_regex, wildcard, peso):
		for elem in tree.xpath("//"+wildcard):
			xpath = tree.getpath(elem.getparent())
			#xpath = tree.getpath(elem.getparent()) + "//*"
			xpath = re.sub("\[\d+\]$","",xpath)
			if(xpaths.__contains__(xpath) == False):
				xpaths[xpath] = 0
			xpaths[xpath] = xpaths[xpath] + 1*peso
			

	_create_single(page_regex, "ponto", 1)
	_create_single(page_regex, "interrogacao", 1)

	print(xpaths, file = file_log)
	xpaths = xpaths.items()

	try:
		"""
			As tres linhas a seguim serao tiradas
			servem como comparação
		"""
		xpath_max_len = max(xpaths, key = lambda x : len(x[0]))
		xpath_max_0 = max(xpaths, key = lambda x : x[0])
		xpath_max_1 = max(xpaths, key = lambda x : x[1])
		lca = xpath_max_1[0]
		lca = xpath = re.sub("\[\d+\]","",lca)
		print("xpath_max_len" + str(xpath_max_len), file = file_log)
		print("xpath_max_0(Key)" + str(xpath_max_0), file = file_log)
		print("xpath_max_1(Valor)" + str(xpath_max_1), file = file_log)
		"""
		Operacao custosa retire em futuro proximo
		"""
		ordem = list(xpaths)
		ordem.sort(key = lambda x: x[1], reverse = True)
		print("len ordem", len(ordem))
		for item in ordem:
			print(item, file = file_general_xpath)

		print("#################", file = file_general_xpath)

		file_regex.close()
	except:
		print("except")
		print("Com as paginas informadas nao foi possivel gerar o xpath", file = file_log)
		return "xpath_erro"
	return lca + "//*"


def remove_space(data):
	data = re.sub("^ ","",data)
	data = re.sub(" $","",data)
	return data
	

def extraction(lca, page_target, id_file, file_json):
	page_target = open(page_target)
	tree = lxml_parser(page_target)
	page_target.close()
	attrs = {}
	#lca_path = lca[:-4]
	try:
		for tag in tree.xpath(lca):
			xpath_tag = re.sub("\[\d+\]","", tree.getpath(tag.getparent()))
			if(tag.text):
				value = re.sub("\s{2,}", "", tag.text)
				value = unidecode(str(value)).lower()
				value = saxutils.unescape(value)
				if(tag.getprevious() == None):
					key = remove_space(value)
				else:
					attrs[key] = [remove_space(value)]
		
		file_json.write("""{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True)))
	except:
		print(lca)
		print("Erro", page_target, "Error")
