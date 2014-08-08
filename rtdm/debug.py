#Para debug 

import file
import rtdm
import tree_lib
from bs4 import BeautifulSoup
import timeit

path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/abt_notebooks/"
#path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/exemplo_tese/simples/"

#path = "/home/azureuser/algumas_paginas_simples/"
pages = file.list_sorted_pages(path)
"""
graphviz = GraphvizOutput()
graphviz.output_file = 'basic.png'

with PyCallGraph(output=graphviz):
"""
#a = rtdm.dist_rtdm(pages[0], pages[1])
#a = rtdm.calc_similaridade(pages[0], pages[1])
pages0 = pages[0]
pages1 = pages[1]
print(timeit.timeit("rtdm.dist_rtdm(\'" + pages0 + "\',\'" + pages1+ "\')", setup = "import rtdm", number=1))
print(timeit.timeit("rtdm.calc_similaridade(\'" + pages0 + "\',\'" + pages1+ "\')", setup =  "import rtdm", number =1))
