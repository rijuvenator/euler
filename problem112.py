# Problem 112: Find the least number for which the proportion of bouncy numbers is exactly 99%.
# Answer: 1587000
print '** Problem 112 **'

def isBouncy(num):
	n = str(num)
	l = len(n)
	s = "".join(sorted(n))
	if int(s) == num or int(s[::-1]) == num:
		return False
	else:
		return True

count = 0
num = 99
while float(count)/float(num) != 0.99:
	num += 1
	if isBouncy(num):
		count += 1

print "Least number is", num
