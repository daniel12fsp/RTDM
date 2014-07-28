#Para debug 

import file
import rtdm
import tree_lib
from bs4 import BeautifulSoup
from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/abt_notebooks/"
#path = "/home/azureuser/algumas_paginas_simples/"
pages = file.list_sorted_pages(path)
"""
graphviz = GraphvizOutput()
graphviz.output_file = 'basic.png'

with PyCallGraph(output=graphviz):
"""
a = rtdm.calc_similaridade(pages[0], pages[1])
print(a)
