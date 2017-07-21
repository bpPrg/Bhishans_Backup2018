#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jun 20, 2017 Tue
# Last update : 
#
# Imports
import pandas as pd
from pandas import DataFrame as DF


a = '0    1    2    3    4    5    6    7    8    9    10    11    12    13    14    15    16    17    18    19    20'.split()
b = '0.0 0.333 0.666 0.999 1.332 1.665 1.998 2.331 2.664 2.997 3.33 3.663 3.996 4.329 4.662 4.995 5.328 5.661 5.994 6.327'.split()

print(a)
print(b)

df = DF(a,columns=['a'])
df['b']= b
print(df )
