# Problem 19: How many Sundays fell on the first of the month between 1 Jan 1901 and 31 Dec 2000?
# Answer: 171
print '** Problem 19 **'

def daysFromDayOne(month,year):
	days = 0
	leapYear = False
	if year%4 == 0:
		leapYear = True
	numberOfLeapYears = (year - 1900)/4
	days = days + (year - 1901)*365 + numberOfLeapYears
	thisYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	days = days + sum(thisYear[0:month-1]) + leapYear * (month > 2)
	return days%7 == 0

number = 0
for year in range(1901,2001):
	for month in range(1,13):
		if daysFromDayOne(month,year):
			number = number + 1

print 'Number of Sundays is',number
