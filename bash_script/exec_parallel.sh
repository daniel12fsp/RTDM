#!/bin/bash
folder=$(cat ../links_rtdm.txt)
mkdir $folder"outputs/"
parallel -j 3 'a={}; ./exec.sh 10 "$a"' ::: $folder*/

