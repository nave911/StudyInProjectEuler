# -*- coding: utf-8 -*-
import math, timeit

n = 10000

def isprime(n, primes):
	sqrt = n ** 0.5
	for i in primes:
		if sqrt < i: break
		if n % i == 0: return False
	return True

primes = [2, 3, 5, 7]
i = 11
while True:
	if isprime(i, primes):
		primes.append(i)
	if (n < len(primes)):break
	i += 2
	if isprime(i, primes):
		primes.append(i)
	if (n < len(primes)):break
	i += 4

print "%d th prime No = %d" % (n, primes.pop())
pause =raw_input("pause")
