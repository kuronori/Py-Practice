#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:02:47 2020

@author: TakahiroKurokawa
"""

def print_page():
    print("no content")
    
print_page()

def print_page(content):
    print(content)

print_page("my contents")

def print_page(content="no content"):
    print(content)

print_page()
print_page("my_content")

print(1,type(print_page))
f=print_page
f()
f("my_content")

def print_title(printer,title):
    print("@@@@")
    printer(title.upper())
    print("@@@@")

print_title(print_page,"python practice book")

def increment(page_num):
    return page_num+1

next_page=increment(1)
print(2,next_page)
print(3,increment(increment(next_page)))

def increment(page_num,last):
    next_page=page_num+1
    if next_page<=last:
        return next_page
    raise ValueError("Invalid arguments")

increment(1,3)
#increment(3,3)

def no_value():
    return
print(3,no_value())

def no_return():
    pass
print(4,no_return())

#条件によってreturn文が実行されない場合がある関数
def increment(page_num,last):
    next_num=page_num+1
    if next_num<=last:
        return next_num

next_page=increment(3,3)
print(next_page)

def increment(page_num,last):
    next_page=page_num+1
    if next_page<=last:
        print(next_page)
        return next_page
    raise ValueError('Invalid arguments')
a=increment(2,10)
b=increment(page_num=2,last=10)
c=increment(last=10,page_num=2)
d=increment(2,last=10)
#e=increment(10,page_num=2)

def increment(page_num,last=10):
    next_page=page_num+1
    if next_page<=last:
        print(next_page)
        return next_page
    raise ValueError('Invalid argument')

increment(2)
#increment(2,1)
#def increment(page_num=0,last):
#    pass

def increment(last,page_num=0):
    next_page=page_num+1
    if next_page <= last:
        print(next_page)
        return next_page
    raise ValueError("Invalid argument")

increment(5)

#column

from datetime import datetime

#デフォルト引数の値は関数が定義された時のため、下記関数は狙いの動作をしない
def print_page(content,timestamp=datetime.now()):
    print(content)
    print(timestamp)

print_page("my content")
print_page("my_content2")

#上記関数の修正
def print_page(content,timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
    print(content)
    print(timestamp)

print_page("my content")
print_page("my_content2")

#可変長の位置引数を受け取る関数
def print_page(content,*args):
    print(content)
    for more in args:
        print(more)
    
print_page("my content")
print_page("my content","content2","content3")

#可変長のキーワード引数を受け取る関数
def print_page(content,**kwargs):
    print(content)
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_page("my content",published=2019,author="rei suyama")

def increment(page_num,last,*,ignore_error=False):
    next_page = page_num + 1
    if next_page <= last:
        print(next_page)
        return next_page
    if ignore_error:
        return None
    raise ValueError("Invalid arguments")

increment(2,2,ignore_error=True)
increment(1,2,ignore_error=True)
#increment(2,2,True)

def print_page(one,two,three):
    print(one)
    print(two)
    print(three)

contents=["my content","content2","content3"]
#*による引数リストのアンパック
print_page(*contents)

def print_page(content,published,author):
    print(content)
    print("published:",published)
    print("authhor:",author)

footer={"published":2019,"author":"rei suyama"}
print_page("my content",**footer)

def increment(page_num,last,*,ignore_error=False):
    """次のページ番号を返す
    :param page_num:元のページ番号
    :type page_num:int
    :param last:最後のページ番号
    :type last:int
    :param ignore_error:Trueの場合、ページのオーバーで例外を出さない
    :type ignore_error:bool
    :rtype: int
    """
    next_page = page_num + 1
    if next_page <= last:
        print(next_page)
        return next_page
    if ignore_error:
        return None
    raise ValueError("Invalid argument")

