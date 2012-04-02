# -*- coding: utf-8 -*-
import sys, math

n = 1000000

gb = {1:1}
def goldbach(n):
	if not (gb.has_key(n)):
		if(n%2==0):
			gb[n] = goldbach(n/2) + 1 
		else:
			gb[n] = goldbach((3*n) + 1) + 1 
	return gb[n]

m = (0, 0)
for i in range(2, n+1):
	g = goldbach(i)
	if (m[1] < g):m = (i, g)

print m
pause =raw_input("pause")
