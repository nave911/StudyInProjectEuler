# -*- coding: utf-8 -*-
import sys, math

def score(name):
	s = 0
	for n in name:
		if n!='"':
			s += ord(n) - ord('A') + 1
	return s
	
names = []
for line in open('names.txt', 'r'):
    names.extend(line[:-1].split(','))

names.sort()
print reduce(lambda x, y: x+y, [(i+1) * score(names[i]) for i in range(len(names))], 0)
pause =raw_input("pause")
