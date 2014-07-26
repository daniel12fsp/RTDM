#Para debug 

import file
import rtdm
import tree_lib
from bs4 import BeautifulSoup

path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_sites/algumas_paginas_simples/"
#path = "/home/azureuser/algumas_paginas_simples/"
pages = file.list_sorted_pages(path)
a = rtdm.calc_similaridade(pages[0], pages[1])
print(a)
