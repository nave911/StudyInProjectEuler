# -*- coding: utf-8 -*-
import sys, math

def factor(n):
	fac = [1]
	i = 2
	while True:
		if (n%i==0):
			fac.append(i)
		if (n/2<i):break
		i += 1
	return fac

def d(n):
	sum = 0
	for i in factor(n):
		sum += i
	return sum

def isAmicable(n):
	if (d(d(n)) == n):return True

def isPerfect(n):
	if (d(n) == n):return True

def isAbundant(n):
	if (d(n) > n):return True

def isDeficient(n):
	if (d(n) < n):return True

def isprime(n, primes):
	if (n%2 == 0): return False
	sqrt = n ** 0.5
	for i in primes:
		if sqrt < i: break
		if n % i == 0: return False
	return True

limit = 28123
primes = [2]
abundants = []
for i in range(3, limit+1):
	if isprime(i, primes):
		primes.append(i)
	elif isAbundant(i):
		abundants.append(i)

notab2 = range(1, limit+1)
for i in range(len(abundants)):
	for j in range(i, len(abundants)):
		k = abundants[i]+abundants[j]
		if (limit<k):break
		if (0 < notab2.count(k)):notab2.remove(k)

sum = 0
for i in notab2:
	sum += i
print "sum : " + str(sum)
pause =raw_input("pause")
