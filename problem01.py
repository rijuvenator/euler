# Problem 1: Find the sum of all the multiples of 3 or 5 below 1000.
# Answer: 233168
print '** Problem 1 **'

x = 0;
for i in range(1000):
	if i%3 == 0 or i%5 == 0:
		x = x + i

print "Sum is",x
