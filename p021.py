# -*- coding: utf-8 -*-
import sys, math

def factor(n):
	f = [1]
	i = 2
	while True:
		if (n%i==0):
			f.append(i)
		if (n/2<i):break
		i += 1
	return f

dd = {}
def d(n):
	if not (dd.has_key(n)):
		dd[n] = reduce(lambda x, y: x+y, factor(n), 0)
	return dd[n]

def isAmicable(n):
	if (d(d(n)) == n):return True

n = 10000
sum = reduce(lambda x, y: x+y, filter(isAmicable, range(2, n+1, 2)))

print "sum of friends : " + str(sum)
pause =raw_input("pause")
