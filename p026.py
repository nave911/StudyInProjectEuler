# -*- coding: utf-8 -*-
import sys, math
from decimal import *

ans = {0:0}
for i in range(1, 1000):
	mod = {}
	m = 1
	c = 0
	while True:
		d = int (m / i)
		m = m % i
		if (mod.has_key(m)):break
		mod[m] = True
		m = 10 * m
		c += 1
	ans[i] = c

k = ans.keys()
k.sort(cmp=lambda a,b: cmp(ans[a],ans[b]), reverse=True)
print str(k[0]) + " : " + str(ans[k[0]])
getcontext().prec = 1000
print Decimal(1)/Decimal(k[0])
pause = raw_input("pause")
