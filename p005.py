# -*- coding: utf-8 -*-
import math, timeit
n = 10

def gcd(a, b):
	while (0<b):a, b = b, (a%b)
	return a
def lcm(a, b):
	return a*b/gcd(a, b)

ans = 1
for i in range(1, n):
	ans = lcm(ans, i+1)

print "n = %d" % (n)
print ans
pause =raw_input("pause")
