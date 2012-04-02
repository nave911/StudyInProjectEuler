# -*- coding: utf-8 -*-
import math

def factor(n):
	f = []
	i = 2
	while True:
		if (n%i==0):
			f.append(i)
			n = n/i
		else:
			i += 1
		if (n<i*i):break
	f.append(n)
	return list(set(f))

ans = factor(600851475143)
print ans
print reduce(lambda x,y: x*y, ans)
pause =raw_input("pause")
