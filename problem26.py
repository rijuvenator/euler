# Problem 26: Find d<1000 such that the decimal expansion of 1/d has the longest repeating part.
# Answer: 983
print '** Problem 26 **'

class Decimal():
	def __init__(self,numerator,denominator):
		self.d = denominator
		self.currentDividend = numerator 
		self.quotient = []
		self.mods = []
		self.repeating = False
		self.repeatLength = 0
	def divide(self):
		self.quotient.append(self.currentDividend/self.d)
		self.currentRemainder = (self.currentDividend%self.d)
		if self.currentRemainder == 0:
			return	
		else:
			if self.currentRemainder not in self.mods:
				self.mods.append(self.currentRemainder)
				self.currentDividend = 10*self.currentRemainder
				self.divide()
			else:
				self.repeating = True
				self.repeatLength = len(self.mods) - self.mods.index(self.currentRemainder)
				return
	def display(self):
		print str(self.quotient[0]) + '.' + ''.join([str(i) for i in self.quotient[1:]])

currentD = 1
currentMax = 0
for d in range(1,1001):
	x = Decimal(1,d)
	x.divide()
	if x.repeating and x.repeatLength > currentMax:
		currentMax = x.repeatLength
		currentD = d

print "Longest repeating decimal is in 1/"+str(currentD)
