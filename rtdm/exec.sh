#!/bin/sh

clear
echo "python works";
path=$(pwd);
     
rm ../paginas_html/*.log
rm ../paginas_html/*/*.log
rm ../paginas_html/*.regex
rm ../paginas_html/*/*.regex
#rm *.pyc
rm -R __pycache__/

modulo=main.py
#mapeamento.py

#gnome-terminal -e "bash -c 'python2 $modulo > /dev/pts/3'; exit;"		
#gnome-terminal -e "bash -c 'python -m pdb $modulo';read" &
gnome-terminal -e "bash -c 'python -m pudb.run $modulo'" &
#gnome-terminal -e "bash -c 'python2 $modulo';read" &
