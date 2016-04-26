# Problem 99: Find the line number with the largest b^e in the given file.
# Answer:
print '** Problem 99 **'

import math

f = open("files/p099_base_exp.txt")
nums = [[0,0] for i in range(1000)]
maxn = 0
maxl = 0
for i,line in enumerate(f):
	nums[i] = [int(j) for j in line.split(",")]
	if float(nums[i][1]) * math.log(nums[i][0]) > maxn:
		maxn = float(nums[i][1]) * math.log(nums[i][0])
		maxl = i

print "Line number of maximum is", maxl+1
