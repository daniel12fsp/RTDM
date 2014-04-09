#!/usr/bin/python3
# -*- coding: utf8 -*-

import xpath
import os
import file

def extraction_xpath_dir(folder):
	file_xpath = file.take_one_file(folder, ".xpath")
	for page in file.take_files_same_extension(folder, ".html"):
		file_data = file.create_file(folder + page, ".data")
		xpath.extraction(file_xpath, folder + page,  file_data)



filename = os.path.dirname(os.path.realpath(__file__)) + "/../links_rtdm.txt"
folder = file.get_links(filename)
extraction_xpath_dir(folder)
