#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:45:53 2020

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

from concurrent.futures import (
    ProcessPoolExecutor,
    as_completed
    )

@elapsed_time
def mul_pro(nums):
    with ProcessPoolExecutor() as p:
        futures = [p.submit(fib,num) for num in nums]
    for future in as_completed(futures):
        print(future.result())

def main():
    n = int(sys.argv[1])
    nums = [n] * os.cpu_count()
    mul_pro(nums)

if __name__ == "__main__":
    main()


