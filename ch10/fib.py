#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:30:01 2020

@author: TakahiroKurokawa
"""
import sys
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a + b
    return a

def main():
    n = int(sys.argv[1])
    print(fib(n))

if __name__ == "__main__":
    main()
