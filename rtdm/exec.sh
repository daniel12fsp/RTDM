#!/bin/sh

clear
echo "python works";
path=$(pwd);


rm ../paginas_html/*.log
rm ../paginas_html/*/*.log
rm ../paginas_html/*.regex
rm ../paginas_html/*/*.regex
modulo=main.py
#mapeamento.py

gnome-terminal -e "bash -c 'python2 $modulo ';$SHELL" &
#gnome-terminal -e "bash -c 'python -m pdb $modulo';$SHELL" &
#gnome-terminal -e "bash -c 'python -m pudb.run $modulo';$SHELL" &
#gnome-terminal -e "bash -c 'python2 $modulo';$SHELL" &
