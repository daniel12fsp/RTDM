#!/bin/python
import re
import bs4
from unidecode import unidecode
import json
import os
import glob
import html
import sys
#<div id="descricao" class="descricao">(.|\n)*</div>
def wrapper(filename):
	page =  open(filename, "r").read()
	result = re.search('<div id="descricao" class="descricao">(.*?)<div id="footer">', page, re.S)
	ficha = result.group(0)
	ficha = unidecode(html.unescape(ficha)).lower()
	ficha = re.sub("\s{2,}|\n","", ficha)
	dados = re.findall("<dt.*?>(.*?)</dt>.*?<dd.*?>(.*?)</dd>", ficha, re.S)
	return dados

def remove_space(data):
	data = re.sub("^ ","",data)
	data = re.sub(" $","",data)
	data = re.sub(r"<.*?>","", data)
	return data

def out_json(filename):
	
	dados = wrapper(filename)
	attrs = {}
	for attr,value in dados:
		attrs[remove_space(attr)] = [remove_space(value)]
	
	id_file =	re.findall("/(\d+)\.html",filename)[0]
	return """{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True))


folder = '/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers/pontofrio_notebooks/'

jsao = open("/media/doc/home/doc/2013/academico/project/Implementacao/rtdm-git/estatistica/ponto-frio_notebooks/" + "json_wrapper.json","w")
files = sorted(glob.glob(folder+'*.html'))

for filename in files:
	jsao.write(out_json(filename))
jsao.close()
