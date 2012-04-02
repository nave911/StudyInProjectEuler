# -*- coding: utf-8 -*-
import sys, math

n = 1000

print reduce(lambda x, y: x+int(y), str(pow(2, n)), 0)
pause =raw_input("pause")
