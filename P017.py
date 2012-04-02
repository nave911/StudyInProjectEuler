# -*- coding: utf-8 -*-
import sys, math, re

n = 1000

num_a = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
num_b = ['zero', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
letters = 0
for i in range(1, n+1):
	s = ''
	l2 = int(('00' + str(i))[-2:])
	if (l2<20):
		s = num_a[l2]
	else:
		s = num_b[int(str(i)[-2])] + ' ' + num_a[int(str(i)[-1])]

	h = ('000'+str(i))[-3]
	if (h != '0'):
		if (str(i)[-2:]=='00'):
			s = num_a[int(h)] + ' hundred ' + s
		else:
			s = num_a[int(h)] + ' hundredand ' + s

	t = ('0000'+str(i))[-4]
	if (t != '0'):
		if (str(i)[-3:]=='000'):
			s = num_a[int(t)] + ' thousand ' + s
		else:
			s = num_a[int(t)] + ' thousand and ' + s
	
	print s
	letters += len(re.sub(' ', '', s))

print letters
pause =raw_input("pause")
