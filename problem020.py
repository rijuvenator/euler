# Problem 20: Find the digit sum of 100!.
# Answer: 648
print '** Problem 20 **'

def factorial(n):
	if n == 1:
		return 1
	else:
		return n*factorial(n-1)

print "Sum is",sum([int(i) for i in list(str(factorial(100)))])
