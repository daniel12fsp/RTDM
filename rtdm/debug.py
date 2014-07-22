#Para debug 

import file
import rtdm
import tree_lib
from bs4 import BeautifulSoup

path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_sites/algumas_paginas_simples/"
path = "/home/azureuser/algumas_paginas_simples/"
#pages = file.list_sorted_pages(path)
#print(len(pages))

#t0, t1 = tree_lib.files_to_trees(pages[0], pages[1])
"""
print("#"*50)
print(" page(0,1)")
a = rtdm.calc_similaridade(pages[0], pages[1])
print("."*50)
print(" page(1,0)")
b = rtdm.calc_similaridade(pages[1], pages[0])
print(a, b)


"""
def teste(t0, t1, m0, m1):
	mt0 = """
<tr>
 <td style="background: #f5f5f5">
  <strong>
   Operating Platform
  </strong>
 </td>
</tr>
"""
	mt1 = """
<tr>
 <td style="background: #f5f5f5">
  <strong>
   Operating Platasdform
  </strong>
 </td>
 <td style="background: #f5f5f5">
	Linux the best
 </td>
</tr>
"""
	mt0 = BeautifulSoup(mt0)
	mt1 = BeautifulSoup(mt1)
	print(mt0.prettify().encode('utf-8'))
	print("*"*80)
	print(mt1.prettify().encode('utf-8'))
	i1, d1, s1 = rtdm.op_ins_del_rep(mt0, mt1)

	a = mt0
	mt0 = mt1
	mt1 = a
	print(type(mt0), type(mt1))
	i2, d2, s2 = rtdm.op_ins_del_rep(mt0, mt1)
	print(i1, d1, s1)
	print(i2, d2, s2)


teste(None, None, "02fc8a5a345df229aeff283c550ab924" ,"051f2e669704dbf1b761ac0f3e40b5cb")

