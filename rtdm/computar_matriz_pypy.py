#!/bin/python
import numpy as np
import file
import rtdm
import sys
from itertools import product
from time import gmtime, strftime

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


path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_sites/algumas_paginas_simples/"
#path = "/home/azureuser/algumas_paginas_simples/"


pages = file.list_sorted_pages(path)
indice = range(len(pages))
matrix = np.zeros(shape=(len(pages),len(pages)), dtype=np.uint)
#par_pags = filter(lambda x: x[0] < x[1]  ,product(pages, pages)) # [(pag1,pag2)...]
par_pags = product(indice, indice) # [(pag1,pag2)...]
"""

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    future_result = [ executor.submit(calc_rtdm, i, j, pages) for (i, j) in par_pags]
"""
name = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(name)

from joblib import Parallel, delayed
resultados = Parallel(n_jobs=-1, backend="multiprocessing")(delayed(calc_rtdm)(i, j, pages) for (i, j) in par_pags)

for r in resultados:
	i, j, op = r
	matrix[i][j] = op



name = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print(name)
np.savetxt(path + "matriz_" + name + ".txt", matrix)
