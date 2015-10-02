
"""
Compound Interest Calculator
"""


def CompoundInterest (principal):

	index= 0
	rate= .05
	while index<20:
		interest= principal + (principal * rate)
		principal = interest	
		print "${0:0.2f}".format(principal)

		index = index + 1

x= 1000.00
CompoundInterest(x)


