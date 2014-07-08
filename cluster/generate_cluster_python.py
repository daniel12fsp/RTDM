"""

A execucao deste modulo ocorre no interpretador python padrao(python, nao pypy) por
questoes de compatibilidade com biblioteca scipy.

"""


"""
data  = [
				[1,1,1],
        [1,1,1],
        [1,1,1],
        [2,2,2],
        [2,2,2],
        [2,2,2],
        [3,3,3],
        [3,3,3],
        [3,3,3]
				]

from scipy import spatial
import scipy.cluster.hierarchy as sch
distance = spatial.distance.pdist(data)

#Performs hierarchical/agglomerative clustering on the condensed distance matrix y.
linkage = sch.linkage(distance, method="complete")
#Forms flat clusters from the hierarchical clustering defined by the linkage matrix Z.
cluster = sch.fclusterdata(linkage, 0.1 , criterion="distance")
#Returns the root nodes in a hierarchical clustering
print(cluster)
tree  = sch.ClusterNode(cluster)

"""
