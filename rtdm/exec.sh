#!/bin/sh

clear
echo "python works";
path=$(pwd);
gnome-terminal -e "bash -c 'python2 main.py';$SHELL" &
#gnome-terminal -e "bash -c 'python2 mapeamento.py';$SHELL" &
#python -m pudb.run main.py 
#gnome-terminal -e "bash -c 'python -m pdb main.py'; $SHELL" &
