# Project Euler Solutions

My solutions to Project Euler problems.

On a Unix-like system, `python problemXX.py` prints ``** Problem XX **`` and a sentence with the answer.

Batch suggestions:
* ``for i in *.py; do python $i; done`` runs all python scripts, printing as above
* ``for i in *.py; do sed -n "1p" $i; done`` prints all problem statements
* ``for i in *.py; do printf "Answer to Problem "; sed -n "1p" $i | awk '{printf $3 " "}'; sed -n "2p" $i | awk '{print $3'}; done`` prints all answers
