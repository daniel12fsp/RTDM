#!/bin/bash
<<COMMENT
    Parametros
	$1 - Quantidade de iteracoes
	$2 - Pasta aonde vai ocorrer a extracao
COMMENT

folder=$(cat ../links_rtdm.txt)

./exec_group.sh $1 $2 2>&1 | tee $2/output_terminal.txt

