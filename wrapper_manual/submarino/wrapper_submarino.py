#!/bin/python
import re
import bs4
from unidecode import unidecode
import json
import os
import glob
import html

def wrapper(filename):
	html =  open(filename, "r").read()
	result = re.search("""<section class="ficha-tecnica">\s*<article>((\n|.)+)</section>""", html)
	ficha =  bs4.BeautifulSoup(result.group(0)).section.prettify()
	ficha = unidecode(ficha)
	ficha = re.sub("\s{2,}","", ficha)
	dados = re.findall("<th>(.*?)</th>.*?<td>(.*?)</td>", ficha)

	return dados

def out_json(filename):
	
	dados = wrapper(filename)
	attrs = {}
	for attr,value in dados:
		value =  html.unescape(value.lower())
		attrs[attr.lower()] = [value.lower()]
	
	id_file =	re.findall("/(\d+)\.html",filename)[0]
	return """{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True))


folder = '/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/ColetaUFAM/ColetaNova/smartphones/submarino_smartphones/'

os.listdir(folder)

jsao = open("jsao.json","w")
files = sorted(glob.glob(folder+'*.html'))
for filename in files:
	jsao.write(out_json(filename))
jsao.close()
