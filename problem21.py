# Problem 21: Find the sum of all amicable numbers less than 10000.
# Answer: 31626
print '** Problem 21 **'

def sumDivisors(n):
	num = 1
	for x in range(2,int(n**(0.5))+1):
		if n%x == 0 and x*x != n:
			num = num + x + n/x
		elif n%x == 0 and x*x == n:
			num = num + x
	return num

total = 0
for i in range(9999):
	x = sumDivisors(i+1)
	if sumDivisors(x) == i+1 and i+1 != x:
		total += i+1

print "Sum is",total
