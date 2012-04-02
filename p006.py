# -*- coding: utf-8 -*-
import math

n = 100

indep = reduce(lambda x,y: x+(y*y), range(1, n+1), 0)
depen = pow(reduce(lambda x,y: x+y, range(1, n+1)), 2)

print "n = %d : %d" % (n, depen - indep)
pause =raw_input("pause")
