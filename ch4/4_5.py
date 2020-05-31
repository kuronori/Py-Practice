#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:38:54 2020

@author: TakahiroKurokawa
"""

items=['note','notebook','sketchbook']
print(1,type(items))
print(2,items)
print(3,list('book'))

items.append('paperbook')
print(4,items)

items=['book']+items
print(5,items)
print(6,items.pop(0))
print(7,items)
del items[1]
print(8,items)

items=['note','notebook','sketchbook']
print(9,items[1])
print(10,items[-2])
items[1]='book'
print(11,items)

items=['note','notebook','sketchbook']
print(12,items[0:2])
print(13,items)
print(14,items[:2])
print(15,items[1:])
print(16,items[0:-1])

#要素数は一致していなくてもよい
items[2:]=[1,2,3]
print(17,items)

items=('note','notebook','sketchbook')
print(17,type(items))
print(18,items)

items='note','notebook','sketchbook'
print(19,items)

items=['note','nottebook']
print(20,tuple(items))

empty_tup=()
print(21,empty_tup)
print(22,())

one_tup=(1,)
print(23,one_tup)

items=('note','notebook','sketchbook')
print(24,items[0:2])
print(25,items[:2])
print(26,items[1:])

for item in ['note','notetbook','sketchbook']:
    print(item)
    
for item in ('note','notebook','sketchbook'):
    print(item)

print(27,bool([]))
print(28,bool(['book']))
print(29,'note' in ['note','notebook','sketchbook'])
print(30,'book' not in ['note','notebook','sketchbook'])

empty=tuple()
print(31,bool(empty))
print(32,bool(('book',)))
print(33, 'note' in ('note','notebook','sketchbook'))
print(34,'book' not in ('note','notebook','sketchbook'))
