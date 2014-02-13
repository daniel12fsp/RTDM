"""
Modulo onde contem todas as funcoes relacionadas com o Algoritmo de Classe de Equivalencia

Funcoes

	get_classe_equivalencia
		add_class

"""
import tree_lib as tree

def get_classe_equivalencia(t1, t2):
	h = []
	k = dict()
	next_class = 0

	def add_class(t, h, k, next_class):
		for one in t:
			if(not one.name in [i.name for i  in h]):
				h += [one]
				k[id(one)] = next_class
				next_class += 1
				continue

			k1 = [one]+tree.post_order(one)
			for node in h:
				identicalNodes = False
				k2 = [node]+tree.post_order(node)
				if(compara_lista(k1, k2)):
					identicalNodes = True
					h += [node]
					k[id(one)] = k[id(node)]
					break

			if(not(identicalNodes)):
				h += [one]
				k[id(one)] = next_class
				next_class += 1
		return h, k, next_class

	post1 = tree.post_order(t1)
	post2 = tree.post_order(t2)
	h, k, next_class = add_class(post1, h, k, next_class)
	h, k, next_class = add_class(post2, h, k, next_class)
	return k

def compara_lista(node1, node2):
	if(len(node1)!=len(node2)):
		return False
	else:
		for i in range(0, len(node1)):
			if( not tree.equal(node1[i], node2[i])):
				return False
	return True
