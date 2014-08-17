#!/usr/bin/python
import numpy as np
from scipy.cluster.hierarchy import fclusterdata
import os
import sys
import file
import glob

"""
Parametros
    1 - o caminho com o nome do arquivo da matriz
    2 - O endereco onde estão as paginas
"""

def cluster_files(cluster_assignments,path,pages):
    n = cluster_assignments.max()
    for cluster_number in range(1, n + 1):
        newDir = path + str(cluster_number) + "/"
        pagesNewDir = np.array(np.where(cluster_assignments == cluster_number))[0]
        os.mkdir(str(newDir))
        for indexPage in pagesNewDir:
            oldPath = (pages[indexPage])
            #print("movendo a pagina",oldPath,"  ->  ",newDir + file.get_name_file_with_extension(pages[indexPage]))
            newPath = newDir + file.get_name_file_with_extension(pages[indexPage])
            os.rename(oldPath, newPath)

 # Make some test data.
dataFile = sys.argv[1]
matrix = np.loadtxt(str(dataFile))
matrix = matrix.astype(np.uint, copy=False)
data = np.array(matrix)

# Compute the clusters.
cutoff = 1.0
cluster_assignments = fclusterdata(data, cutoff)
num_clusters = cluster_assignments.max()
print("clusters",num_clusters)
path = sys.argv[2]
pages = []
pages = glob.glob(path + "*.html*")
pages = sorted(pages)
cluster_files(cluster_assignments,path,pages)
