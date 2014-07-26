#!/bin/python
import numpy as np
import file
import rtdm
import sys
from itertools import product
from time import gmtime, strftime
from joblib import Parallel, delayed

"""

A execucao deste modulo ocorre no interpretador python alternativo(pypy, nao python) por
questoes de velocidade em recusao do modulos

exemplo

a = np.array( [ ( 1, 1, 1, 1),
				( 1, 1, 1, 1),
				( 1, 1, 1, 1)], dtype=np.uint)

"""

def calc_rtdm(i, j, pages):
	op = rtdm.calc_similaridade(pages[i], pages[j])
	return i, j, op


path = sys.argv[1]
print(path)

pages = file.list_sorted_pages(path)
indice = range(len(pages))
matrix = np.zeros(shape=(len(pages),len(pages)), dtype=np.uint)
par_pags = filter(lambda x: x[0] < x[1]  ,product(indice, indice)) # [(pag1,pag2)...]
#par_pags = product(indice, indice) # [(pag1,pag2)...]

name = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(name)

resultados = Parallel(n_jobs=-1, backend="multiprocessing")(delayed(calc_rtdm)(i, j, pages) for (i, j) in par_pags)

for r in resultados:
	i, j, op = r
	matrix[i][j] = op


name = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(name)
np.savetxt(path + "matriz_" + name + ".txt", matrix)
