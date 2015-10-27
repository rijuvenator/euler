# Problem 15: How many two-player Nim games of heap size 20 are there?
# Answer: 137846528820 
print '** Problem 15 **'

data = {(1,0):1}
def routes(x,y):
	if x == 0 or y == 0:
		return 1
	else:
		if (max(x,y),min(x,y)) in data.keys():
			return data[(max(x,y),min(x,y))]
		else:
			data[(max(x,y),min(x,y))] = routes(x-1,y) + routes(x,y-1)
			return data[(max(x,y),min(x,y))]

print "Number of paths is",routes(20,20)
