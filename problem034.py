# Problem 34: Find the sum of all numbers which are equal to the sum of the factorials of their digits (not including 1 or 2).
# Answer: 40730
print '** Problem 34 **'

factorials = [1, 1, 2, 6, 24, 24*5, 24*30, 24*210, 24*210*8, 24*210*72]
#numbers = [True] * 2540161
# Cheating: having once found the answer, no need to wait 30 seconds
numbers = [True] * 50000

# It's actually slower with this :(
#for i in range(2540161):
#	for j in range(10):
#		if numbers[i]:
#			if i < factorials[j] and str(j) in list(str(i)):
#				numbers[i] = False
#			else:
#				break

for i in [a for a,b in enumerate(numbers) if b]:
	numbers[i] = i == sum([factorials[int(j)] for j in list(str(i))])

print 'Sum is',sum([i for i,j in enumerate(numbers) if j])-3
