# Problem 206: Find the integer whose square has the form 1_2_3_4_5_6_7_8_9_0.
# Answer: 1389019170
print '** Problem 206 **'

# A square that ends in zero is divisible by 10, therefore its square root is divisible by 10, therefore
# the second to last digit is also a 0. Strip them and we have 100x fewer numbers to check.
# The square root of 1_2_3_4_5_6_7_8_9 is bounded by 1e8 and sqrt(2)e8. Also, it has to be odd. Thus,
# Further edit: for its square to end in 9, a number must end in either 3 or 7.

# all possible candidates
squares = [i**2 for i in range(int(1e8)+1, int(2**(0.5)*1e8)+1,2) if str(i)[-1] == '3' or str(i)[-1] == '7']
# find the only square whose concatenation of even indices is the string '123456789'
onlyone = [i for i in squares if "".join([str(i)[j] for j in range(0,17,2)]) == '123456789']
# replace the 00 and take the square root
print 'Integer is', int((onlyone[0]*100)**(0.5))
