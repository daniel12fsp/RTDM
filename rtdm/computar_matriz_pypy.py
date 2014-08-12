#!/bin/python
import numpy as np
import file
import rtdm
import sys
from itertools import product
from multiprocessing import Pool
from time import gmtime, strftime

"""

A execucao deste modulo ocorre no interpretador python alternativo(pypy, nao python) por
questoes de velocidade em recusao do modulos

exemplo

a = np.array( [ ( 1, 1, 1, 1),
				( 1, 1, 1, 1),
				( 1, 1, 1, 1)], dtype=np.uint)

"""


path = sys.argv[1]
print("iniciou", path)

pages = file.list_sorted_pages(path)
indice = xrange(len(pages))

par_pags = filter(lambda x: x[0] < x[1]  ,product(indice, indice)) # [(pag1,pag2)...]

def calc_rtdm(*arg):
	arg = arg[0]
	i = arg[0]
	j = arg[1]
	op = int(rtdm.dist_rtdm(pages[i], pages[j]))
	#op = int(rtdm.calc_similaridade(pages[i], pages[j]))
	print(i, j)
	return	i, j, op

p = Pool(maxtasksperchild = 1 )
future = p.map(calc_rtdm, ( (i, j) for (i, j) in par_pags) )


matrix = np.zeros(shape=(len(pages),len(pages)), dtype=np.int)
for i, j, op in future:
	matrix[i][j] = op

print("acabou", path)
time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
shop =  path.split("/")[-2]

np.savetxt(path + "matriz_" + shop + time + ".txt", matrix, fmt='%d')
