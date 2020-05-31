#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:48:50 2020

@author: TakahiroKurokawa
"""

import os
import time
import sys

#elapsed_timeは先ほどと同じ
def elapsed_time(f):
    def wrapper(*args,**kwargs):
        st = time.time()
        v = f(*args,**kwargs)
        print(f"{f.__name__}:{time.time()-st}")
        return v
    return wrapper

def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a + b
    return a

@elapsed_time
def get_sequential(nums):
    for num in nums:
        print(fibonacci(num))
        
def main():
    n = int(sys.argv[1])
    #返される値が環境により異なる
    nums = [n] * os.cpu_count()
    get_sequential(nums)

if __name__ =="__main__":
    main()