#! /bin/bash

folder=$(cat "../links_rtdm.txt")
echo "Ecluir $folder dados"

rm $folder*.regex
rm $folder*.data
rm $folder*.xpath
rm $folder*.log

