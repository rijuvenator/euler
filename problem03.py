# Problem 3: Find the largest prime factor of 600851475143.
# Answer: 6857
print '** Problem 3 **'

n = 600851475143
d = 2
x = n
l = d
while x > 1:
	while x%d == 0:
		x = x/d
		l = d
	d = d + 1
	if d*d > n:
		if x>1:
			l = x
		break

print "Largest prime is",l
