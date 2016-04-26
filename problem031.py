# Problem 31: Find the number of ways 2 pounds can be made with any number of 1p, 2p, 5p, 10p, 20p, 50p, 1 pound, and 2 pound coins.
# Answer: 73682
print '** Problem 31 **'

#total = 200
#coins = [200, 100, 50, 20, 10, 5, 2, 1]
#enum = [1, 0, 0, 0, 0, 0, 0, 0]
#ways = 1
#
#def dist():
#	global ways
#	last = 0
#	while enum[last] == 0:
#		last += 1
#	if last == 7:
#		return
#	enum[last] -= 1
#	free = coins[last]
#	far = 1
#	while free > 0:
#		enum[last+far] += free/coins[last+far]
#		free -= (free/coins[last+far])*coins[last+far]
#		far += 1
#	ways += 1
#	dist()
#
#dist()
#print ways

#import operator as op
#def nCr(n, r):
#	r = min(r, n-r)
#	if r == 0: return 1
#	numer = reduce(op.mul, xrange(n, n-r, -1))
#	denom = reduce(op.mul, xrange(1, r+1))
#	return numer/denom
#def compute(i):
#	# one way for all 1's
#	lways = 1
#	# one way for itself, if coin
#	if i in coins:
#		lways += 1
#	for lesser in [coin for coin in coins if coin < i and coin != 1]:
#		if i/lesser > 1:
#			lways += nCr(ways[lesser] + i/lesser-1 - 1, i/lesser-1) * ways[i - (i/lesser)*lesser]
#		else:
#			lways += ways[i-lesser]
#	ways[i] = lways
#
#for i in range(2,val+1):
#	compute(i)
#	print i, ":", ways[i]

#ways = [0] * (val+1)
#ways[0] = 1
#ways[1] = 1
#def waysUsingOnly(i,max_coin):
#	if coins[max_coin] == 2:
#		return i/2+1
#	if i/coins[max_coin] == 0:
#		return 0
#	elif i/coins[max_coin] == 1:
#		return ways[i-coins[max_coin]] + waysUsingOnly(i, max_coin+1)
#	else:
#		tmpways = 0
#		for num in range(1,i/coins[max_coin]-1+1):
#			tmpways += waysUsingOnly(i-num*coins[max_coin], max_coin)
#		tmpways += waysUsingOnly(i, max_coin+1)
#		#if i in coins:
#		#	tmpways += 1
#		return tmpways

coins = [200, 100, 50, 20, 10, 5, 2, 1]
val = 200
ways = {}
for coin in coins:
	if coin == 1:
		ways[coin] = [1] * (val+1)
	elif coin == 2:
		ways[coin] = [i/2 for i in range(val+1)]
	else:
		ways[coin] = [0] * (val+1)
	ways[coin][coin] = 1

def waysUsingAtLeastOne(i,idx):
	if coins[idx] == 1:
		return 1
	elif coins[idx] == 2:
		return i/2
	else: 
		return sum([ways[j][i-coins[idx]] for j in coins if j <= coins[idx]])

for i in range(2,val+1):
	for idx in [idx for idx,coin in enumerate(coins) if coin <= i and coin > 1]:
		ways[coins[idx]][i] = waysUsingAtLeastOne(i, idx)

sums = [0] * (val+1)
for num in range(val+1):
	for coin in coins:
		sums[num] += ways[coin][num]

print "Total number of ways is", sums[val]
