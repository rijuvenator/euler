# Problem 38: Find the largest pandigital number that can be formed as the concatenated product of an integer with (1,..n), where n > 1?
# Answer: 932718654
print '** Problem 38 **'

currentMax = 0
for i in range(10000):
	num = str(i)
	mult = 2
	while len(num) < 9:
		num += str(i*mult)
		mult += 1
	if "0" in num:
		continue
	if len(num) == 9:
		if len(set([j for j in num])) == 9:
			if int(num) > currentMax:
				currentMax = int(num)

print "Largest pandigital number is",currentMax
