#!/bin/bash

./exec_group_loop.sh $1 2>&1 | tee ../testes/output_terminal.txt
