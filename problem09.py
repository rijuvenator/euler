# Problem 9: Find the product of the Pythagorean triplet that sums to 1000.
# Answer: 31875000 
print '** Problem 9 **'

for a in range(1,500):
	b = (500 - a)/(1 - 0.001*a)
	if int(b) == b:
		print "Product is",int(a*b*(1000 - a - b))
		break
