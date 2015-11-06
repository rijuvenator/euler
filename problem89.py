# Problem 89: Find the number of characters saved by writing the Roman numbers in the given text file in their minimal form.
# Answer: 
print '** Problem 89 **'

romedict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
invromedict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

f = open("files/p089_roman.txt")

def toRoman(num):
	output = ""
	tmpNum = num+1
	# basic
	for numeral in [1000, 500, 100, 50, 10, 5, 1]:
		while tmpNum > numeral:
			output += invromedict[numeral]
			tmpNum -= numeral
	# subtractive combinations
	output = output.replace("DCCCC","CM")
	output = output.replace("CCCC","CD")
	output = output.replace("LXXXX","XC")
	output = output.replace("XXXX","XL")
	output = output.replace("VIIII","IX")
	output = output.replace("IIII","IV")
	return output

extrachars = 0
for line in f:
	# this one will be changed to be strictly descending
	romannumber = line[:-1]
	# this one is the original
	realromannumber = line[:-1]
	# backwards!
	romannumber = romannumber.replace("CM","DCCCC")
	romannumber = romannumber.replace("CD","CCCC")
	romannumber = romannumber.replace("XC","LXXXX")
	romannumber = romannumber.replace("XL","XXXX")
	romannumber = romannumber.replace("IX","VIIII")
	romannumber = romannumber.replace("IV","IIII")
	# now the number is simply the sum of the strictly descending numeral
	number = sum([romedict[i] for i in romannumber])
	minimalromannumber = toRoman(number)
	extrachars += len(realromannumber) - len(minimalromannumber)

print "Characters saved is",extrachars
