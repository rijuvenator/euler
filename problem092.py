# Problem 92: How many starting numbers below ten million have sum-square-digits chains ending in 89?
# Answer: 8581146
print '** Problem 92 **'

ends = [0] * 20000000
ends[1] = 1
ends[89] = 89

def endsIn(num):
	if ends[num] != 0:
		return ends[num]
	else:
		newnum = sum([int(i)*int(i) for i in str(num)])
		ends[newnum] = endsIn(newnum)
		return ends[newnum]

count = 0
for i in range(1,10000000):
	if endsIn(i) == 89:
		count += 1

print "Number of numbers ending in 89 is",count
