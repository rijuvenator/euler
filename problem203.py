# Problem 203: Find the sum of the distinct squarefree integers in the first 51 rows of Pascal's triangle.
# Answer: 34029210557338
print '** Problem 203 **'

import itertools
import math

def nCr(n,r):
	return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

maxrow = 51
# largest prime I'll have to check = ceiling(sqrt(nCr(50,25)))
# n = int(math.ceil(math.sqrt(nCr(maxrow-1,maxrow/2))))
# LOL. largest prime I'll have to check is actually maxrow. Went from taking about a minute to being instant...
n = maxrow

primeBools = [True] * n

primeBools[0] = False
primeBools[1] = False

for i in range(n):
	if primeBools[i]:
		for j in range(2,n/i + 1 - (n%i == 0)):
			primeBools[j*i] = False

primes = [i for i,x in enumerate(primeBools) if x]

pascal = []

for N in range(maxrow):
	for r in range(N+1):
		pascal.append(nCr(N,r))

pascal = sorted(list(set(pascal)))

def isSqFree(N):
	ans = True
	for p2 in [x**2 for x in primes if x**2 <= N]:
		if N%p2 == 0:
			ans = False
			break
	return ans

s = 0
for i in pascal:
	if isSqFree(i):
		s += i

print 'Sum is', s
