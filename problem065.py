# Problem 65: Find the sum of the digits of the denominator of the 100th convergent of the continued fraction expansion for e.
# Answer: 272
print '** Problem 65 **'

class Fraction:
	def __init__(self, a, b=1):
		self.num = a
		self.den = b
		self.reduce()
	
	def __repr__(self):
		return str(self.num)+"/"+str(self.den)

	def gcd(self, a, b):
		while b:
			a, b = b, a % b
		return a

	def lcm(self, a, b):
		return a / self.gcd(a, b) * b

	def reduce(self):
		g = self.gcd(self.num, self.den)
		self.num = self.num / g
		self.den = self.den / g

	def __div__(self, second):
		x = Fraction(self.num * second.den, self.den * second.num)
		x.reduce()
		return x

	def __add__(self, second):
		l = self.lcm(self.den, second.den)
		la = self.num * l / self.den
		ra = second.num * l / second.den
		x = Fraction(la + ra, l)
		x.reduce()
		return x

	def approx(self):
		return float(self.num)/float(self.den)

num = 100 
terms = [1] * num
for i in range(0,num/3):
	terms[2 + 3*i] = 2*(i+1)
terms[0] = 2

#terms = [2] * num
#terms[0] = 1

def nextTerm(i):
	if i < num-1:
		z = nextTerm(i+1)
		return Fraction(terms[i]) + (Fraction(1) / Fraction(z.num, z.den))
	else:
		return Fraction(terms[i])

x = nextTerm(0)
s = [int(i) for i in str(x.num)]
print "Sum is", sum(s)
