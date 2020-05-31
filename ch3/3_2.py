#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:59:18 2020

@author: TakahiroKurokawa
"""

import sys


def py2_or_py3():
    major=sys.version_info.major
    if major==2:
        return "Python2"
    elif major==3:
        return "Python3"
    else:
        return "Neither"
print(py2_or_py3())

#複雑な条件式
def first_item(item):
    if len(item)>0:
        return item[0]
    else:
        return None
print(first_item(["book"]))

#シンプルな条件式
def first_item2(item):
    if item:
        return item[0]
    else:
        return None

print(first_item2([]))

x="book"
y="note"

print(x==y)
print(x!=y)
print(x is None)
print(x is not None)

items=["book","note"]
print("book" in items)
print("book" not in items)

count={"book":1,
       "note":2}
print(1 in count)    
