# Problem 209: Find the number of truth tables T such that T(abcdef) & T(bcdefa ^ (b & c)) == 0 for all 6-bit inputs abcdef.
# Answer: 15964587728784
print '** Problem 209 **'

print "Number of truth tables is",1 * 3 * 4 * 18 * 18 * 4106118243

# This part of the code takes every number between 0 and 63 and computes its bcdefa ^ (b & c) partner
#n = 6
#nums = [[]] * (2**n)
#count = 0
#jays = []
#for abcdef in range(2**n):
#	b = (abcdef & 2**(n-2))>>(n-2)
#	c = (abcdef & 2**(n-3))>>(n-3)
#	bcdefa = ((abcdef & 2**(n-1)-1) << 1) + (abcdef >> (n-1))
#	j = (bcdefa ^ (b & c))
#	jays.append(j)
#	print "T("+str(abcdef)+")","aka","T("+format(abcdef,"06b")+")","has to result in 0 when anded with","T("+str(j)+")","aka","T("+format(j,"06b")+")"
#
# jays is a list of partners
# This part of the code writes out the cycles: 0 -> 0, 1 -> 2 -> 4 -> 8 -> 16 -> 32 -> 1, etc.
# Basically it goes through range(64) again, and if the starting number has not been done already, it follows the jays chain down
#
#alreadytraversed = []
#for i in range(2**n):
#	idx = i
#	inAChain = False
#	while True:
#		if idx in alreadytraversed:
#			if inAChain:
#				print idx
#			break
#		else:
#			if not inAChain:
#				print ":: ",
#			inAChain = True
#			print idx,"->",
#			alreadytraversed.append(idx)
#			idx = jays[idx]

# By using the above code (which no longer executes), I determined that:
# 1. Every number 0-64 maps injectively to another number 0-64
# 2. This consists of cycles of the following length: 1, 2, 3, 6, 6, and 46 (the sum is 64); the next bit must result in 0 when anded with the current
# 3. A valid bit pattern of length n: does not start AND end in 1; has no neighboring 1s
# 4. I determined that the number of valid bit patterns of length n is F_n + F_n+2 where F_1 = 0 and F_2 = 1
#    (I just started drawing trees and counting)
# 5. Therefore, the number of possible bit patterns of length 64 satisfying the conditions is
#    1 * 3 * 4 * 18 * 18 * (F_46 + F_48)
# Using the code below, I computed F_46 + F_48
#    1 * 3 * 4 * 18 * 18 * 4106118243

# Generate fibonnaci numbers
#fibs = [0,1]
#while len(fibs) < 50:
#	fibs.append(fibs[-1] + fibs[-2])
#
# F_n corresponds to fibs[n-1]
#
#print fibs[45] + fibs[47]

