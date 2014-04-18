#! /bin/bash

folder=$(cat "../links_rtdm.txt")
gedit $(ls $folder*".data"|shuf -n 5)
