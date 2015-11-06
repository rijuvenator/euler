# Problem 22: Find the sum of name scores in the given text file, where NS = (sorted position) * (letter sum).
# Answer: 871198282
print '** Problem 22 **'

# I have already processed this file to have a different word on every line with no other special characters.
f = open('files/p022_names.txt')

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

names = []
for line in f:
	names.append(line)

names.sort()

scoresum = 0
for index,name in enumerate(names):
	chars = [i for i in name]
	chars.pop()
	num = sum([chardict[i] for i in chars])
	score = (index+1)*num
	scoresum += score

print "Total of name scores is",scoresum
