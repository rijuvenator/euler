# Problem 33: Find the denominator of the reduced product of the four unique XX/XX fractions whose layman cancellation is correct.
# Answer: 100
print '** Problem 33 **'

nums = []
dems = []
for j in range(11,100):
	for i in range(11,j+1):
		a = int(str(i)[0])
		b = int(str(i)[1])
		c = int(str(j)[0])
		d = int(str(j)[1])
		x = float(i)/float(j)
		y = 0
		if b == 0 or d == 0:
			continue
		if (a == c) ^ (a == d) ^ (b == c) ^ (b == d):
			if a == c:
				y = float(str(b))/float(str(d))
			if a == d:
				y = float(str(b))/float(str(c))
			if b == c:
				y = float(str(a))/float(str(d))
			if b == d:
				y = float(str(a))/float(str(c))
		if abs(x - y) < 0.00000001:
			nums.append(i)
			dems.append(j)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

x = nums[0]*nums[1]*nums[2]*nums[3]
y = dems[0]*dems[1]*dems[2]*dems[3]

while gcd(x,y) != 1:
	j = gcd(x,y)
	x = x/j
	y = y/j

print "Denominator of product is",y
