# Problem 54: How many hands does Player 1 win in the given text file?
# Answer: 376
print '** Problem 54 **'

class Card:
	def __init__(self,card):
		values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
		self.number = card[0]
		self.suit = card[1]
		self.value = values[self.number]

class Hand:
	def __init__(self,hand):
		self.hand = []
		self.vals = []
		self.suits = []

		for card in hand.split():
			currentCard = Card(card)
			self.hand.append(currentCard)
			self.vals.append(currentCard.value)
			self.suits.append(currentCard.suit)

		self.vals.sort()

		self.counts = dict((x,self.vals.count(x)) for x in set(self.vals))
	
	def determineHand(self):
		if self.isRoyalFlush():
			return 9
		elif self.isStraightFlush():
			return 8
		elif self.isFourOfAKind():
			return 7
		elif self.isFullHouse():
			return 6
		elif self.isFlush():
			return 5
		elif self.isStraight():
			return 4
		elif self.isThreeOfAKind():
			return 3
		elif self.isTwoPairs():
			return 2
		elif self.isOnePair():
			return 1
		else:
			return 0

	def isOnePair(self):
		if self.counts.values().count(2) == 1 and set(self.counts.values()) == set([1,2]):
			return True
		else:
			return False

	def isTwoPairs(self):
		if self.counts.values().count(2) == 2:
			return True
		else:
			return False
	
	def isThreeOfAKind(self):
		if 3 in self.counts.values() and 2 not in self.counts.values():
			return True
		else:
			return False

	def isStraight(self):
		firstVal = self.vals[0]
		if self.vals == range(firstVal,firstVal+5):
			return True
		else:
			return False

	def isFlush(self):
		if len(set(self.suits)) > 1:
			return False
		else:
			return True

	def isFullHouse(self):
		if 2 in self.counts.values() and 3 in self.counts.values():
			return True
		else:
			return False

	def isFourOfAKind(self):
		if 4 in self.counts.values():
			return True
		else:
			return False

	def isStraightFlush(self):
		if self.isFlush() and self.isStraight():
			return True
		else:
			return False

	def isRoyalFlush(self):
		if self.isStraightFlush() and self.vals[0] == 10:
			return True
		else:
			return False


f = open('files/p054_poker.txt')

count = 0
handDict = {0:"High Card",1:"One Pair",2:"Two Pairs",3:"Three of a Kind",4:"Straight",5:"Flush",6:"Full House",7:"Four of a Kind",8:"Straight Flush",9:"Royal Flush"}
for line in f:
	hand1 = Hand(line[0:14])
	hand2 = Hand(line[15:29])
	hand1rank = hand1.determineHand()
	hand2rank = hand2.determineHand()
	if hand1rank > hand2rank:
		count += 1
	elif hand1rank == hand2rank:
		# In this file, the only equal-rank hands are either high card or one pair, so it remains to merely distinguish between the two
		# A more complete solution would have methods to distinguish all equal-rank hands
		if hand1rank == 0:
			i = 4
			while hand1.vals[i] == hand2.vals[i]:
				i -= 1
			if hand1.vals[i] > hand2.vals[i]:
				count += 1
		elif hand1rank == 1:
			hand1counts = dict((counter,key) for key,counter in hand1.counts.iteritems())
			hand2counts = dict((counter,key) for key,counter in hand2.counts.iteritems())
			if hand1counts[2] > hand2counts[2]:
				count += 1
			elif hand1counts[2] == hand2counts[2]:
				i = 4
				while hand1.vals[i] == hand2.vals[i]:
					i -= 1
				if hand1.vals[i] > hand2.vals[i]:
					count += 1
			elif hand1counts[2] < hand2counts[2]:
				pass

print "Player 1 wins",count,"hands"
