#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 15:02:37 2020

@author: TakahiroKurokawa
"""

items={'note':1,'notebook':2,'sketchbook':3}
print(1,type(items))
print(2,items)

items=dict(note=1,notebook=2,sketchbook=3)
print(3,items)

items['book']=4
items.pop('notebook')
print(4,items)

del items['sketchbook']
print(5,items)

items=dict(note=1,notebook=2,sketchbook=3)
print(6,items['note'])
print(7,items.get('book',None))

book=('book',)
item={book:'0'}
print(8,item)

items={'note':1,'notebook':2,'sketcbook':3}
for key in items:
    print(key)

for key,value in items.items():
    print(key,value)

for value in items.values():
    print(value)

print(8,bool({}))
print(9,bool({"book":0}))

print(10,"note" in items)
print(11,"book" not in items)
print(12,1 in items.values())