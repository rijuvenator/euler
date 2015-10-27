# Project Euler Solutions

My solutions to Project Euler problems.

On a Unix-like system, for example `python problem01.py` prints
```
** Problem 1 **
Sum is 233168
```

Batch suggestions:
* run all python scripts, printing as above
```
for i in *.py; do python $i; done
```
* print all problem statements
```
for i in *.py; do sed -n "1p" $i; done
```
* print all answers
```
for i in *.py; do printf "Answer to Problem "; sed -n "1p" $i | awk '{printf $3 " "}'; sed -n "2p" $i | awk '{print $3'}; done
``` 
