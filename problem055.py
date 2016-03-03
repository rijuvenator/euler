# Problem 55: How many Lychrel numbers are there below 10,000?
# Answer: 249
print '** Problem 55 **'

def isPalindrome(num):
	if str(num) == "".join(reversed(list(str(num)))):
		return True
	else:
		return False

def stepOne(num):
	return num + int("".join(reversed(list(str(num)))))

lychrels = [True] * 10000
lychrels[0] = False

for i in range(10000):
	current = i
	iterations = 0
	while iterations < 50:
		current = stepOne(current)
		iterations += 1
		if isPalindrome(current):
			lychrels[i] = False
			break

print "Number of Lychrel numbers less than 10,000 is",len([i for i,j in enumerate(lychrels) if j])

