#!/usr/bin/env python

'''
Speed Converter
'''

def ConvertMPHtoMS(speed_mph):
	speed_MS = speed_mph * .447
	return speed_MS

x=25 #mph
y=ConvertMPHtoMS(x) #MS

print str(x) + " mph is " + str(y) + " m/s"


