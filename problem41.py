# Problem 41: Find the largest pandigital prime.
# Answer: 
print '** Problem 41 **'

n = 100
primeBools = [True] * n
primeBools[0] = False
primeBools[1] = False

for (i, isprime) in enumerate(primeBools):
	if isprime:
		for j in range(2,n/i + 1 - (n%i == 0)):
			primeBools[j*i] = False

primesUpToN = [i for i,isprime in enumerate(primeBools) if isprime == True]

def isPrime(num):
	for x in primesUpToN:
		if num%x == 0:
			return False
	sqrtn = int(num**(0.5))+1
	for x in range(n,sqrtn+1):
		if num%x == 0:
			return False
	return True

# Ugh. 9 or 8 digits can't be prime because 45 and 36 are divisible by 3. Start with 7 digits.

pan = 7654321
while True:
	#if isPrime(pan):
	#	if set(range(1,len(str(pan))+1)) == set([int(z) for z in str(pan)]):
	if set(range(1,len(str(pan))+1)) == set([int(z) for z in str(pan)]):
		if isPrime(pan):
			break
	pan -= 2

print "Largest pandigital prime is",pan
