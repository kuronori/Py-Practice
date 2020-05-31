#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:28:45 2020

@author: TakahiroKurokawa
"""

print(None)
print(str(None))

#インタプリタと違い、bookの後にNoneが出力されない
str(print('book'))

if None:
    print('Noneは真')
else:
    print('Noneは偽')

n=None
if n is None:#Noneとの比較はisを使う
    print('変数nの値はNoneです')
else:
    print('変数nの値はNoneではありません')


