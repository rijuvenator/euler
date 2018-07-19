# Problem 301: For how many positive integers n <= 2**30 is the nim-sum of n, 2n, 3n = 0?
# Answer: 2178309
print '** Problem 301 **'

def nimsum(n):
	return n ^ (2*n) ^ (3*n)

#for z in range(20):
#	x = 1
#	c = 0
#	while x <= 2**z:
#		if not nimsum(x):
#			c += 1
#		x += 1
#	print z, c

# As it turns out, the number for 2**i is the
# i'th Fibonacci number. So it's easier to just
# calculate that.
a = 1
b = 2
e = 2
print "0 1"
print "1 2"
while e<=30:
	print e, a+b
	olda = a
	a = b
	b = olda+b
	e+=1
