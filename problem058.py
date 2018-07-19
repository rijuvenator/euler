# Problem 58: Find the minimum side length of a counterclockwise number spiral for which the fraction of primes on the diagonals is less than 10%.
# Answer: 26241
import pyprimesieve as ps
print '** Problem 58 **'

#10001 2250 20001 0.1125
maxs = 40001

# --- Make Primes
n = maxs**2 + 1
primes = ps.primes(n)

pcount = 0
lastbot = 1
diags = 1
pointer = 0
for s in range(3,maxs+1,2):
	diags = s/2 * 4 + 1
	for p in [lastbot + (s-1), lastbot + 2*(s-1), lastbot + 3*(s-1)]:
		thisP = pointer
		while primes[thisP] <= p:
			if p == primes[thisP]:
				pcount += 1
				break
			thisP += 1
	pointer = thisP
	lastbot = s**2
	if float(pcount)/float(diags) < 0.1:
		print 'Side length is', s
		break
