# -*- coding: utf-8 -*-
import math, random, timeit

def isprime(q,k=50):
	q = abs(q)
#	if q == 2: return True
#	if q < 2 or q&1 == 0: return False

	d = (q-1)>>1
	while d&1 == 0:
		d >>= 1

	for i in xrange(k):
		a = random.randint(1,q-1)
		t = d
		y = pow(a,t,q)
		while t != q-1 and y != 1 and y != q-1: 
			y = pow(y,2,q)
			t <<= 1
		if y != q-1 and t&1 == 0:
			return False
	return True
#	if n == 2: return True
#	elif n&1 == 0 or n < 2:	return False
#	else: return (pow(2, n-1, n) == 1)

n = 2000000
primes = [2, 3, 5, 11, 13]
i = 17
while (i<n+1):
	if (isprime(i)):primes.append(i)
	i += 2
	if (isprime(i)):primes.append(i)
	i += 4

sum = reduce(lambda x, y:x+y, primes)

print "ans = %d" % (sum)
pause =raw_input("pause")
