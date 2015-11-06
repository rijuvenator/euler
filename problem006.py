# Problem 6: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Answer: 25164150
print '** Problem 6 **'

# The difference is the cross terms only. Therefore,

diff = 0

for i in range(1,101):
	diff += 2*i*sum(range(i+1,101))

print "Difference is",diff
