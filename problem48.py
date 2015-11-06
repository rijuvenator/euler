# Problem 48: Find the last ten digits of the sum of n^n for n an integer in [1,1000].
# Answer: 
print '** Problem 48 **'

Sum = 0
for i in range(1,1001):
	Sum += i**i

print "Last ten digits are",str(Sum)[-10:]
