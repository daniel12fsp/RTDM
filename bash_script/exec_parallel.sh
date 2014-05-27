#!/bin/bash
folder=$(cat ../links_rtdm.txt)
#mkdir $folder"outputs/"
#
parallel -j 5 'a={}; ./exec.sh 1 $a' ::: $folder*/

