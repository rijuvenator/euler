# Problem 29: How many distinct terms are formed by a^b, where a,b are integers in [2,100]?
# Answer: 9183
print '** Problem 29 **'

nums = []
for a in range(2,101):
	for b in range(2,101):
		nums.append(a**b)

print "Number of distinct terms is",len(set(nums))
