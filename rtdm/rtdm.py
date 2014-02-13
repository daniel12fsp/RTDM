from utils import get_elem, exist_elem
import os
import tree_lib as tree
from mapeamento import mapeamento_array, get_list, mapeamento_node

def delete(t1, t2):
	i  = 0
	c1 = tree.get_children(t1)
	c2 = tree.get_children(t2)
	custo_delete = 0
	if(t1 is not None and t2 is not None) and ( not tree.equal(t1,t2)):
		custo_delete += tree.length(t1)
		return custo_delete

	while(i < len(c1) and i < len(c2)):

		node1 = get_elem(c1, i)
		node2 = get_elem(c2, i)
		custo_delete += delete(node1, node2)
		i += 1
	if(len(c1)>0):
		for j in range(i, len(c1)):
			custo_delete += tree.length(get_elem(c1, j))
	return custo_delete

def insert(t1, t2):
	i  = 0
	c1 = tree.get_children(t1)
	c2 = tree.get_children(t2)
	custo_insert = 0
	if(t1 is not None and t2 is not None) and ( not tree.equal(t1,t2)):
		custo_insert += tree.length(t2)
		return custo_insert

	while(i < len(c1) and i < len(c2)):
		node1 = get_elem(c1, i)
		node2 = get_elem(c2, i)
		custo_insert += insert(node1, node2)
		i += 1

	if(i<len(c2)):
		for j in range(i, len(c2)):
			custo_insert += tree.length(get_elem(c2, j))
	return custo_insert


"""
	Funcao: replace_no_no

		Verifica somente se a raiz da subarvore eh diferente, caso afirmativo returna 1, se nao 0
"""
def replace_no_no(t1, t2):
	return 1 if not tree.equal(t1,t2) else 0

"""
	Funcao: replace_nos_t2

		Retorna o valor de todos os nos da subarvore t2
"""
def replace_nos_t2(t1, t2):
	r = 0
	for j in tree.get_children(t2):
			r += tree.length(j)
	return r
"""
	Funcao: replace_mesma_quantidade_elementos

		Retorna o valor de elementos iguais nas posicoes equivalentes nas arvores
"""
def replace_mesma_quantidade_elementos(t1, t2):
	i  = 0
	c1 = tree.get_children(t1)
	c2 = tree.get_children(t2)
	custo_replace = 0
	if(t1 is not None and t2 is not None) and not tree.equal(t1,t2):
		custo_replace += tree.length(t2)

	while(i < len(c1) and i < len(c2)):
		node1 = get_elem(c1, i)
		node2 = get_elem(c2, i)
		custo_replace += replace_mesma_quantidade_elementos(node1, node2)
		i += 1
	return custo_replace

"""
	Funcao: replace_choice(option)
		
		Define qual funcao de replace sera utilizada dentre estas:
			1 - replace_no_no
			2 - replace_nos_t2
			3 - replace_mesma_quantidade_elementos 
"""
def replace_choice(option):
	print("A opcao de replace foi: %s" % (option))
	global replace
	if(option==1):
		replace = replace_no_no
	elif(option==2):
		replace = replace_nos_t2
	elif(option==3):
		replace = replace_mesma_quantidade_elementos

def prepareRTDM(k_parament, log_parament):
	global k
	k = k_parament
	global log
	log = log_parament

def menor_operacao(d,i,s):
	res = []
	if(d >= i) and (s >= i):
		 res += ["i"]
	if(i >= d) and (s >= d):
		 res += ["d"]
	if(i >= s) and (d>= s):
		res += ["s"]
	return res
	
def RTDM(t1, t2):
	c1 = [t1]+t1.find_all(recursive=False)
	c2 = [t2]+t2.find_all(recursive=False)
	m = len(c1)
	n = len(c2)
	mape = []
	M = [[0 for x in range(n)] for x in range(m)]
	O = [[0 for x in range(n)] for x in range(m)]
	MAPE = [[None for x in range(n)] for x in range(m)]
	O[0][0]=["s"]
	MAPE[0][0] = (c1[0].name,c2[0].name)
	log.write("\n%d %d" % (m, n))

	for i in range(1, m):
		M[i][0] = M[i-1][0]+tree.length(c1[i])
		O[i][0] = ["d"]

	for j in range(1, n):
		M[0][j] = M[0][j-1]+tree.length(c2[j])
		O[0][j] = ["i"]

	aux = []
	for i in range(1, m):
		for j in range(1, n):
			aux_mape = None
			log.write("\n\n\tM[%d][%d](%s x %s)" % (i, j, c1[i].name, c2[j].name))
			d = (M[i-1][j]+delete(c1[i], c2[j]))
			d1 = delete(c1[i], c2[j])
			a = (M[i][j-1]+insert(c1[i], c2[j]))
			a1 = insert(c1[i], c2[j])
			s = M[i-1][j-1]
			s1 = 0
			aux = [] 
			if(tree.is_any_wildcard(c1[i],c2[j]) or k[id(c1[i])]==k[id(c2[j])] ):
				log.write("\nIguais %s %s" % ( c1[i].name, c2[j].name))
				M[i][j] = s
				O[i][j] = O[i-1][j-1]
				MAPE[i][j] = [get_list(c1[i])]
				continue
			elif(not tree.equal(c1[i],c2[j])):
				#aux += [[(c1[i].name, c2[j].name)]]
				log.write("\nSubst")
				s += replace(c1[i], c2[j])
				s1 = replace(c1[i], c2[j])

				if tree.is_leaf(c1[i]) and not tree.is_leaf(c2[j]):
					log.write("\nfolha")
					s += insert(c1[i], c2[j])

				elif tree.is_leaf(c2[j]) and not tree.is_leaf(c1[i]):
					log.write("\nfolha")
					s += delete(c1[i], c2[j])

			else:
				rtdm,_,aux_mape = RTDM(c1[i], c2[j])
				mape.insert(0,aux_mape)
				log.write("\nRecursao %f" % (rtdm))
				s += rtdm

			log.write("\n\tM[%d][%d](%s x %s)\ti:%d,d:%d,s:%d" % (i, j, c1[i].name, c2[j].name, a1, d1, s1))
			M[i][j] = min(d, a, s)
			O[i][j] = menor_operacao(d, a, s)
			MAPE[i][j] = mapeamento_node(aux_mape, c1[i].name, c2[j].name) 

	for x in range(0, m):
		log.write("\n"+str(M[x]))

	log.write("\n")
	for x in range(0, m):
		log.write("\n"+str(O[x]))
		
	log.write("\n")
	for x in range(0, m):
		log.write("\n"+str(MAPE[x]))
	log.write("\n")

	mape = [(c1[0].name,c2[0].name)] + mape #+ aux
	return M[m-1][n-1],M,mapeamento_array(MAPE,O,c1,c2)


