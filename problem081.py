# Problem 81: Find the minimal path sum of the given 80x80 matrix.
# Answer: 427337
print '** Problem 81 **'

#matrix = [[1,2,3,4],[4,5,6,8],[9,10,11,12],[13,14,15,16]]

f = open("files/p081_matrix.txt")
matrix = [[0 for j in range(80)] for i in range(80)]
for j,line in enumerate(f):
	matrix[j] = [int(i) for i in line.strip("\n").split(",")]

nrow = len(matrix) - 1
ncol = len(matrix[0]) - 1

sums = [[0 for i in range(nrow + 1)] for j in range(ncol + 1)]

# refer to this diagram to understand what's going on below
#
#  X b b b B
#  a d d d d
#  a d d d d
#  a d d d d
#  A d d d M

for i in range(nrow,-1,-1):
	if i == nrow:
		# fills M
		sums[i][ncol] = matrix[i][ncol]
	else:
		# fills B = matrix(B) + sums(d below B)
		sums[i][ncol] = matrix[i][ncol] + sums[i+1][ncol]
		# fills A = matrix(A) + sums(d right A)
		sums[nrow][i] = matrix[nrow][i] + sums[nrow][i+1]
		
		for j in range(i+1,ncol):
			# fills b = matrix(b) + min(sums(d below), sums(b right))
			sums[i][i+ncol-j] = matrix[i][i+ncol-j] + min(sums[i][i+ncol-j+1], sums[i+1][i+ncol-j])
			# since nrow = ncol in this problem, do in same for loop
			# fills a = matrix(a) + min(sums(d right), sums(a below))
			sums[i+nrow-j][i] = matrix[i+nrow-j][i] + min(sums[i+nrow-j+1][i], sums[i+nrow-j][i+1])
		
		# fills X = min(sums(b right), sums(a below))
		sums[i][i] = min(matrix[i][i] + sums[i][i+1], matrix[i][i] + sums[i+1][i])

print "Minimal path sum is", sums[0][0]
