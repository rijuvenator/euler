# Problem 47: Find the first of the first four consecutive integers to have four distinct prime factors.
# Answer: 134043
print '** Problem 47 **'

n = 1000
primeBools = [True] * n
#primeBools = {}
#for i in range(n):
#	primeBools[i] = True

primeBools[0] = False
primeBools[1] = False

for i in range(n):
	if primeBools[i]:
		for j in range(2,n/i + 1 - (n%i == 0)):
			primeBools[j*i] = False

primes = [i for i,x in enumerate(primeBools) if x]
#primes = [i for i in primeBools.keys() if primeBools[i]]

#factors = {}
factors = [None] * 140000
factors[0] = []
factors[1] = []
factors[2] = [2]
factors[3] = [3]

# Unmemoized version
def NumUniquePrimeFactors(num):
	count = 0
	for prime in [i for i in primes if i < num/2+1]:
		if num%prime == 0:
			count += 1
		if count > 4:
			return count
	return count

# Fills "factors", also returns the list for a given number
def FillUnq(num):
	global factors
#	if num in factors.keys():
	if factors[num] is not None:
		return factors[num]
	else:
		if num in primes:
			factors[num] = [num]
			return factors[num]
		thisf = []
		for prime in [i for i in primes if i < num/2+1][::-1]: # don't need primes > half the number; start from the biggest
			if num%prime == 0:
				thisf.append(prime)
				thisf.extend(FillUnq(num/prime))
				thisf = list(set(sorted(thisf)))
				break
		factors[num] = thisf
		return factors[num]

# I cheated the first time; I successively increased this number so I wouldn't waste time, but it didn't run under a minute
# The problem was not with the algorithm or the memoization, but with the number of primes and the list comprehension.
# I needed no primes under 1000; setting n to 1000000 led to the slowdown.
#f = 644
#done = False
#while not done:
#	if len(FillUnq(f))==4:
#		if len(FillUnq(f+1))==4:
#			if len(FillUnq(f+2))==4:
#				if len(FillUnq(f+3))==4:
#					done = True
#					print "First integer is", f
#	f += 1

# Unmemoized version
f = 644
done = False
while not done:
	if NumUniquePrimeFactors(f)==4:
		if NumUniquePrimeFactors(f+1)==4:
			if NumUniquePrimeFactors(f+2)==4:
				if NumUniquePrimeFactors(f+3)==4:
					done = True
					print "First integer is", f
	f += 1
