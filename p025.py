# -*- coding: utf-8 -*-
import sys, math

fibo = [1, 1]
n = 2
while True:
	fibo.append(fibo[n-2] + fibo[n-1])
	n += 1
	if (1000<=len(str(fibo[-1]))):break

print "fibo[" + str(n) + "]:" + str(fibo[-1])
pause =raw_input("pause")