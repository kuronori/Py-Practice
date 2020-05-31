#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:09:39 2020

@author: TakahiroKurokawa
"""

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
    )

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
def get_multi_thread(nums):
    with ThreadPoolExecutor() as e:
        futures = [e.submit(fibonacci,num)
                   for num in nums]
        for future in as_completed(futures):
            print(future.result())

def main():
    n = int(sys.argv[1])
    nums = [n] * os.cpu_count()
    get_multi_thread(nums)

if __name__ =="__main__":
    main()