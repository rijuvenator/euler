# Problem 57: Find the number of expansions of sqrt(2) with more digits in the numerator than denominator.
# Answer: 153
print '** Problem 57 **'

# Xaphiosis's code. Runs faster than mine, so I don't have to blacklist :\
def expand(n):
	(num,den) = (1,2)
	for i in range(1, n):
		(num,den) = (den,num + 2*den)
	return (num,den)

def nth(n):
	(num,den) = expand(n)
	return len(str(num+den)) > len(str(den))

counter = 0
for n in range(0, 1000):
	if nth(n+1): counter += 1

print "Number of top-heavy expansions is", counter

#import sys
#sys.setrecursionlimit(2000)
#
#class Fraction:
#	def __init__(self, a, b=1):
#		self.num = a
#		self.den = b
#		self.reduce()
#	
#	def __repr__(self):
#		return str(self.num)+"/"+str(self.den)
#
#	def gcd(self, a, b):
#		while b:
#			a, b = b, a % b
#		return a
#
#	def lcm(self, a, b):
#		return a / self.gcd(a, b) * b
#
#	def reduce(self):
#		g = self.gcd(self.num, self.den)
#		self.num = self.num / g
#		self.den = self.den / g
#
#	def __div__(self, second):
#		x = Fraction(self.num * second.den, self.den * second.num)
#		x.reduce()
#		return x
#
#	def __add__(self, second):
#		l = self.lcm(self.den, second.den)
#		la = self.num * l / self.den
#		ra = second.num * l / second.den
#		x = Fraction(la + ra, l)
#		x.reduce()
#		return x
#
#	def approx(self):
#		return float(self.num)/float(self.den)
#
#count = 0
#for i in range(1,1002):
#	num = i
#	terms = [2] * num
#	terms[0] = 1
#
#	def nextTerm(i):
#		if i < num-1:
#			z = nextTerm(i+1)
#			return Fraction(terms[i]) + (Fraction(1) / Fraction(z.num, z.den))
#		else:
#			return Fraction(terms[i])
#
#	x = nextTerm(0)
#	if len(str(x.num)) > len(str(x.den)):
#		count += 1
##		print "Term", i-1, "has a top-heavy numerator."
#
#print "Number of top-heavy expansions is", count
