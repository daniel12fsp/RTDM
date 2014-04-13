import subprocess
import os
import random

def execute_bash(command):
	## call date command ##
	proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
	(output, err) = proc.communicate()
	return output

def generate_list_from_cmd(path_dir):
	command = "ls " + path_dir +"*.html -lS"
	tmp = execute_bash(command).splitlines()
	tmp.pop(0)
	files = []
	for one in tmp:
		split = one.split()
		length = int(split[4])
		name = split[8]
		files.append((length, name))


	middle = int((files[0][0] + files[-1][0])/2)
	result = []
	for one in files:
		if one[0]>= middle:
			result.append(one[1])
		else:
			break
	return result

def pick_elems(path_dir, quant_elem):	
	return ["/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/page_erro/112043970.html", "/media/doc/home/doc/2013/academico/project/Implementacao/Yang-Algoritmos/novo/rtdm-git/paginas_html/page_erro/112043996_115401269.regex.html"]
	files_all = generate_list_from_cmd(path_dir)
	return files_all[:quant_elem]
	#files = [str(files_all[0]), str(files_all[-1])]
	random.shuffle(files_all)
	#del files_all[0]
	#del files_all[-1]
	if(quant_elem != 2):
		files.extend(files_all[:quant_elem - 2])
	return files
