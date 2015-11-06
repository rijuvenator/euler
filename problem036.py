# Problem 36: Find the sum of all numbers less than one million that are palindromic in both base 2 and base 10.
# Answer: 872187
print '** Problem 36 **'

tot = 0
n = 1000000
for i in range(1,n,2):
	dec = list(str(i))
	two = list(bin(i)[2:])
	decrev = list(str(i))
	tworev = list(bin(i)[2:])
	decrev.reverse()
	tworev.reverse()
	if dec == decrev and two == tworev:
		tot += i

print 'Sum is',tot
