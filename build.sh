#!/bin/bash
rm test.gv
./main.py > test.gv
cat test.gv | dot -Tpng > test.png 
