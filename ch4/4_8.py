#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:50:32 2020

@author: TakahiroKurokawa
"""
numbers=[]
for i in range(10):
    numbers+=[i]
print(1,numbers)
numbers=[num for num in range(10)]
print(2,numbers)
print(3,i)
#print(num)

numbers=[(x,y) for x in range(1,4) for y in range(4,7)]
print(4,numbers)

even_numers=[num for num in range(10) if num % 2 == 0]
print(5,even_numers)

set_comprehension={i for i in range(10)}
print(6,type(set_comprehension))
print(7,set_comprehension)

dict_comprehension={str(num):num for num in range(3)}
print(8,dict_comprehension)

gen=(i for i in range(3))
print(9,type(gen))
print(10,gen)