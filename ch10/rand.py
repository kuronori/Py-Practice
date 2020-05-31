#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:16:51 2020

@author: TakahiroKurokawa
"""

from concurrent.futures import (
    ProcessPoolExecutor,
    as_completed
    )

import numpy as np

def use_numpy_random():
    #乱数生成器を初期化する場合はこの行を実行
    np.random.seed()
    return np.random.random()

def main():
    with ProcessPoolExecutor() as e:
        futures = [e.submit(use_numpy_random)
                   for _ in range(3)]
        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()

