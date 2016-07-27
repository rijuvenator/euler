# Problem 243: Find the smallest denominator d having a resilience R(d) < 15499/94744.
# Answer:
print '** Problem 243 **'
# *** NOTE: DO NOT DELETE AND START OVER. THE CODE WORKS JUST FINE. JUST TRY TO UNDERSTAND IT. ***

import itertools

n = 40000
primeBools = [True] * n

primeBools[0] = False
primeBools[1] = False

for i in range(n):
	if primeBools[i]:
		for j in range(2,n/i + 1 - (n%i == 0)):
			primeBools[j*i] = False

primes = [i for i,x in enumerate(primeBools) if x]

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def res(d):
	a = [gcd(i,d)==1 for i in range(1,d)]
	sa = sum(a)
	#print sa
	return float(sa)/float(d-1), a


def bleh(num,maxp):
	p = [i for i in primes if i<=maxp]
	x = False
	for i in p:
		x = x or num%i==0
	return not x
def prod(l):
	a = 1
	for i in l:
		a *= i
	return a
def better(num,maxp):
	unres = 1
	x = [1]
	#c = len([i for i in range(maxp+1,num) if bleh(i,maxp)])
	fothers = [i for i in primes if i<num and i>maxp]
	unres += len(fothers)
	x.extend(fothers)
	others = [i for i in fothers if i<num/(maxp)]
	c = 0
	r = 2
	used = []
	while others[0]**r < num:
		for i in itertools.combinations_with_replacement(others, r):
			if prod(i) < num:
				x.append(prod(i))
				c += 1
		r += 1
	unres += c
	print unres
	rd = float(unres)/float(num-1)
	return rd, x

maxp = 19
ss = [i for i in primes if i<=maxp]
z = prod(ss)
print 'Testing:', z
print 'Res:'
m1, q = res(z)
a = [i+1 for i,x in enumerate(q) if x]
#print a
print 'R(d) =', m1
exit()
print 'Better:'
m2, b = better(z,maxp)
print 'R(d) =', m2
print [i for i in a if i not in b]

#print 223092870*4, res(223092870*4)[0]
