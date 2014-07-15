#!/bin/python
import numpy as np
import file
import rtdm
"""

A execucao deste modulo ocorre no interpretador python alternativo(pypy, nao python) por
questoes de velocidade em recusao do modulos

exemplo

a = np.array( [ ( 1, 1, 1, 1),
				( 1, 1, 1, 1),
				( 1, 1, 1, 1)], dtype=np.uint)

"""

path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_sites/alguns_pontofrio/"
pages = file.list_sorted_pages(path)
matrix = np.zeros(shape=(len(pages),len(pages)), dtype=np.uint)
i = -1
for i in range(0, len(pages)):
	print(pages[i])
	matrix[i][i] = 0
	for j in range(i + 1, len(pages)):
		matrix[i][j] = rtdm.calc_similaridade(pages[i], pages[j])

np.savetxt('data.txt', matrix)
