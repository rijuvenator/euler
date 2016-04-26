# Problem 27: Find the product of the coefficients of the quadratic polynomial yielding the largest number of consecutive primes.
# Answer: -59231
print '** Problem 27 **'

# a must be odd, b has to be prime

N = 22000
bbools = [True] * N
bbools[0] = False
bbools[1] = False

for (i, isprime) in enumerate(bbools):
	if isprime:
		if N%i == 0:
			xup = N/i
		else:
			xup = N/i + 1
		for j in range(2,xup):
			bbools[j*i] = False

blist = [i for i,isprime in enumerate(bbools) if isprime == True and i<1000]
plist = [i for i,isprime in enumerate(bbools) if isprime == True]

maxa = 0
maxb = 0
maxp = 0

for a in range(1,1000,2):
	for b in blist:
		p1 = b
		p2 = b
		n1 = 0
		n2 = 0
		while p1 in plist:
			n1 += 1
			p1 = n1*n1 + a*n1 + b
		while p2 in plist:
			n2 += 1
			p2 = n2*n2 - a*n2 + b
		if n1 > maxp:
			maxp = n1
			maxa = a
			maxb = b
		if n2 > maxp:
			maxp = n2
			maxa = -a
			maxb = b

print "Product is",maxa*maxb
