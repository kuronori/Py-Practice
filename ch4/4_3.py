#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:24:10 2020

@author: TakahiroKurokawa
"""

print(1,1+2)
print(2,1-2.0)
print(3,1.0*2j)
print(4,1/2)
#print(1/0)

print(5,11%5)
print(6,11//5)
print(7,11**5)

import math
print(8,math.log(5))

a=1
print(9,a)

print(10,1_000_000)
a=int(1)
print(11,float(a))
print(12,complex(a))

print(13,type(3))
print(14,3+4)
print(15,3/2)
print(16,int(3/-2))
print(17,type(3.0))
print(18,type(1e-5))
print(19,3.0+4.0)
print(20,3.0+4)

infinity=float("inf")
print(21,infinity)
print(22,type(infinity))
print(23,infinity+1)
print(24,float('-inf'))
nan=float('nan')
print(25,nan)
print(26,nan+1)

import sys
print(27,sys.float_info)

a=1.2+3j
print(28,a)
print(29,type(a))
print(30,a.real)
print(31,a.imag)

print(32,a+2j)
print(33,a+2)
print(34,a+3.4)

print(35,bool(0.0))
print(36,bool(1))
print(37,bool(-1))
print(38,bool(float('-inf')))

#float型を扱う時、０.３は正確に表現できない
print(39,0.1+0.1+0.1==0.3)
print(40,round(0.1+0.1+0.1)==round(0.3))