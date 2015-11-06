# Problem 17: How many letters are used in writing out the numbers from 1 to 1000?
# Answer: 21124
print '** Problem 17 **'

convert = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve'}
decades = {2:'twen',3:'thir',4:'for',5:'fif',6:'six',7:'seven',8:'eigh',9:'nine'}
def numInWords(n):
	if n < 13:
		return convert[n]
	elif n > 12 and n < 20:
		s = int(str(n)[-1])
		if s == 3:
			cat = 'thir'
		elif s == 5:
			cat = 'fif'
		elif s == 8:
			cat = 'eigh'
		else:
			cat = convert[s]
		return cat + 'teen'
	elif n > 19 and n < 100:
		ones = convert[int(str(n)[-1])]
		tens = decades[int(str(n)[0])]
		return tens + 'ty' + ones
	else:
		hund = convert[int(str(n)[0])]
		rest = numInWords(int(str(n)[1:]))
		if rest == '':
			x = ''
		else:
			x = 'and'
		return hund + 'hundred' + x + rest

total = 0
for i in range(999):
	total += len(numInWords(i+1))

total += 11
print 'Number of letters is',total
