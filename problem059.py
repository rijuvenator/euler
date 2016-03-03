# Problem 59: Decrypt the given file with a 3-lowercase-letter-key XOR and find the sum of the decrypted ASCII values.
# Answer: 107359

import itertools

print '** Problem 59 **'

f = open('files/p059_cipher.txt','r')
enc = [int(x) for x in f.readline().strip().split(',')]

def listToString(nums):
	return "".join([chr(x) for x in nums])

lowercases = 'abcdefghijklmnopqrstuvwxyz'

# Cartesian product of lowercase letters, i.e. aaa, aab, aac, ...
enckeys = ["".join(i) for i in list(itertools.product(lowercases,repeat=3))]

# try all the keys
for key in enckeys:
	charlist = [ord(x) for x in key]
	dec = [x^charlist[index%3] for index,x in enumerate(enc)]
	ctcand = listToString(dec)
	# No frequency analysis required! I simply looked for ' the ', hoping that it would be present. And it was.
	if ctcand.find(" the ") > 0:
		# I ran this once already. It's the Gospel of John, Chapter 1.
		# print ctcand
		print 'Sum of the ASCII values is',sum(dec)
		break
