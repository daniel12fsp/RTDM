#!/usr/bin/python3
# -*- coding: utf8 -*-

import xpath
import os
import file
import re
import glob

def extraction_xpath_dir(path_dir):
	file_json = open(os.path.dirname(os.path.realpath(__file__)) + "data.json","w")
	path_xpath = os.path.dirname(os.path.realpath(__file__)) + "/../xpath.txt"
	file_xpath = open(path_xpath)
	lca = file_xpath.read()
	file_xpath.close()

	for page in sorted(glob.glob(path_dir + '*.html')):
		print(page)
		id_file =	re.findall("(\d+)\.html", page)[0]
		xpath.extraction(lca, page, id_file, file_json)
	file_json.close()


path_dir = open(os.path.dirname(os.path.realpath(__file__)) + "/../links_rtdm.txt").read().strip()
extraction_xpath_dir(path_dir)
