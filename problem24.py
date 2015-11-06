# Problem 24: Find the millionth lexicographic permutation of 0123456789.
# Answer: 2783915460
print '** Problem 24 **'

import itertools

perms = list(itertools.permutations('0123456789'))

print "Millionth lexicographic permutation is","".join(perms[999999])
