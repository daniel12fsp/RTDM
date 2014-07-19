#!/bin/python
import numpy as np
import file
import rtdm
import sys
"""

A execucao deste modulo ocorre no interpretador python alternativo(pypy, nao python) por
questoes de velocidade em recusao do modulos

exemplo

a = np.array( [ ( 1, 1, 1, 1),
				( 1, 1, 1, 1),
				( 1, 1, 1, 1)], dtype=np.uint)

"""

path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_sites/algumas_paginas_simples/1/"
pages = file.list_sorted_pages(path)
#print(" ."*len(pages))
for i in range(0, len(pages)):
	print(pages[i])
	matrix[i][i] = 0
	#for j in range(i + 1, len(pages)):
	print "",
	for j in range(0, len(pages)):
		#print ".",
		#sys.stdout.flush()
		matrix[i][j] = rtdm.calc_similaridade(pages[i], pages[j])

np.savetxt(path + 'data.txt', matrix)
