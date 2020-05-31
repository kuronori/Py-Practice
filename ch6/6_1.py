#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:01:50 2020

@author: TakahiroKurokawa
"""

class Page:
    def __init__(self,num,content):
        self.num = num #ページの番号
        self.content = content #ページの内容
    
    def output(self):
        return f"{self.content}"

print(1,Page)

#インスタンス化
title_page=Page(0,"Python Practice Book")
print(2,type(title_page))

#ページクラスのインスタンスか確認
print(3,isinstance(title_page,Page))
print(4,dir(title_page))
    
    