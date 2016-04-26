# Problem 50: Find the prime below 1 million that can be written as the most number of consecutive primes.
# Answer: 997651
print '** Problem 50 **'

#n = 1000000
n = 1000000
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

#print sum(primes[primes.index(1097)-182:primes.index(1097)+1])
#print primes[primes.index(1097)-182]

#maxcon = 1000
constart = 542
maxcon = constart+2
sums = [[0 for i in range(len(primes))] for i in range(maxcon)]
sums[0] = primes
sums[1] = [sum(primes[i:i+constart]) for i in range(len(primes)-constart+1)]
sums[1] += [0] * (constart-1)
current = 2 

for con in range(constart+1,maxcon):
	#meh = [0] * len(primes)
	for i in range(len(primes)-con+1 - 10000):
		#meh[i] = sums[con-2][i] + primes[i+con-1]
		sums[con-constart-1+2][i] = sums[con-constart-1+1][i] + primes[i+con-1]
		if sums[con-constart-1+2][i] in primes and con > current:
			current = con
			print "Prime is", sums[con-constart-1+2][i]
			break
	#sums[con-1] = meh
