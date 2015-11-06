# Problem 47: Find the first of the first four consecutive integers to have four distinct prime factors.
# Answer: 
print '** Problem 47 **'

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

factors = {}

x = 210
def PrimeFactors(num):
	tmpNum = num
	results = []
	for prime in [i for i in primes if i < num/2+1]:
		if tmpNum == 1:
			return len(set(results))
		while tmpNum%prime == 0:
			results.append(prime)
			tmpNum /= prime

def NumUniquePrimeFactors(num):
	count = 0
	for prime in [i for i in primes if i < num/2+1]:
		if num%prime == 0:
			count += 1
		if count > 4:
			return count
	return count

def something(num,results,realnum):
	tmpNum = num
	if tmpNum == 1:
		factors[realnum] = set(results)
		return
	if tmpNum in factors.keys():
		factors[realnum] = factors[tmpNum] | set(results)
		return
	if tmpNum in primes:
		factors[tmpNum] = set([tmpNum])
	for prime in [i for i in primes if i < num/2+1]:
		if tmpNum%prime == 0 and prime not in results:
			results.append(prime)
			something(tmpNum/prime,results,realnum)

x = 2
while True:
	something(x,[],x)
	something(x+1,[],x+1)
	something(x+2,[],x+2)
	something(x+3,[],x+3)
	count = 0
	for i in range(x,x+4):
		count += (len(factors[i]) == 4)
		#if (len(factors[i]) == 4):
		#	print i,"has 4 factors"
	if count == 4:
		break
	x += 1

#while True:
#	count = 0
#	count = (NumUniquePrimeFactors(x) == 4) + (NumUniquePrimeFactors(x+1) == 4) + (NumUniquePrimeFactors(x+2) == 4) + (NumUniquePrimeFactors(x+3) == 4)
#	if NumUniquePrimeFactors(x) == 4:
#		print x,"has 4 factors"
#	if count == 4:
#		break
#	x += 1

print "First number is",x


#numfacts = {}
#def countFactors(num,startFrom,factors,realnum):
#	tmpNum = num
#	if tmpNum not in numfacts.keys():
#		if realnum == 420:
#			print tmpNum,realnum
#		for prime in [i for i in primes if i < realnum/2+1 and i >= startFrom]:
#			nextPrime = prime
#			if tmpNum%prime == 0:
##				print realnum,"is divisible by",prime
#				factors.append(prime)
#				#while tmpNum%prime == 0:
#				tmpNum = tmpNum/prime
#				if tmpNum%prime != 0:
#					nextPrime = primes[primes.index(prime)+1]
#				if tmpNum == 1 or len(set(factors)) > 4:
#					numfacts[realnum] = set(factors)
#					if len(set(factors)) == 4:
#						print "Got down to tmpNum = 1 without else"
#						print realnum,set(factors)
#					return len(set(factors))
#				else:
#					if realnum == 420:
#						print "tmpNum is",tmpNum,"about to recurse. Factors are",factors
#					result = countFactors(tmpNum,nextPrime,factors,realnum)
#					if result == 4:
#						print "Got down to 4 via recursion"
#						print realnum,factors
#					return result
#	else:
#		if realnum == 420:
#			print "Hit an else with 420"
#			print tmpNum, factors, numfacts[tmpNum],list(set(factors) | numfacts[tmpNum])
##		print tmpNum,"has been previously calculated to have",len(numfacts[tmpNum]),"factors"
##		print set(factors),"are the current factors"
##		print numfacts[tmpNum],"are the factors to be appended"
#		factors = list(set(factors[:]) | numfacts[tmpNum])
#		if realnum == 420:
#			print realnum, set(factors)
#		numfacts[realnum] = set(factors)
#		return len(set(factors))
#
#x = 2*3*5*7
#while True:
#	count = 0
#	count = (countFactors(x,2,[],x) == 4) + (countFactors(x+1,2,[],x+1) == 4) + (countFactors(x+2,2,[],x+2) == 4) + (countFactors(x+3,2,[],x+3) == 4)
#	if count == 4:
#		break
#	x += 1
		
#def hasFour(num):
#	count = 0
#	for prime in primes:
#		if prime > int(num**(0.5))+1:
#			return False
#		if num%prime == 0:
#		#	print "Number: ",num,", Prime",prime,", Count",count
#			count += 1
#			if count == 4:
#				return True
#	return False
#
#x = 210
#while True:
#	if hasFour(x):
#		if hasFour(x+1):
#			if hasFour(x+2):
#				if hasFour(x+3):
#					break
#	x += 1
#
#print x,"is divisible by"
#count = 0
#for prime in primes:
#	if x%prime == 0:
#		print prime, count
#		count += 1
#		if count == 4:
#			break
#print x+1,"is divisible by"
#count = 0
#for prime in primes:
#	if (x+1)%prime == 0:
#		print prime, count
#		count += 1
#		if count == 4:
#			break
#print x+2,"is divisible by"
#count = 0
#for prime in primes:
#	if (x+2)%prime == 0:
#		print prime, count
#		count += 1
#		if count == 4:
#			break
#print x+3,"is divisible by"
#count = 0
#for prime in primes:
#	if (x+3)%prime == 0:
#		print prime, count
#		count += 1
#		if count == 4:
#			break
