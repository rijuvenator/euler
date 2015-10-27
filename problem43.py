# Problem 43: Find the sum of pandigital numbers with a given interesting substring divisibility property.
# Answer:
print '** Problem 43 **'

primes = [2,3,5,7,11,13,17]
mults = {}
firsttwos = {}
lasttwos = {}
for i in primes:
	mults[i] = ["{:03d}".format(n) for n in range(0,1000,i)]
	for n in mults[i][:]:
		if n[0] == n[1] or n[0] == n[2] or n[1] == n[2]:
			mults[i].remove(n)
	firsttwos[i] = set([n[0:2] for n in mults[i]])
	lasttwos[i] = set([n[1:3] for n in mults[i]])
