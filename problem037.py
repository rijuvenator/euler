# Problem 37: Find the sum of the only eleven left and right truncatable primes.
# Answer: 
print '** Problem 37 **'

n = 739398
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

def isTrunc(prime,side):
	size = len(str(prime))
	if side == "L":
		for i in range(size):
			if int(str(prime)[i:]) not in primes:
				return False
		return True
	if side == "R":
		for i in range(1,size):
			if int(str(prime)[:i]) not in primes:
				return False
		return True

count = 0
primesum = 0
for prime in primes:
	# This line added later; makes sure there are no 0,4,6,8 anywhere or 0,2,4,5,6,8 after the first digit; dramatically reduces time
	if len(set([0,4,6,8]) & set([int(i) for i in str(prime)])) > 0 or len(set([0,2,4,5,6,8]) & set([int(i) for i in str(prime)[1:]])) > 0:
		continue
	if isTrunc(prime,"L") and isTrunc(prime,"R") and prime > 9:
		count += 1
		primesum += prime
		if count == 11:
			break

if count != 11:
	print "Not done yet."

print "Sum is",primesum
			
