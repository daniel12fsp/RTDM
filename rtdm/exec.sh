#!/bin/sh


for((k=0; k < 30; k++));
do
	echo $k
	output_file=../testes/"output$k.txt"
	echo "RTDM"
	pypy main_rtdm.py > $output_file
	echo "OK"
	echo "Extraction"
	python3 main_extraction.py
	echo "OK"
	#gedit $(cat ../links_rtdm.txt)data.json
	cat $(cat ../links_rtdm.txt)extraction.xpath >> $output_file
	diff tester/data1.json $(cat ../links_rtdm.txt)data.json >> $output_file
done
