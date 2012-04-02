# -*- coding: utf-8 -*-
import sys, math

def factorial(n):
	if n==1:return 1
	return n*factorial(n-1)

def swap(ary, m, n):
	ary[m], ary[n] = ary[n], ary[m]

N = 10
NO = 1000000
stock = range(N)

a = 0
no = NO - 1
ans = []
for i in range(N):
	f = factorial(N-i)
	no -= a*f
	a = no / (f/(N-i))
	ans.append(stock[a])
	stock.remove(stock[a])
	stock.sort()

print ans
pause =raw_input("pause")
