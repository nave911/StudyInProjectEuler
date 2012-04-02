# -*- coding: utf-8 -*-

fib = [1, 2]
def fibo(n):
	if (len(fib)<n):
		for i in range(n - len(fib)):
			fib.append(fib[-2] + fib[-1])
	return fib[:n]

n = 4000000
i = 1
while True:
	if (n < fibo(i).pop()):
		i -= 1
		break
	i += 1

f = fibo(i)
sum = 0
for n in range(i/3):
	sum += f[n*3+1]
print sum
pause =raw_input("pause")
