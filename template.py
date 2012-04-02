# -*- coding: utf-8 -*-
import sys, math

fib = [1, 2]
def fibonacci(n):
	if (len(fib)<n):
		for i in xrange(n - len(fib)):
			fib.append(fib[-2] + fib[-1])
	return fib[:n]

def gcd(a, b):
	while (0<b):a, b = b, (a%b)
	return a

def lcm(a, b):
	return a*b/gcd(a, b)

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
		for p in xrange(2, n/2+1):
			if not(isprime(p)):continue
			while (n%p==0):
				n = n/p
				if (fac.has_key(p)):
					fac[p] = fac[p] + 1
				else:
					fac[p] = 1
			if (n == 1):break
	return [(k, v) for k,v in fac.iteritems()]

fac = {}
def factor(n):
	if (fac.has_key(n)):
		return fac[n]
	else:
		fa = factorize(n)
		nf = len(fa)
		f = [0] * nf
		fac[n] = []
		while True:
			fac[n].append(reduce(lambda x, y: x*y, [fa[x][0]**f[x] for x in range(nf)], 1))
			i = 0
			while True: 
				f[i] += 1 
				if f[i] <= fa[i][1]: 
					break
				f[i] = 0
				i += 1
				if i >= nf: 
					return fac[n]

def factorial(n):
	return reduce(lambda x, y: x*(y+1), range(n), 1)

def ismirror(n):
	r = False
	if (n == int(str(n)[::-1])) : r = True
	return r

array = range(100)
sum = reduce(lambda x, y:x+y, array)
print sum

pause = raw_input("pause")
