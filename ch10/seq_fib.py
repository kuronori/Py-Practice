#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:36:08 2020

@author: TakahiroKurokawa
"""

import os
import time
import sys

def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a + b
    return a

def elapsed_time(f):
    def wrapper(*args,**kwargs):
        st = time.time()
        v = f(*args,**kwargs)
        print(f"{f.__name__}:{time.time()-st}")
        return v
    return wrapper

@elapsed_time
def sequential(nums):
    for num in nums:
        print(fib(num))

def main():
    n = int(sys.argv[1])
    nums = [n] * os.cpu_count()
    sequential(nums)

if __name__ == "__main__":
    main()
    