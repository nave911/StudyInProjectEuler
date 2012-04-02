# -*- coding: utf-8 -*-
import sys, math

n = 1001
sum = reduce(lambda x, y: x+((y-2)*(y-2) + 1) + (y*y - 1) + y*y + (y*y - 2*(y-1)), range(3, n+1, 2), 1)
print str(n) + ' : ' + str(sum)
pause = raw_input("pause")
