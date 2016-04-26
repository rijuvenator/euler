# Problem 63: Find the number of n-digit integers that are nth powers.
# Answer: 49
print '** Problem 63 **'

count = 0
for e in range(22):
	for b in range(1,10):
		if len(str(b**e)) == e:
			count += 1
			#print str(b)+"^"+str(e)+" = "+str(b**e)

print "Number of integers is", count
