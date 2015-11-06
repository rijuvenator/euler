# Problem 35: Find the number of circular primes below one million.
# Answer: 55 
print '** Problem 35 **'

n = 1000000
primes = [True] * n
primes[0] = False
primes[1] = False

for i,isPrime in enumerate(primes):
	if not isPrime:
		continue
	for j in range(2,n/i + 1*(n%i != 0)):
		primes[i*j] = False

primes = [i for i,j in enumerate(primes) if j]

from collections import deque

def isCircular(prime):
	piano = deque(list(str(prime)))
	# I copied this part. Totally didn't realize that the relevant primes had to only have odd numbers not 5
	if prime != 2 and prime != 5 and ('0' in piano or '2' in piano or '4' in piano or '6' in piano or '8' in piano  or '5' in piano):
		return False
	for i in range(len(piano)):
		piano.append(piano.popleft())
		nownum = int(''.join(str(j) for j in piano))
		if nownum not in primes:
			return False
	return True

count = 0
for i in primes:
	if isCircular(i):
		count += 1

print 'Number of circular primes is',count
