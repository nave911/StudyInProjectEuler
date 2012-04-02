# -*- coding: utf-8 -*-
import sys, math

n = 100
sqares = {}
for a in range(2, n+1):
	for b in range(2, n+1):
		sqares[int(math.pow(a, b))] = True

print len(sqares)
pause = raw_input("pause")
