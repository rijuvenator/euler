# Problem 23: Find the sum of all the positive integers than cannot be written as the sum of two abundant numbers.
# Answer: 4179871
print '** Problem 23 **'

def sumDivisors(n):
	num = 1
	for x in range(2,int(n**(0.5))+1):
		if n%x == 0 and x*x != n:
			num = num + x + n/x
		elif n%x == 0 and x*x == n:
			num = num + x
	return num

def isAbundant(n):
	return sumDivisors(n) > n

abBool = [False] * 28112
for i in range(1,28112):
	abBool[i] = isAbundant(i)

ab = [i for i,x in enumerate(abBool) if x == True]

canBe = [False] * 28124
for i in ab:
	for j in [k for k in ab if k<28124-i and k>=i]:
		canBe[i+j] = True

print "Sum is",sum([i for i,x in enumerate(canBe) if x == False]) 
