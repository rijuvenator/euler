# Problem 40: Find the product of the (10^i)th digits of Champernowne's constant for i between 0 and 6, inclusive.
# Answer: 210
print '** Problem 40 **'

digits = ""
for i in range(185185):
	digits += str(i+1)

prod = 1
for i in range(7):
	prod *= int(digits[10**i-1])

print 'Product is',prod
