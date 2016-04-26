# Problem 213: Find the expected value of empty square occupancy with jumping fleas.
# Answer: 

import random

# Direction map to randints
#   0
# 3   1
#   2
#
# 0 = UP
# 1 = RIGHT
# 2 = DOWN
# 3 = LEFT


class Grid:
	def __init__(self, size):
		self.size = size
		self.current = [[1 for i in range(size)] for j in range(size)]
		self.modify = [[0 for i in range(size)] for j in range(size)]

	def reset(self):
		self.current = [[1 for i in range(self.size)] for j in range(self.size)]

	def fillModify(self):
		self.modify = [[0 for i in range(self.size)] for j in range(self.size)]
		for i in range(self.size):
			for j in range(self.size):
				for flea in range(self.current[i][j]):
					x = self.getRand(i,j)
					if x == 0:
						self.modify[i-1][j] = self.modify[i-1][j] + 1
					elif x == 1:
						self.modify[i][j+1] = self.modify[i][j+1] + 1
					elif x == 2:
						self.modify[i+1][j] = self.modify[i+1][j] + 1
					elif x == 3:
						self.modify[i][j-1] = self.modify[i][j-1] + 1

	def getRand(self,i,j):
		x = 0
		if i == 0 and j == 0:
			x = random.randint(1,2)
		elif i == 0 and j == self.size-1:
			x = random.randint(2,3)
		elif i == 0:
			x = random.randint(1,3)
		elif i == self.size-1 and j == 0:
			x = random.randint(0,1)
		elif i == self.size-1 and j == self.size-1:
			x = random.randint(0,1)*3
		elif i == self.size-1:
			x = random.randint(1,3); x -= 2 * (x == 2)
		elif j == 0:
			x = random.randint(0,2)
		elif j == self.size-1:
			x = random.randint(2,4); x -= 4 * (x == 4)
		else:
			x = random.randint(0,3)
		return x

	def jump(self):
		self.fillModify()
		self.current = self.modify

	def printGrid(self):
		for i in range(self.size):
			for j in range(self.size):
				print self.current[i][j]," ",
			print ""
	
	def countEmpty(self):
		count = 0
		for i in range(self.size):
			for j in range(self.size):
				if self.current[i][j] == 0:
					count += 1
		return count

gridsize = 30
jumps = 50
trials = 100

flea = Grid(gridsize)
empties = [0] * trials

for j in range(trials):
	for i in range(jumps):
		flea.jump()
	empties[j] = flea.countEmpty()

print float(sum(empties))/float(trials)
