# Problem 39: Find the perimeter no more than 1000 with the most Pythagorean triples.
# Answer: 840
print '** Problem 39 **'

maxp = 1000
currp = 0
maxc = 0
for p in range(maxp+1):
	count = 0
	for a in range(p/3):
		for b in range((p-a)/2):
			c = p - a - b
			if a**2 + b**2 == c**2:
				count += 1
	if count > maxc:
		maxc = count
		currp = p

print  "Perimeter with most Pythagorean triples is", currp
