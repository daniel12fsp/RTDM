import main_rtdm as main
import re
import os
from distutils.dir_util import mkpath as mkpath
file_folders = os.path.dirname(os.path.realpath(__file__)) + "/../links_rtdm.txt"
folders = open(file_folders, "r").readlines()

s = re.search("(.*/).*?/$",folders[0])
path_pai= s.group(1)
path_test = path_pai + "teste/"
mkpath(path_test)
file_erro = open(path_test + "erro.txt", "w", 0)

for folder in folders:
	print(folder)
	s = re.search(".*/(.*?)/$",folder)
	loja = s.group(1)
	path_test_loja = path_test + loja + "/"
	path_log = path_test_loja + "/log/"
	mkpath(path_log)
	main.prepare_vars(folder.strip(), path_test_loja, path_log)
	main.exec_rtdm(file_erro)

file_erro.close()
