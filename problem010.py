# Problem 10: Find the sum of all primes below two million.
# Answer: 142913828922
print '** Problem 10 **'

n = 2000000 
primeBools = [True] * n
primeBools[0] = False
primeBools[1] = False

for (i, isprime) in enumerate(primeBools):
	if isprime:
		if n%i == 0:
			xup = n/i
		else:
			xup = n/i + 1
		for j in range(2,xup):
			primeBools[j*i] = False

primes = [i for i,isprime in enumerate(primeBools) if isprime == True]
print "Sum is",sum(primes)
