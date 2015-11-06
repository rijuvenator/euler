# Problem 44: Find the minimum absolute difference of two pentagonal numbers whose sum and difference are also pentagonal.
# Answer: 5482660
print '** Problem 44 **'

# This gives an answer; however, it doesn't prove that it's the minimum; it just gives the first answer.
nmax = 2170
pnums = []
for i in range(nmax):
	pnums.append((i+1)*(3*(i+1)-1)/2)

def isPentagonal(num):
	x = (1 + (1 + 4*3*2*num)**(0.5))/6
	y = float(int(x))
	if x == y:
		return True
	else:
		return False

mindif = pnums[-1]
for i in pnums:
	for j in pnums[pnums.index(i)+1:]:
		if abs(i-j) < mindif and abs(i-j) != 0:
			if isPentagonal(i+j) and isPentagonal(abs(i-j)):
				mindif = abs(i-j)

print "Minimum difference is",mindif
