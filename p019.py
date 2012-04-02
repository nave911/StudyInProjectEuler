# -*- coding: utf-8 -*-
import sys, math

days365 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days366 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days(y):
	if ((y%4!=0)or((y%400!=0)and(y%100==0))):
		return days365
	return days366

def count(y):
	c = 0
	s = 0
	for i in range(1900, y):
		d = days(i)
		for j in d:
			if (s%7==6):
				c += 1
			s += j
	return c

print count(2001) - count(1901)

pause =raw_input("pause")
