#!/bin/python
from lxml import etree
import file
import re

def lxml_parser(file_tree):
	return etree.parse(file_tree, parser=etree.HTMLParser())

def create(file_regex, file_xpath):
	file_regex = open(file_regex)
	file_xpath = open(file_xpath, "w")
	tree = lxml_parser(file_regex)
	xpaths = {}
	def _create_single(file_regex, wildcard):
		for elem in tree.xpath("//"+wildcard):
			xpath = tree.getpath(elem.getparent()) + "//*"
			xpath = re.sub("\[\d+\]","",xpath)
			if(xpaths.__contains__(xpath) == False):
				file_xpath.write(xpath+"\n")
			xpaths[xpath] = None

	_create_single(file_regex, "ponto")
	_create_single(file_regex, "interrogacao")
	_create_single(file_regex, "asterisco")
	_create_single(file_regex, "mais")

	file_xpath.close()
	file_regex.close()

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
		print("Erro", page_target)

