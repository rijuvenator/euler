# Problem 42: Find the number of words in the given text file whose alphabetical positionwise letter sum is a triangle number.
# Answer: 162
print '** Problem 42 **'

# I have already processed this file to have a different word on every line with no other special characters.
f = open('files/p042_words.txt')

chardict = {
	'A':1,
	'B':2,
	'C':3,
	'D':4,
	'E':5,
	'F':6,
	'G':7,
	'H':8,
	'I':9,
	'J':10,
	'K':11,
	'L':12,
	'M':13,
	'N':14,
	'O':15,
	'P':16,
	'Q':17,
	'R':18,
	'S':19,
	'T':20,
	'U':21,
	'V':22,
	'W':23,
	'X':24,
	'Y':25,
	'Z':26
}

def isTriangle(num):
	x = float(-1 + (1 + 4*2*num)**(0.5))/2.
	y = float(int(x))
	if (x-y)<0.0000001:
		return True
	else:
		return False

count = 0
for line in f:
	chars = [i for i in line]
	chars.pop()
	num = sum([chardict[i] for i in chars])
	count += isTriangle(num)

print "Number of triangle words is",count
