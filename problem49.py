# Problem 49: Find the 12 digit number formed by concatenating the other arithmetic sequence of primes that are permutations of each other.
# Answer: 296962999629
print '** Problem 49 **'

import itertools

n = 10000
primeBools = {}
for i in range(n):
	primeBools[i] = True

primeBools[0] = False
primeBools[1] = False

for i in range(n):
	if primeBools[i]:
		for j in range(2,n/i + 1 - (n%i == 0)):
			primeBools[j*i] = False

primes = [i for i in primeBools.keys() if primeBools[i] == True]

def findArithmeticPrime():
	for i in primes:
		if len(str(i)) < 4:
			continue
		permTuples = set(list(itertools.permutations(str(i))))
		primePerms = []
		for thing in permTuples:
			toBeAdded = "".join(thing)
			if int(toBeAdded) in primes:
				primePerms.append(toBeAdded)
		primePerms = sorted(list(set(primePerms[:])))
		diffs = []
		for prime1 in primePerms:
			for prime2 in primePerms[primePerms.index(prime1)+1:]:
				if str(2*int(prime2) - int(prime1)) in primePerms:
					if prime1[0] != "0" and prime1 != "1487":
						diff = int(prime2)-int(prime1)
						ans = prime1+str(int(prime1)+diff)+str(int(prime1)+2*diff)
						return ans

print "Number is",findArithmeticPrime()

