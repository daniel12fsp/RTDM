#!/bin/bash
i=0
folder=1
for a in *.html;
do
	if [ $i = 65 ]
	then
		i=0
		folder=$[folder+1]
		echo $i,$folder
	else
		mv $a "$folder/"
		echo $a $folder/
	fi
	i=$[i+1]
done

