#!/bin/bash
<<COMMENT
	$1 - Quantidade de iteracoes
	$2 - Pasta aonde vai ocorrer a extracao
	$3 - O nome da pasta
COMMENT

if [[ -z "$3" ]]
	then
		$bateria=$3
	else
		$bateria="teste"
	fi


output_general="$3../output_general.txt"

for((k=0; k < $1; k++));
do
	rm "$2"extraction.xpath
	output_file="bateria-$bateria-output$k.txt"
	pypy -B ../rtdm/main_rtdm.py "$2" > $output_file
	xpath=$(cat "$2"extraction.xpath)
	echo -e "$bateria - $k - $xpath\n" >> $output_general
done
