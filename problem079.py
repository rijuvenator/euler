# Problem 79: What is the shortest passcode possible given the fifty successful 3-digit logins in the given file?
# Answer: 73162890 
print "** Problem 79 **"

# The list is the full fifty logins; find the unique ones to save time
logins = list(set([319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]))

# stringify for convenience
slogins = [str(i) for i in logins]

# This is simply list(set([i for i in "".join(slogins)]))
unique = ['1', '0', '3', '2', '7', '6', '9', '8']

# class for holding a digit and the list of digits that appear to its left and right
class CodeDigit:
	def __init__(self, digit):
		self.digit = digit
		self.left = []
		self.right = []

	def fillLefts(self):
		for x in slogins:
			if x[2] == self.digit:
				if x[1] not in self.left:
					self.left.append(x[1])
				if x[0] not in self.left:
					self.left.append(x[0])
			if x[1] == self.digit:
				if x[0] not in self.left:
					self.left.append(x[0])

	def fillRights(self):
		for x in slogins:
			if x[0] == self.digit:
				if x[1] not in self.right:
					self.right.append(x[1])
				if x[2] not in self.right:
					self.right.append(x[2])
			if x[1] == self.digit:
				if x[2] not in self.right:
					self.right.append(x[2])

# loop through the digits and fill the left and right
CodeDigitList = []
for x in unique:
	z = CodeDigit(x)
	z.fillLefts()
	z.fillRights()
	CodeDigitList.append(z)

# as it turns out, the unique 8 digits are the only 8 digits necessary for the code.
# so loop through the list of left lists, and write down the digit that matches it
ans = ""
for i in range(8):
	for x in CodeDigitList:
		if len(x.left) == i:
			ans += x.digit

print "Shortest passcode is", ans
