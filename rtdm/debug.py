#Para debug 

import file
import rtdm
import tree_lib
from bs4 import BeautifulSoup
import timeit
"""
path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/abt_notebooks/"
#path = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/exemplo_tese/simples/"

#path = "/home/azureuser/algumas_paginas_simples/"
pages = file.list_sorted_pages(path)
"""
pages0 = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/pontofrio_bem_simples/8254798.html"
pages1 = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/pontofrio_bem_simples/23846640.html"
pages1 = "/media/doc/home/doc/2013/academico/project/Implementacao/paginas_html/ColetaUFAM/ColetaNova/wrappers_base/pontofrio_bem_simples/8254798_23846640.regex"
print(rtdm.create_regex(pages0 , pages1))
#print(timeit.timeit("rtdm.calc_similaridade(\'" + pages0 + "\',\'" + pages1+ "\')", setup = "import rtdm", number=1))
