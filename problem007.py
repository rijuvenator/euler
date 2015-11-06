# Problem 7: What is the 10,001st prime number?
# Answer: 104743
print '** Problem 7 **'

n = 105720
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
print "10,001st prime is",primes[10000]
