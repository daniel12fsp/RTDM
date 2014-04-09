#!/usr/bin/python3
# -*- coding: utf8 -*-

import xpath
import os
import file

def extraction_xpath_dir(page_target):
	diretory = file.get_path_dir_from_file(page_target)
	file_xpath = file.take_one_file(diretory, ".xpath")
	for page in file.take_files_same_extension(diretory, ".html"):
		file_data = file.create_file(diretory + page, ".data")
		xpath.extraction(file_xpath, diretory + page,  file_data)



filename = os.path.dirname(os.path.realpath(__file__)) + "/../links_rtdm.txt"
_, page, folder = file.get_links(filename)
extraction_xpath_dir(page)
