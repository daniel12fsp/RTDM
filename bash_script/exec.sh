#!/bin/bash
<<COMMENT
	$1 - Quantidade de iteracoes
	$2 - Pasta aonde vai ocorrer a extracao
COMMENT

folder=$(cat ../links_rtdm.txt)

regex="([0-9]+/$)"
[[ $2 =~ $regex ]]
name_folder="${BASH_REMATCH[1]}"
	if [ "$name" != "" ];
	then
		./exec_group.sh $1 $2 $name_folder 2>&1 | tee outputs/terminal/output_terminal-"$name_folder".txt
	fi

