# Problem 102: Find the number of triangles that contain the origin in the given file.
# Answer: 228
print '** Problem 102 **'

f = open("files/p102_triangles.txt")
triangles = [[] for i in range(1000)]
for i,line in enumerate(f):
	triangles[i] = [int(x) for x in line.split(",")]

count = 0
for tri in triangles:
	x = tri[0::2]
	y = tri[1::2]
	
	if min(x)*max(x) > 0 or min(y)*max(y) > 0:
		continue

	a = float((y[1] - y[2])*(-x[2]) + (x[2] - x[1])*(-y[2])) / float((y[1] - y[2])*(x[0] - x[2]) + (x[2] - x[1])*(y[0] - y[2]))
	b = float((y[2] - y[0])*(-x[2]) + (x[0] - x[2])*(-y[2])) / float((y[1] - y[2])*(x[0] - x[2]) + (x[2] - x[1])*(y[0] - y[2]))
	c = 1 - a - b

	if not (0 <= a and a <= 1 and 0 <= b and b <= 1 and 0 <= c and c <= 1):
		continue

	count += 1

print "Number of triangles is", count
