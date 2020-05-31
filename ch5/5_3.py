#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 18:35:57 2020

@author: TakahiroKurokawa
"""

from typing import Optional
def increment(
        page_num:int,
        last:int,
        *,
        ignore_error:bool = False) ->Optional[int]:
    next_page = page_num + 1
    if next_page <= last:
        print(next_page)
        return next_page
    if ignore_error:
        return None
    raise ValueError("Invalid arguments")

print(increment.__annotations__)

def decrement(page_num:int) -> int:
    prev_page:int
    prev_page= page_num - 1
    return prev_page

a=decrement(2)
print(a)