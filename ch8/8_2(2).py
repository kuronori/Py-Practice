#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:31:17 2020

@author: TakahiroKurokawa
"""

class A:
    def __len__(self):
        return 5

a = A()
print(len(a))

class B:
    def __len__(self):
        return -1

b = B()
#print(len(b))


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Point({self.x},{self.y})"
    def __str__(self):
        return f"({self.x},{self.y})"
p = Point(1,2)
print(p)

class QueryParams:
    def __init__(self,params):
        self.params = params
    def __bool__(self):
        return bool(self.params)

query = QueryParams({})
print(bool(query))

class QueryParams:
    def __init__(self,params):
        self.params = params
    def __len__(self):
        return len(self.params)

print(bool(QueryParams({})))

class Adder:
    def __init__(self):
        self._values = []
    def add(self,x):
        self._values.append(x)
    def __call__(self):
        return sum(self._values)

adder = Adder()
adder.add(1)
adder.add(2)
print(adder())
adder.add(5)
print(adder())

def f():
    return 1
print(dir(f))
print(type(f))

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #属性名で属性入力を制限する
    def __setattr__(self,name,value):
        if name not in ("x","y"):
            raise AttributeError("Not Allowed")
        super().__setattr__(name, value)
p = Point(1,2)
#p.z = 3
p.x = 4
#p.z = 2
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def delattr(self,name):
        if name not in ("x","y"):
            return AttributeError("Not Allowed")
        super().__delattr__(name)
    
p = Point(1,2)
del p.x

#__getattr__と__getattribute__の違い
class Point:
    pass

p = Point()
print(p.__dict__)
p.x = 1
print(p.__dict__)
p.__dict__["y"] = 2
print(p.y)

dummy_dict = {"a":1}
class Config:
    def __init__(self,dic):
        self.dic = dic
    def __getattr__(self,key):
        if key in self.dic:
            return self.dic[key]
        raise AttributeError()
conf = Config(dummy_dict)
print(conf.a)   

#イテラブルは__iter__のみ       
class Iterable:
    def __init__(self,num):
        self.num = num
    def __iter__(self):
        return iter(range(self.num))
print(dir(Iterable))

f = [val for val in Iterable(3)]

#__iter__はfor i in xと書いた時、for文はxの__iter__を呼び出す
#__iter__の戻り値は、イテレータと呼ばれる
#イテレータは__iter__と__next__をもつ
#nextはループのたびに呼ばれ、__next__の戻り値がfor i in xのiに格納される
#イテレータの__iter__の戻り値は、イテレータ自身self
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

f = [val for val in Reverser([1,2,3])]

#__getitem__は、インデックスやキーによるアクセスx[1]、x[key]で呼び出される
#__setitem__は、インデックスやキーによる代入x[key] = 1で呼び出される
#キーごとに参照された回数と代入された回数を数える
from collections import defaultdict
class Counter:
    def __init__(self):
        self._data = {}
        self.set_count = defaultdict(int)
        self.get_count = defaultdict(int)
    def __getitem__(self,key):
        self.get_count[key] += 1
        return self._data[key]
    def __setitem__(self,key,value):
        self.set_count[key] += 1
        self._data[key] = value
    @property
    def count(self):
        return {
            "set":list(self.set_count.items()),
            "get":list(self.get_count.items())}

counter = Counter()
counter["a"] = 1
counter["a"] = 2
counter["b"] = 3
print(counter["a"])
print(counter["b"])
print(counter.count)

#1 in xを実行すると、1が__contains__の第２引数に渡されて呼び出される
class OddNumbers:
    def __contains__(self,item):
        try:
            return item %2 == 1
        except:
            return False
    
odds = OddNumbers()
print(1 in odds)
print(2 in odds)

#__contains__を実装していないクラスでも、in演算子を利用できる場合がある
r = Reverser([1,2,3])
print(2 in r)
print(4 in r)
#__contains__が実装されていないクラスでは、__iter__を使って得た各要素に一致するものがないか確認する
      
        
        
    
        

            