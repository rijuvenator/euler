# Problem 4: Find the largest palindrome made from the product of two 3-digit numbers.
# Answer: 906609
print '** Problem 4 **'

# This is my lovely recursive isPalindrome function.
# Unfortunately, python has built-in ways to reverse things.
#
#def isPalindrome(x):
#	if len(str(x)) > 2:
#		if str(x)[-1] == str(x)[0]:
#			return isPalindrome(str(x)[1:len(str(x))-1])
#		else:
#			return False
#	elif len(str(x)) == 2:
#		if str(x)[0] == str(x)[1]:
#			return True
#		else:
#			return False
#	elif len(str(x)) == 1:
#		return True

def isPalindrome(x):
	if str(x)[::-1] == str(x):
		return True
	else:
		return False

maxPal = 0
for i in range(1000):
	for j in range(i):
		currentPal = (999-i)*(999-j)
		if isPalindrome(currentPal) and maxPal < currentPal:
			maxPal = currentPal

print "Largest palindrome is",maxPal
