#!/bin/bash


for((k=0; k < $1; k++));
do
	echo $k
	output_file=../testes/"output$k.txt"
	cmp_file=../testes/comparador/"output$k-cmp.txt"
	echo "RTDM"
	pypy main_rtdm.py > $output_file
	echo "OK"
	xpath=$(cat $(cat ../links_rtdm.txt)extraction.xpath)
	echo -e "$xpath\n"
<<COMMENT
	echo "Extraction"
	python3 main_extraction.py
	echo "OK"
	#gedit $(cat ../links_rtdm.txt)data.json
	cat $(cat ../links_rtdm.txt)extraction.xpath >> $output_file
	diff tester/data1.json $(cat ../links_rtdm.txt)data.json >> $output_file
	python3 tester/comparator.py > $cmp_file
COMMENT
done
