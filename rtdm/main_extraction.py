#!/usr/bin/python3
# -*- coding: utf8 -*-

import xpath
import os
import file
import re
import glob

def extraction_xpath_dir(path_dir):
	file_json = open(path_dir + "data.json","w")
	file_xpath = open(path_dir + "extraction.xpath")
	lca = file_xpath.read()
	file_xpath.close()

	for page in sorted(glob.glob(path_dir + '*.html')):
		id_file =	re.findall("(\d+)\.html", page)[0]
		xpath.extraction(lca, page, id_file, file_json)
	file_json.close()


path_dir = file.get_link("arquivo")
extraction_xpath_dir(path_dir)
