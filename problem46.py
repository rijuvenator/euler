# Problem 46: What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# Answer: 5777
print '** Problem 46 **'

n = 100
primeBools = [True] * n
primeBools[0] = False
primeBools[1] = False

for (i, isprime) in enumerate(primeBools):
	if isprime:
		for j in range(2,n/i + 1 - (n%i == 0)):
			primeBools[j*i] = False

primesUpToN = [i for i,isprime in enumerate(primeBools) if isprime == True]

def isPrime(num):
	sqrtn = int(num**(0.5))+1
	for x in range(2,sqrtn+1):
		if num%x == 0:
			return False
	return True

ans = 5
while True:
	if isPrime(ans):
		ans += 2
		continue
	largestSquare = int((ans/2)**(0.5))
	currentSquare = largestSquare
	canBeWritten = False
	while True:
		if isPrime(ans - 2*currentSquare*currentSquare):
			canBeWritten = True
			break
		currentSquare -= 1
		if currentSquare == 0:
			break
	if canBeWritten == True:
		ans += 2
	else:
		break

print "Smallest number is",ans
