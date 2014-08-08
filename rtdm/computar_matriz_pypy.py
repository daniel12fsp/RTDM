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
path = sys.argv[1]
print(path)

pages = file.list_sorted_pages(path)
indice = xrange(len(pages))
matrix = np.zeros(shape=(len(pages),len(pages)), dtype=np.int)
par_pags = filter(lambda x: x[0] < x[1]  ,product(indice, indice)) # [(pag1,pag2)...]
#par_pags = product(indice, indice) # [(pag1,pag2)...]

name = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(name)
def calc_rtdm(i, j, pages):
	matrix[i][j] = rtdm.dist_rtdm(pages[i], pages[j])
	print(i,j)

Parallel(n_jobs=-2)(delayed(calc_rtdm)(i, j, pages) for (i, j) in par_pags)

name = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(name)
np.savetxt(path + "matriz_" + name + ".txt", matrix)
