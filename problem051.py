# Problem 51: Find the smallest positive integer x such that 1x through 6x contain the same digits.
# Answer: 142857
print '** Problem 51 **'

x = 1
while True:
	x1 = sorted([i for i in str(1*x)])
	x2 = sorted([i for i in str(2*x)])
	x3 = sorted([i for i in str(3*x)])
	x4 = sorted([i for i in str(4*x)])
	x5 = sorted([i for i in str(5*x)])
	x6 = sorted([i for i in str(6*x)])

	if x1 == x2:
		if x2 == x3:
			if x3 == x4:
				if x4 == x5:
					if x5 == x6:
						break
	x += 1
print x
