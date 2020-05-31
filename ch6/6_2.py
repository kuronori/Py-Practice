#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:07:49 2020

@author: TakahiroKurokawa
"""

class Page:
    def __init__(self,num,content):
        self.num = num #ページの番号
        self.content = content #ページの内容
    
    def output(self):
        return f"{self.content}"

title_page=Page(0,"Python Practice Book")
a=title_page.output()
print(1,a)

#column
class Klass:
    def some_method(self):
        print("method")

def some_function(self):
    return "function"
    

print(2,type(Klass.some_method))
print(3,type(some_function))
#インスタンスを通じてアクセスするとmethodクラスになる
kls=Klass()
print(4,type(kls.some_method))

#クラスオブジェクトの属性に関数を追加
Klass.some_function=some_function
#インスタンスメソッドとして実行
print(5,kls.some_function())

title_page.section=0
print(6,title_page.section)

first_page=Page(1,"first page")
#print(7,first_page.section)

class Page:
    def __init__(self,num,content,section=None):
        self.num = num
        self.content = content
        self.section = section
    def output(self):
        return f"{self.content}"

title_page = Page(0,"Pthon Practice Book")
print(7,title_page.section)
print(8,title_page.output())

first_page = Page(1,"first page",1)
print(9,first_page.section)
print(10,first_page.output())

class Book:
    def __init__(self,raw_price):
        if raw_price < 0:
            raise ValueError("price must be positive")
        self.raw_price = raw_price
        self._discounts = 0
    @property
    def discounts(self):
        return self._discounts
    @discounts.setter
    def discounts(self,value):
        if value < 0 or 100 < value:
            raise ValueError("discounts must be between 0 and 100")
        self._discounts = value
    @property
    def price(self):
        multi = 100 - self._discounts
        return int(self.raw_price * multi / 100)

book=Book(2000)
#初期は値引率0
print(11,book.discounts)
#初期価格は2000
print(12,book.price)
#値引率を設定
book.discounts = 10
#値引き後の価格を出力する
print(13,book.price)
#100を超える値を入れるとエラー
#book.discounts = 120

#_から始まる属性はプライベートな属性であることの表明
#しかし、アクセス可能
print(14,book._discounts)

#__から始まる属性は属性名をクラス名で修飾できる
#サブクラスでの名前衝突を避けるため
class Klass:
    def __init__(self,x):
        self.__x = x

kls = Klass(10)
#print(15,kls.x)
#kls._Klass.__xならアクセスできる
print(15,kls._Klass__x)

