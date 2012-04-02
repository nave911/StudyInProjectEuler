# -*- coding: utf-8 -*-
import sys, math

def Combi(m, n):
	u = reduce(lambda x, y: x*y, range(m, m-n, -1), 1)
	d = reduce(lambda x, y: x*y, range(n, 1, -1), 1)
	return u/d

n = 20
print Combi(2*n, n)
pause =raw_input("pause")
