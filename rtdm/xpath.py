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
	print("O xpath escolhido pra extracao")
	for key in xpaths:
		#print(key, xpaths[key])
		print(key)
		file_xpath.write(key + "\n")
	file_xpath.close()
	file_regex.close()


def fusion_xpath(xpaths):

	descendents = {k: [] for k in xpaths.keys()}
	for key1 in xpaths:
		for key2 in xpaths:
			if(key1 != key2 and re.match(key1[:-2],key2 )):
				xpaths[key1] = xpaths[key1] + xpaths[key2]
				descendents[key1].append(key2)
		#print(key1, xpaths[key1])

	order = list(xpaths.items())
	order.sort(key = lambda x : x[1], reverse = True)
	last_div = order.pop(0)[0]
	elems = []
	for i in range(len(order)):
		(key,freq) = order[i]
		if(not re.search("div/$",key[:-2])):
			elems =  [(xpaths[key], key) for key in descendents[last_div]]
			elems.sort(reverse = True)
			break
		last_div = key
		del order[i]

	result = []
	print(elems)
	for _,k1 in elems:

		if(re.search("div/$", k1[:-2]) ):
			continue

		_add_xpath_unique(k1, result)

	if(len(result) <= 1):
		return [last_div]
	else:
		xpath = last_div + "[" + "self::"+re.findall("/(\w+)//\*$",result[0])[0]
		for i in result[1:]	:
			xpath += _generate_or(re.findall("/(\w+)//\*$", i)[0])
		xpath +="]//*"
		print(xpath)
		return [xpath]


def _add_xpath_unique(one, elems):
	found = 0
	for i in elems:	
		if(re.match(i[:-2], one)):
			found = 1
			break
	if(found == 0):
		elems.append(one)

def _generate_or(elem):
	return " | self::"+elem+" "
			

def extraction(file_xpath, page_target, file_data):
	try:
		file_xpath = open(file_xpath)
		page_target = open(page_target)
		tree = lxml_parser(page_target)
		file_data = open(file_data,"w")
		for xpath in file_xpath.readlines():
			tags = tree.xpath(xpath[:-1])
			if(tags != []):
				for tag in tags:
					if(tag.text  and re.search("\w",tag.text) and (True or tag.tag not in ["script", "a", "li", "lo", "option", "em","b","strong","label","fieldset","ul", "select","small"])):
						file_data.write(str((tag.tag,tag.text))+"\n")
						#file_data.write(str((tree.getpath(tag),tag.tag,tag.text))+"\n")
			file_xpath.close()
			page_target.close()
			file_data.close()
	except:
		print("Erro", page_target, "Error")

#ponto ["script", "a", "p", "li", "lo", "option", "em", "div", "span","b","strong","label","fieldset","ul", "select"])
#luiza == americanas ["script", "a", "li", "lo", "option", "em","b","strong","label","fieldset","ul", "select","small"]


