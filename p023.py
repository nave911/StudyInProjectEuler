# -*- coding: utf-8 -*-
import sys, math

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
	return [(k, v) for k,v in fac.iteritems()]

def factor(n):
	fac = factorize(n)
	nf = len(fac)
	f = [0] * nf
	ans = []
	while True:
		ans.append(reduce(lambda x, y: x*y, [fac[x][0]**f[x] for x in range(nf)], 1))
		i = 0
		while True: 
			f[i] += 1 
			if f[i] <= fac[i][1]: 
				break 
			f[i] = 0 
			i += 1 
			if i >= nf: 
				return ans

dd = {}
def d(n):
	if not (dd.has_key(n)):
		dd[n] = reduce(lambda x, y: x+y, factor(n), 0)
	return dd[n]

def isAmicable(n):
	if (d(d(n)) == n):return True

def isPerfect(n):
	if (d(n) == n):return True

def isAbundant(n):
	if (d(n) > n):return True

def isDeficient(n):
	if (d(n) < n):return True

limit = 28123
abundants = filter(isAbundant, range(3, limit+1))

notab2 = range(1, limit+1)
for i in range(len(abundants)):
	for j in range(i, len(abundants)):
		k = abundants[i]+abundants[j]
		if (limit<k):break
		if (0 < notab2.count(k)):notab2.remove(k)

print "sum : " + str(reduce(lambda x, y: x+y, notab2))
pause =raw_input("pause")
