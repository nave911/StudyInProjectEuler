# -*- coding: utf-8 -*-

primes = {}
def isprime(n):
	if not (primes.has_key(n)):
		if n == 2: primes[n] = True
		elif n < 2 or n&1 == 0:	primes[n] = False
		else: primes[n] = (pow(2, n-1, n) == 1)
	return primes[n]

def checkprimegen(a, b):
	n = 0
	while True:
		x = n*n + a*n + b
		if (isprime(x)==False):break
		n += 1
	return n-1

m, n = 0, {'a':0, 'b':0}
for a in range(-999, 1000+1, 2):
	for b in range(1000+1):
		if (isprime(b)):
			c = checkprimegen(a, b)
			if (m < c):
				m, n = c, {'a':a, 'b':b}

print m
print n
print 'a * b = ' + str(n['a']*n['b'])

#a, b = -61, 971
#for n in range(70+1):
#	print n*n + a*n + b

pause = raw_input("pause")
