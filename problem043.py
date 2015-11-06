# Problem 43: Find the sum of pandigital numbers with a given interesting substring divisibility property.
# Answer: 16695334890
print '** Problem 43 **'

primes = [2,3,5,7,11,13,17]
mults = {}
firsttwos = {}
lasttwos = {}
for i in primes:
	mults[i] = ["{:03d}".format(n) for n in range(0,1000,i)]
	for n in mults[i][:]:
		if len(set([n[0],n[1],n[2]])) != 3:
			mults[i].remove(n)

def cutlist(prime, prevstring):
	return [i for i in mults[prime] if i[0:2] == prevstring[1:3]]

panlist = []
cuts = {}
for a in mults[2]:
	cuts[3] = cutlist(3,a)
	for b in cuts[3]:
		cuts[5] = cutlist(5,b)
		for c in cuts[5]:
			cuts[7] = cutlist(7,c)
			for d in cuts[7]:
				cuts[11] = cutlist(11,d)
				for e in cuts[11]:
					cuts[13] = cutlist(13,e)
					for f in cuts[13]:
						cuts[17] = cutlist(17,f)
						for g in cuts[17]:
							pancan = a+b[2]+c[2]+d[2]+e[2]+f[2]+g[2]
							if len(set([i for i in pancan])) == 9:
								panlist.append(pancan)

pansum = 0
for pan in panlist:
	missingdigit = str(45 - sum([int(i) for i in pan]))
	truepan = missingdigit + pan
	pansum += int(truepan)

print "Sum is",pansum

