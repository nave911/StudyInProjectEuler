# -*- coding: utf-8 -*-
import math, timeit

n = 1000

for a in range(1, n-1):
	for b in range(a+1, n):
		c = math.sqrt(a*a+b*b)
		if (a+b+c==n)and(int(c)==c):
			print 'a: %d, b: %d, c: %d' % (a, b, c)
			print '%d^2 + %d^2 = %d^2' % (a, b, c)
			print '%d + %d = %d' % (a*a, b*b, c*c)
pause =raw_input("pause")
