# Problem 28: Find the sum of the diagonals of a clockwise spiral grid.
# Answer: 669171001
print '** Problem 28 **'

size = 1001
n = (size - 1)/2 
print 'Sum is',4*(8*(n**3) + 15*(n**2) + 13*n)/6 + 1
