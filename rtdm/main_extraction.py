#!/usr/bin/python3
# -*- coding: utf8 -*-

import xpath
import os
import file
import re
import glob

def extraction_xpath_dir(folder):
	file_xpath = folder + "extraction.xpath"
	print("file_xpath", file_xpath)
	file_json = open(folder + "data.json","w")
	for page in sorted(glob.glob(folder + '*.html')):
		print("page", page)
		id_file =	re.findall("(\d+)\.html", page)[0]
		xpath.extraction(file_xpath, page, id_file, file_json)
	file_json.close()


filename = os.path.dirname(os.path.realpath(__file__)) + "/../links_rtdm.txt"
folder = file.get_links(filename)
extraction_xpath_dir(folder)
