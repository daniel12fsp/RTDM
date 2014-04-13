#!/bin/python
from lxml import etree
import file
import re
import mapping

def lxml_parser(file_tree):
	return etree.parse(file_tree, parser=etree.HTMLParser())

def create(filename_regex, file_xpath):
	file_regex = open(filename_regex)
	page_regex = open(filename_regex).read()
	#page_regex = mapping.promocao_curingas(page_regex)
	file_xpath = open(file_xpath, "w")
	tree = lxml_parser(file_regex)
	xpaths = {}
	def _create_single(page_regex, wildcard):
		for elem in tree.xpath("//"+wildcard):
			xpath = tree.getpath(elem.getparent()) + "//*"
			xpath = re.sub("\[\d+\]","",xpath)
			if(xpaths.__contains__(xpath) == False):
				xpaths[xpath] = 0
			xpaths[xpath] = xpaths[xpath] + 1
			

	_create_single(page_regex, "ponto")
	_create_single(page_regex, "interrogacao")
	_create_single(page_regex, "asterisco")
	_create_single(page_regex, "mais")

	xpaths = fusion_xpath(xpaths)

	for key in xpaths:
		print(key, xpaths[key])
		if(xpaths[key] > 5):
			file_xpath.write(key + "\n")
	file_xpath.close()
	file_regex.close()



def fusion_xpath(xpaths):
	keys_repeated = set()
	for key1 in xpaths:
		for key2 in xpaths:
			if(key1 != key2 and re.match(key1[:-2],key2 )):
				xpaths[key1] = xpaths[key1] + xpaths[key2]
				keys_repeated.add(key2)

	for key in keys_repeated:
		del xpaths[key]

	return xpaths	
			

def extraction(file_xpath, page_target, file_data):
	file_xpath = open(file_xpath)
	page_target = open(page_target)
	tree = lxml_parser(page_target)
	file_data = open(file_data,"w")
	for xpath in file_xpath.readlines():
		tags = tree.xpath(xpath[:-1])
		if(tags != []):
			for tag in tags:
				if(tag.text and re.search("\w",tag.text)):
					file_data.write(str((tag.tag,tag.text))+"\n")
	try:

		file_xpath.close()
		page_target.close()
		file_data.close()
	except:
		print("Erro", page_target, "Error")

