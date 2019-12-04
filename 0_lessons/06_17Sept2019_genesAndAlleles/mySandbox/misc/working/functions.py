#*************************************
# Honor Code: This work is mine unless otherwise cited.
# Janyl Jumadinova
# CMPSC 300 Spring 2016
# Class Example
# Date: February 11, 2016

# Purpose: illustrating functions
#*************************************

# here we define/implement the function that sums up 
# the squares up to n
# Note: body of function is indented (one tab == 4 spaces)
def compSumOfSquares(n):
	listOfNo = range(n+1)
	sum = 0
	for no in listOfNo:
		sum = sum + no**2
	return sum 

# the function can be invoked many times
print "Sum of squares up to 3 is: ", compSumOfSquares(3)
print "Sum of squares up to 105 is: ", compSumOfSquares(105)


