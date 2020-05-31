#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:39:21 2020

@author: TakahiroKurokawa
"""

a=type(True)
print(a)
print(bool(None))
print(bool([]))
print(bool(['book']))

print(True or False)
print(True or True)
print(False or True)
print(False or False)

x=['book']
y=[]
print(x or y)
print(y or x)
z=0
print(y or z)
print(z or y)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

x=['book']
y=[]

print(x and y)
print(y and x)
z=1

print(x and z)
print(z and x)

print(not True)
print(not False)
print(not [])
print(not ['book'])
print(not [] and ['book'])