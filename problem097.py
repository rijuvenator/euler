# Problem 97: Find the last ten digits of 28433 * 2^7830457 + 1.
# Answer: 8739992577
print '** Problem 97 **'

# Looks like python will do it for me

print "Last ten digits are", (28433 * (2**7830457) + 1)%(10**10)
