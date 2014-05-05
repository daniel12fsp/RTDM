#!/bin/python
import itertools
import json



page = open("/media/doc/home/doc/2013/academico/project/Implementacao/rtdm-git/estatistica/submarino-notebooks/json_rtdm.json").read().splitlines()
gabarito = open("/media/doc/home/doc/2013/academico/project/Implementacao/rtdm-git/estatistica/submarino-notebooks/json_wrapper.json").read().splitlines()

erro = 0
def float_division(a, b):
	try:
		return a / float(b)
	except:
		return float("NaN")

precisao_geral = 0
revocacao_geral = 0
for line1, line2 in zip(page, gabarito):

	pag = json.loads(line1)
	gab = json.loads(line2)

	attr_pag = pag["atributos"]
	attr_gab = gab["atributos"]

	acertos = 0

	for one_attr in attr_pag.keys():
		if(attr_pag.get(one_attr) and attr_gab.get(one_attr)  and attr_pag[one_attr] == attr_gab[one_attr]):	
			acertos += 1
	
	precisao = float_division(acertos, len(attr_pag))
	revocacao = float_division(acertos, len(attr_gab))

	precisao_geral += precisao
	revocacao_geral += revocacao

	print("id:%9s, acertos:%2d, precisao:%3f, revocacao:%3f, len attr_pag(page):%2d, len attr_gab(gab):%d" 
		% (pag['id'], acertos, precisao, revocacao, len(attr_pag), len(attr_gab)))

precisao_final = float_division(precisao_geral, len(gabarito))
revocacao_final = float_division(revocacao_geral, len(gabarito))
print("Informações Gerais")
print("Precisao", precisao_final )
print("Revocacao", revocacao_final)
f1=(2*revocacao_final*precisao_final)/(precisao_final + revocacao_final)
print("f1",f1)


