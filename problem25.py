# Problem 25: Find the index of the first Fibonacci number with 1000 digits.
# Answer: 4782
print '** Problem 25 **'

fib = {1:1,2:1}
def fibonacci(n):
	if n in fib.keys():
		return fib[n]
	else:
		fib[n] = fibonacci(n-1) + fibonacci(n-2)
		return fib[n]

n = 1
while len(list(str(fibonacci(n))))<1000:
	fibonacci(n)
	n += 1

print 'Index is',n
