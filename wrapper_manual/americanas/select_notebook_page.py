#!/bin/python3
import re
import os
import shutil
import glob

def isValidationPage(page):
	html = open(page,"r").read()
	result = re.findall("""<dl>(.+?)</dl>""", html, re.S)
	return result
folder = '/home/ervili/Neemu/ColetaUFAM/ColetaNova/notebooks/americanas_notebook/'
newFolder = '/home/ervili/Neemu/ColetaUFAM/ColetaNova/notebooks/americanas_notebook/notebooks/'
os.listdir(folder)
for filename in glob.glob(folder+'*.html'):
	print("PAGE: " + filename)
	if(isValidationPage(filename)):
		print(filename + " movido")
		shutil.copy2(filename,newFolder)
		

	


