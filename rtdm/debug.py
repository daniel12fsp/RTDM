#Para debug 

import file
import rtdm

path = "/media/doc/home/doc/2013/academico/project/Implementacao/rtdm/rtdm/teste/"
pages = file.list_sorted_pages(path)

print("#"*50)
print(" page(0,1)")
a = rtdm.calc_similaridade(pages[0], pages[1])
print("."*50)
print(" page(1,0)")
b = rtdm.calc_similaridade(pages[1], pages[0])
print(a, b)

