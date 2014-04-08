#!/usr/bin/python3
# -*- coding: utf8 -*-

import xpath
import os
import file

def extraction_xpath_page(file_xpath, page_target):
	file_data = file.get_path_file(file_xpath,"",".data")
	xpath.extraction(file_xpath, page_target, file_data)

def extraction_xpath_dir():
	pass
	


filename = os.path.dirname(os.path.realpath(__file__)) + "/../links_extraction.txt"
file_xpath, page_target, dir_target = file.get_links(filename)
extraction_xpath_page(file_xpath, page_target)
