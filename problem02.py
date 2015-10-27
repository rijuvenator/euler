# Problem 2: Find the sum of the even terms of the Fibonnaci sequence less than four million.
# Answer: 4613732
print '** Problem 2 **'

answer = 0 

def fib(x,y,answer):
	if x > 4000000:
		print "Sum is",answer
		return
	if x%2 == 0: 
		answer = answer + x	
	fib(y,x+y,answer)

fib(1,2,0)


