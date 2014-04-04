#!/bin/python
from lxml import etree
xpath_file = open("/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/exemplo_tese/t4_t5.xpath")
page_target = "/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/exemplo_tese/t5.html"
tree = etree.parse(page_target)
print(tree)
for xpath in xpath_file.readlines():
	print(xpath[:-1])
	r = tree.xpath(xpath)
	print(r[0].text)
