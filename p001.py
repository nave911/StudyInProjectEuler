# -*- coding: utf-8 -*-

n = 10
array = []
for c in range(1, 1000):
	if (c%3==0)|(c%5==0):
		array.append(c)

sum = reduce(lambda x, y:x+y, array)
print sum
pause =raw_input("pause")
