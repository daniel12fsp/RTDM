#Para debug 

import file
import rtdm
import tree_lib

path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_sites/algumas_paginas_simples/1/"
pages = file.list_sorted_pages(path)

t0, t1 = tree_lib.files_to_trees(pages[0], pages[1])

print("#"*50)
print(" page(0,1)")
a = rtdm.calc_similaridade(pages[0], pages[1])
print("."*50)
print(" page(1,0)")
b = rtdm.calc_similaridade(pages[1], pages[0])
print(a, b)


"""
def teste(t0, t1, m0, m1):
	mt0 = tree_lib.search_md5_node(t0, m0)
	mt1 = tree_lib.search_md5_node(t1, m1)
	print(type(mt0), type(mt1))

	i1 = rtdm.insert(mt0, mt1)
	d1 = rtdm.delete(mt0, mt1)
	s1 = rtdm.replace(mt0, mt1)
		
	mt0 = tree_lib.search_md5_node(t1, m1)
	mt1 = tree_lib.search_md5_node(t0, m0)
	print(type(mt0), type(mt1))
	i2 = rtdm.insert(mt0, mt1)
	d2 = rtdm.delete(mt0, mt1)
	s2 = rtdm.replace(mt0, mt1)
	print(i1, d1, s1)
	print(i2, d2, s2)


teste(t0, t1, "02fc8a5a345df229aeff283c550ab924" ,"051f2e669704dbf1b761ac0f3e40b5cb")
"""
