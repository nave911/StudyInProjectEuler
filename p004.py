# -*- coding: utf-8 -*-
import math

def ismirror(n):
	s = str(n)
	if (s == s[::-1]) : return True
	return False

m = (0, 0, 0)
n = 3
na = pow(10, n-1)
nb = pow(10, n) - 1
for i in xrange(nb, na, -1):
	for j in xrange(nb, i, -1):
		if ((m[2]<i*j) and ismirror(i*j)):
			m = (i, j, i*j)

print m
pause =raw_input("pause")
