# -*- coding: utf-8 -*-
import sys, math

n = 5
ans = reduce(lambda x,y: x+y, filter(lambda i: i == reduce(lambda x,y: x+y, [pow(int(x), n) for x in str('0'*n+str(i))[-4:]]), range(2, pow(10, n))))

#ans = 0
#for i in range(2, pow(10, n)):
#	if (i == reduce(lambda x,y: x+y, [pow(int(x), n) for x in str('0'*n+str(i))[-4:]])):
#		ans += i
print 'sum:' + str(ans)
pause = raw_input("pause")
