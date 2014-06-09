import main_rtdm as main
import re
import os
from distutils.dir_util import mkpath as mkpath
import file
#from glob import glob

path_logs, folders =  file.get_path()
file_erro = open(path_logs + "erro.txt", "w", 0)

for folder in folders:
	print(folder)
	s = re.search(".*/(.*?)/.*?",folder)
	loja = s.group(1)
	path_logs_loja = path_logs + loja + "/"
	path_log = path_logs_loja + "/log/"
	mkpath(path_log)
	main.prepare_vars(folder.strip(), path_logs_loja, path_log)
	main.exec_rtdm(file_erro)

file_erro.close()
