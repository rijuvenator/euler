# Problem 205: Find the probability that the sum of nine 4-sided dice is greater than the sum of six 6-sided dice.
# Answer: 0.5731441
print '** Problem 205 **'

import itertools as it
from collections import Counter as count

psums = []
csums = []

for i in it.product(range(1,5),repeat=9):
	psums.append(sum(i))

for i in it.product(range(1,7),repeat=6):
	csums.append(sum(i))

psums.sort()
csums.sort()

pcount = count(psums)
ccount = count(csums)

s = 0
for c in ccount.keys():
	s += ccount[c]*sum([pcount[j] for j in [i for i in pcount.keys() if i>c]])

print "Probability is %9.7f" % (float(s)/float(len(psums)*len(csums)))
