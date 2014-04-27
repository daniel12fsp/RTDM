#!/bin/python
from lxml import etree
import file
import re
import mapping
from unidecode import unidecode
import json
try:
       import html.parser
except:
       import HTMLParser



def lxml_parser(file_tree):
	return etree.parse(file_tree, parser=etree.HTMLParser(encoding="UTF-8"))

def create(filename_regex, file_xpath):
	file_regex = open(filename_regex)
	page_regex = open(filename_regex).read()
	file_xpath = open(file_xpath, "w")
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
	#_create_single(page_regex, "interrogacao", 2)

	lca = fusion_xpath(xpaths)
	print("O xpath escolhido pra extracao")
	print(lca)
	file_xpath.write(lca + "\n")
	file_xpath.close()
	file_regex.close()
	return lca


def fusion_xpath(xpaths):
	print(xpaths)
	xpaths = xpaths.items()
	xpath_max_len = max(xpaths, key = lambda x : len(x[0]))
	xpath_max_0 = max(xpaths, key = lambda x : x[0])
	xpath_max_1 = max(xpaths, key = lambda x : x[1])
	lca = xpath_max_1[0]
	lca = xpath = re.sub("\[\d+\]","",lca)
	print("xpath_max_len", xpath_max_len)
	print("xpath_max_0(Key)", xpath_max_0)
	print("xpath_max_1(Valor)", xpath_max_1)
	return lca + "//*"
"""
def define_lca(file_xpath, page_target):
	file_xpath = open(file_xpath)
	page_target = open(page_target)
	tree = lxml_parser(page_target)
	txt = file_xpath.readlines()
	xpath = txt[0]
	tags = tree.xpath(xpath[:-1])
	result = []
	if(tags != []):
		freq = {}
		for tag in tags:
			if(tag.text  and re.search("\w",tag.text)):
				xpath_tag = re.sub("\[\d+\]","", tree.getpath(tag.getparent()))
				result.append(tag)
				if(freq.get(xpath_tag)):
					freq[xpath_tag] = freq[xpath_tag] + 1
				else:
					freq[xpath_tag] = 1

	lca = max(freq.items(), key = lambda x : x[1])[0]
	file_xpath.close()
	page_target.close()
	return lca + "//*"
"""

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
				parser = html.parser.HTMLParser()	
				value = re.sub("\s{2,}", "", tag.text)
				value = unidecode(str(value)).lower()
				value = parser.unescape(value)
				if(tag.getprevious() == None):
					key = value
				else:
					attrs[key] = [value]
		
		file_json.write("""{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True)))
	except:
		print(lca)
		print("Erro", page_target, "Error")
