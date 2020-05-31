#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:31:27 2020

@author: TakahiroKurokawa
"""

items={"note","notebook","sketchbook"}
print(1,items)

print(2,type(items))
print(3,items)

items=set(["note","notebook","sketchbook","note"])
print(4,items)

print(5,set())

items.add("book")
print(6,items)
items.remove("book")
print(7,items)

items.pop()
print(8,items)

items=frozenset(["note","notebook","sketchbook"])
print(9,type(items))
print(10,items)
#items.add("book")

set_a={"note","notebook","sketchbook"}
set_b={"book","rulebook","sketchbook"}

union=set_a | set_b
print(11,union)
print(12,set_a.union(set_b))

intersec=set_a & set_b
print(13,intersec)
print(14,set_a.intersection(set_b))

diff=set_a - set_b
print(15,diff)
print(16,set_a.difference(set_b))

symmetric=set_a ^ set_b
print(17,symmetric)
print(18,set_a.symmetric_difference(set_b))

print(19,{"note","notebook"} <= set_a)
print(20,{"note","notebook"}.issubset(set_a))

items={"note","notebook","sketchbook"}
for item in items:
    print(item)

frozen_items=frozenset(items)
print(21,frozen_items)

for item in frozen_items:
    print(item)

print(22,bool(set()))
print(23,bool(items))
print(24, "note" in items)
print(25,"book" not in items)

print(26,bool(frozenset()))
print(27,bool(frozen_items))
print(28,"note" in frozen_items)
print(29,"book" not in frozen_items)
