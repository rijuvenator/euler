# Problem 30: Find the sum of all numbers that are equal to the sum of the fifth powers of their digits.
# Answer: 443839
print '** Problem 30 **'

total = 0
for i in range(2,354295):
	if i == sum([int(j)**5 for j in list(str(i))]):
		total += i

print 'Sum is',total
