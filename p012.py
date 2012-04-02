# -*- coding: utf-8 -*-
import math, timeit, re

primes = {}
def isprime(n):
	if not (primes.has_key(n)):
		if n == 2: primes[n] = True
		elif n < 2 or n&1 == 0:	primes[n] = False
		else: primes[n] = (pow(2, n-1, n) == 1)
	return primes[n]

def factorize(n):
	fac = {}
	if (isprime(n)):
		fac = {n: 1}
	else:
		for p in range(2, n/2+1):
			if not(isprime(p)):continue
			while (n%p==0):
				n = n/p
				if (fac.has_key(p)):
					fac[p] = fac[p] + 1
				else:
					fac[p] = 1
			if (n == 1):break
	return fac
#	return [(k, v) for k,v in fac.iteritems()]

n = 500 - 1
i = 3
while True:
	if (isprime(i)):
		f0 = factorize((i + 1) / 2)
		f1 = {i : 1}
	elif (i%2==1):
		f0 = factorize((i + 1) / 2)
		f1 = factorize(i)
	else:
		f0 = factorize(i / 2)
		f1 = factorize(i + 1)

	for k, v in f0.items():
		if not(f1.has_key(k)):f1[k] = 0
		f1[k] += v
	if (n < reduce(lambda x, y: x*y, [v+1 for v in f1.values()], 1)):
		break
	i += 1

print "%d : %d" % (i, i*(i+1)/2)
pause =raw_input("pause")
