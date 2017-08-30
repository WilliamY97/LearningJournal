# Given an integer, , traverse its digits (1,2,...,n) and determine how many digits evenly divide  (i.e.: count the number of times
# divided by each digit i has a remainder of ). Print the number of evenly divisible digits.

def findDigits(num):
	l = [int(x) for x in str(num)]
	c = 0
	for x in l:
	    if x is not 0 and num is not 0 and num % x == 0:
	        c += 1
	print c

findDigits(124) #3
findDigits(12) #2
findDigits(1012) #3
