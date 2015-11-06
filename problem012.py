# Problem 12: Find the first triangular number to have over 500 divisors.
# Answer: 76576500
print '** Problem 12 **'

def numDivs(n):
	if n == 1:
		return 1
	num = 2
	for x in range(2,int(n**(0.5))+1):
		if n%x == 0 and x*x != n:
			num += 2
		if n%x == 0 and x*x == n:
			num += 1
	return num

n = 1
while numDivs(n*(n+1)/2) < 500:
	n += 1

print "Number is",n*(n+1)/2
