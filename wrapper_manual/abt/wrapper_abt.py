#!/bin/python
import re
import bs4
from unidecode import unidecode
import json
import os
import glob
import html
import sys
import html.parser 
def wrapper(filename):
	page =  open(filename, "r").read()
	try:
		result = re.search('Specifications:(.*?)Begin accessories', page, re.S)
		ficha = result.group(0)
		ficha = html.parser.HTMLParser().unescape(ficha)
		ficha = unidecode(ficha).lower()
		ficha = re.sub("\s{2,}|\n","", ficha)
		dados = []
		dados += re.findall("<li>.*?<b>(.*?)</b>(.*?)</li>", ficha, re.S)
		dados += re.findall("<dt.*?>(.*?)</dt>.*?<dd.*?>(.*?)</dd>", ficha, re.S)
	except:
		return None
	return dados

def format_data(data):
	data = re.sub(r"<.*?>","", data)
	data = re.sub("^\W*","",data)
	data = re.sub("\W*$","",data)
	return data

def out_json(filename):
	
	dados = wrapper(filename)
	attrs = {}
	if(dados):
		for attr,value in dados:
			attr = format_data(attr)
			value = format_data(value)
			if(attr!=""):
				attrs[attr] = [value]
		
	id_file =	re.findall("/(\d+)\.html",filename)[0]
	return """{"id": %s, "atributos": %s}\n""" % (id_file,json.dumps(attrs, sort_keys=True))


folder = '/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_sites/abt_notebooks/'

jsao = open(folder + "json_wrapper.json","w")
files = sorted(glob.glob(folder + '*.html'))

for filename in files:
	jsao.write(out_json(filename))
jsao.close()
