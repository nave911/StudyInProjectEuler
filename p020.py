# -*- coding: utf-8 -*-
import sys, math

def Factorial(n):
	return reduce(lambda x, y: x*(y+1), range(n), 1)

st = str(Factorial(100))
print reduce(lambda x, y: x+int(y), st, 0)
pause =raw_input("pause")
