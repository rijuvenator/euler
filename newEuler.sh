#!/bin/bash

if [ $# != 1 ]; then
	echo "Invalid number of arguments."
	exit
fi

if [[ "$1" =~ [^0-9] ]]; then
	echo "Argument is not a number."
	exit
fi

cat > problem$1.py <<EOF
# Problem $((10#$1)):
# Answer:
print '** Problem $((10#$1)) **'

EOF
