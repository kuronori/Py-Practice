#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:13:25 2020

@author: TakahiroKurokawa
"""

from concurrent.futures import (
    ProcessPoolExecutor,
    wait
    )

func = lambda: 1
def main():
    with ProcessPoolExecutor() as e:
        future = e.submit(func)
        done,not_done = wait([future])
    print(future.result())

if __name__ =="__main__":
    main()