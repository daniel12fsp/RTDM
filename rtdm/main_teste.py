import main_rtdm as main
import re
import os
from distutils.dir_util import mkpath as mkpath
file_folders = os.path.dirname(os.path.realpath(__file__)) + "/../links_rtdm.txt"
folders = open(file_folders, "r").readlines()
i = 0
for folder in folders:
	print(folder)
	i += 1
	s = re.search("(.*)/(.*?)/$",folder)
	path_pai, loja = s.groups()
	path_test = path_pai + "/teste/" + loja + "/"
	path_log = path_test + "/log/"
	path_pages = path_pai + "/"+loja +"/"

	mkpath(path_test)
	mkpath(path_log)
	main.prepare_vars(path_pages, path_test, path_log)
	main.exec_rtdm()
