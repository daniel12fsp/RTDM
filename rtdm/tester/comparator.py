#!/bin/python
import itertools
import json

file1 = open("/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/ColetaUFAM/ColetaNova/notebooks/submarino_notebook/data.json").read().splitlines()
gabarito = open("/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/wrapper_manual/submarino/jsao.json").read().splitlines()

erro = 0
def float_division(a, b):
	return a / float(b)

precisao_geral = 0
revocacao_geral = 0
for line1, line2 in zip(file1, gabarito):

	xpath = json.loads(line1)
	gab = json.loads(line2)

	attr1 = xpath["atributos"]
	attr2 = gab["atributos"]
	acertos = 0

	for one_attr in attr1.keys():
		if(attr2.get(one_attr) and attr2[one_attr] == attr1[one_attr]):	
			acertos += 1
	
	precisao = float_division(acertos, len(attr1))
	revocacao = float_division(len(attr2),len(attr1))

	precisao_geral += precisao
	revocacao_geral += revocacao

	print("id:%9s, acertos:%2d, precisao:%3f, revocacao:%3f, len attr1(xpath):%2d, len attr2(gab):%d" 
		% (xpath['id'], acertos, precisao, revocacao, len(attr1), len(attr2)))

print("Informações Gerais")
print("Precisao", float_division(precisao_geral, len(gabarito)))
print("Revocacao", float_division(revocacao_geral, len(gabarito)))



