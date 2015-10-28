# Problem 32: Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# Answer: 45228
print '** Problem 32 **'

nums = [i for i in range(5000) if len(set([j for j in str(i)])) == len(str(i)) and "0" not in [j for j in str(i)]]

prods = []
for i in nums:
	for j in nums[nums.index(i)+1:]:
		leftside = str(i)+str(j)
		if len(set([k for k in leftside])) != len(leftside):
			continue
		prod = i*j
		allofit = leftside+str(prod)
		if "0" in [k for k in str(prod)]:
			continue
		if len(allofit) != 9:
			continue
		if len(set([k for k in allofit])) != 9:
			continue
		prods.append(prod)

print "Sum is",sum(set(prods))
