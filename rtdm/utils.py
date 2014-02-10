"""
	Modulo responsavel por ter as funcoes auxiliares

"""

"""
	rtdm.py
"""

def get_elem(lista, index):
	try:
		return lista[index]
	except:
		return None

def exist_elem(lista, index):
	return 	get_elem(lista, index) is not None
