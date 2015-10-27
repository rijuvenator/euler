# Problem 14: Which number less than one million produces the longest Collatz sequence?
# Answer: 837799
print '** Problem 14 **'

steps = [1]
def collatz(n,count):
	if n <= len(steps):
		count += steps[n-1]
		return count
	else:
		if n%2 == 0:
			n /= 2
		else:
			n = 3*n + 1
		count += 1
		return collatz(n,count)

for i in range(999999):
	steps.append(collatz(i+2,0))

print "Longest Collatz seed is",steps.index(max(steps))+1
