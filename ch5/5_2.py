#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 18:35:28 2020

@author: TakahiroKurokawa
"""

increment=lambda num:num+1
a=increment(1)
print(a) 

nums=["one","two","three"]
filtered=filter(lambda x:len(x) == 3,nums)
print(list(filtered))