# Problem 45: Find the second non-unit triangle number that is also pentagonal and hexagonal (after T_285 = P_165 = H_143).
# Answer: 1533776805
print '** Problem 45 **'

#nmax = 10000
#tnums = [n*(n+1)/2 for n in range(286,nmax+1)]
#pnums = [n*(3*n-1)/2 for n in range(165,nmax+1)]
#hnums = [n*(2*n-1) for n in range(143,nmax+1)]
#allthree = [n for n in tnums if n in pnums and n in hnums]

def isPentagonal(num):
	x = (1 + (1 + 4*3*2*num)**(0.5))/6
	y = float(int(x))
	if x == y:
		return True
	else:
		return False

def isHexagonal(num):
	x = (1 + (1 + 4*2*num)**(0.5))/4
	y = float(int(x))
	if x == y:
		return True
	else:
		return False

n = 286
nextnum = 0
while True:
	num = n*(n+1)/2
	n += 1
	if isPentagonal(num) and isHexagonal(num):
		nextnum = num
		break

print "Next number is",nextnum
