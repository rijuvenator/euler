# Problem 56: What is the maximum digit sum of numbers of the form a^b, where a,b are integers < 100?
# Answer: 
print '** Problem 56 **'

maxsum = 0
for a in range(100):
	for b in range(100):
		x = sum([int(i) for i in str(a**b)])
		if x > maxsum:
			maxsum = x

print "Maximum digit sum is",maxsum
