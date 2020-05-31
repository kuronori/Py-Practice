#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:54:49 2020

@author: TakahiroKurokawa
"""

class A:
    def __len__(self):
        return 5

a = A()
print(1,len(a))

class B:
    def __len__(self):
        return -1

b = B()
#print(2,len(b))

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x},{self.y})"
    def __str__(self):
        return f"({self.x},{self.y})"

p = Point(1,2)
print(2,p)

class QueryParams:
    def __init__(self,params):
        self.params = params
    def __bool__(self):
        return bool(self.params)
#ユーザー定義のクラス、インスタンスはデフォルトで真
#しかし、__bool__()を実装するとその処理を変更
query = QueryParams({})
print(3,bool(query))

class QueryParams:
    def __init__(self,params):
        self.params = params

query = QueryParams({})
print(4,bool(query))

#__bool__を実装せずに__len__が0を返すと、そのオブジェクトは偽となる
class QueryParams:
    def __init__(self,params):
        self.params = params
    def __len__(self):
        return len(self.params)

print(5,bool(QueryParams({})))


class Adder:
    def __init__(self):
        self._values = []
    def add(self,x):
        self._values.append(x)
    def __call__(self):
        return sum(self._values)


adder = Adder()
adder.add(1)
adder.add(3)
print(6,adder())
adder.add(5)
print(7,adder())

def f():
    return 1
print(8,dir(f))
print(8,type(f))

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #p.x = 1のような属性への代入で呼ばれるメソッド
    #属性の代入を属性名で制限
    def __setattr__(self, name, value):
        if name not in ("x","y"):
            raise AttributeError("Not allowed")
        #self.name = valueと書くと__setattr__が再度呼ばれて無限ループになる
        #このため、__setattr__()の内部で自分自身に属性を追加する場合は、
        #必ず組み込み関数super()を使って基底クラスの__setattr__()を呼び出す
        super().__setattr__(name, value)

p = Point(1,2)
#p.z = 3
p.x = 3
print(9,p.x)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __delattr__(self,name):
        if name not in ("x","y"):
            raise AttributeError("Not allowed")
        super().__delattr__(name)

p = Point(1,2)
del p.x

#属性アクセスメソッド__getattr__()、__getattribute__()の違い
#__getattr__()は属性アクセス時に対象の名前が属性辞書__dict__に存在しない場合にのみ呼ばれる
#__getattribute__()は全ての属性アクセス時に呼び出される

class Point:
    pass

p = Point()
print(10,p.__dict__)
p.x = 1
print(11,p.__dict__)
#__dict__は直接書き込み可能
p.__dict__["y"] = 2
print(12,p.__dict__)

import json
class Config:
    def __init__(self,filename):
        self.config = json.load(open(filename))
    def __getattr__(self,name):
        if name in self.config:
            return self.config[name]
        raise AttributeError()

#conf = Config("config.json")
#print(13,conf.url)

class Iterable:
    def __init__(self,num):
        self.num = num
    def __iter__(self):
        return iter(range(self.num))

lists = [val for val in Iterable(3)]
#__iter__()と__next__()を両方実装したオブジェクトをイテレータと呼ぶ
#イテレータの__iter__()の戻り値は必ず自分自身
#__next__()はループのたびに呼ばれ、その戻り値がfor i in xのiに渡される
#nextにイテレータを渡すとそのイテレータの__next__()が呼ばれ、その戻り値がnext（）の戻り値として受け取れる

class Reverser:
    def __init__(self,x):
        self.x = x
    def __iter__(self):
        return self
    def __next__(self):
        try:
            return self.x.pop()
        except IndexError:
            raise StopIteration()
lists = [val for val in Reverser([1,2,3])]

#インデックス、キーによるアクセスは__getitem__()
#インデックス、キーによる代入は__setitem__()
from collections import defaultdict

class CountDict:
    def __init__(self):
        self._data = {}
        self._get_count = defaultdict(int)
        self._set_count = defaultdict(int)
    def __getitem__(self,key):
        #c["x"]など参照時に呼ばれる
        self._get_count[key] = self._get_count[key] + 1
        return self._data[key]
    def __setitem__(self,key,value):
        #c["x"]=1など代入時に呼ばれる
        self._set_count[key] = self._set_count[key] + 1
        self._data[key] = value
    @property
    def count(self):
        return {
            "set":list(self._set_count.items()),
            "get":list(self._get_count.items())
            }
c = CountDict()
c["x"] = 1
print(13,c["x"])
c["x"] = 2
c["y"] = 3

#参照、代入された回数を返す
print(14,c.count)


#__contains__()は、in演算子で呼び出される
#1 in x を実行すると、オブジェクトxの__contain__()の第２引数に１が渡されて呼び出される
class OddNumbers:
    def __contains__(self,item):
        try:
            return item % 2 == 1
        except:
            raise False

odds = OddNumbers()
print(15,1 in odds)