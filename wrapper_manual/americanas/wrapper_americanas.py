#!/bin/python3
import re
import bs4
from unidecode import unidecode
import json
import os
import glob

def wrapper(filename):
	html =  open(filename, "r", encoding="utf8").read()
	result = re.findall("""<dl>(.+?)</dl>""", html, re.S)
	try:
		ficha =  result[0]
		ficha = unidecode(ficha)
		ficha = re.sub("\s{2,}","", ficha)
		dados = re.findall("<dt>(.+?)</dt>.*?<dd.+?>(.+?)</dd>", ficha)
		return dados
	except:
		return ""
	

	

def out_json(filename):
	dados = wrapper(filename)
	if (dados):
		attrs = {}
		for attr,value in dados:
			attrs[attr.lower()] = [value.lower()]
		
		id_file =	re.findall("/(\d+)\.html",filename)[0]
		return """{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True))


#folder = '/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/ColetaUFAM/ColetaNova/notebooks/submarino_notebook/'
folder = '/home/ervili/Neemu/ColetaUFAM/ColetaNova/notebooks/americanas_notebook/'
os.listdir(folder)

jsao = open(folder + "gabarito.json","w")
for filename in glob.glob(folder+'*.html'):
	extraction = out_json(filename)
	if(extraction):
		jsao.write(extraction)
print("finalizou")
jsao.close()
