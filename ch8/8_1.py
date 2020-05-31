#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 09:38:14 2020

@author: TakahiroKurokawa
"""

d = {}
#第１引数はインスタンスオブジェクト
print(1,isinstance(d,dict))
print(2,isinstance(d,object))
print(3,isinstance(d,(list,int,dict)))

#第１引数はクラスオベジェクト
print(4,issubclass(dict,object))
print(5,issubclass(bool,(list,int,dict)))

#辞書から値を取り出す関数
def get_value(obj,key):
    if not isinstance(obj,dict):
        raise ValueError
    return obj[key]

#辞書風オブジェクトの作成
from collections import UserDict
class Mydict(UserDict):
    pass

#辞書のように使える
my_dict = Mydict()
my_dict["a"] = 1
print(6,my_dict["a"])

#dictのインスタンスではないためエラー
#get_value(my_dict, a)

from collections import abc

#Mydictクラスの基底クラスUserdictは
#辞書として振る舞う際に必要となるメソッドを全て実装している
#辞書の抽象基底クラスcollections.abc.Mappingを利用すると解決する
#抽象基底クラスとはインターフェースを宣言するために用意されたクラス
#辞書の抽象基底クラスであるMappingクラスには、辞書として振る舞う際に必要となるメソッド群が定義されている
#isinstanceの判定で、抽象基底クラスを利用すると必要なメソッド群が定義されているかで判定する
def get_value(obj,key):
    if not isinstance(obj,abc.Mapping):
        raise ValueError
    return obj[key]

get_value(my_dict,"a")

#()をつけて呼び出せるオブジェクトを呼び出し可能オブジェクト
print(7,callable(isinstance))
print(8,callable(Exception))
print(9,callable("".split))

class Threshold:
    def __init__(self,threshold):
        self.threshold = threshold
    def __call__(self,x):
        return self.threshold < x

#インスタンス化時に閾値を設定
threshold = Threshold(2)

#__call__を実装すると、インスタンスに()をつけると__call__を呼び出せる
print(10,threshold(3))
print(11,threshold(1))
print(12,callable(threshold))

import json
import os

#パッケージオブジェクトは必ず__path__を持つ
def is_package(module_or_package):
    return hasattr(module_or_package,"__path__")

#jsonはモジュールはパッケージ
#osモジュールは単体ファイル
print(13,is_package(json))
print(14,is_package(os))

class Mutable:
    def __init__(self,attr_map):
        #辞書のキーを属性名にしたインスタンス変数を用意
        for k,v in attr_map.items():
            setattr(self, str(k), v)
m = Mutable({"a":1,"b":2})
print(15,m.a)
print(16,getattr(m,"b"))

delattr(m,"a")

#getattrはインスタンス変数だけでなく、メソッドも取得できる
#getattrでメソッドを取得した時、元のインスタンスの情報を保持したメソッドが返る
text = "python"
instance_method = getattr(text,"upper")
print(16,instance_method)
#text.upper()と同等
print(17,instance_method())

x = [1,2,3]
y = [4,5,6]
zipped = zip(x,y)
zipped = list(zipped)
print(18,zipped)

x = [1,2,3]
y = [4,5,6,7]
z = [8,9]

#一番短いイテラブルの長さになる
zipped2 = list(zip(x,y,z))
from itertools import zip_longest
#fillvalueは足りない値を埋める時に使われる
zipped3 = list(zip_longest(x,y,z,fillvalue=0))

x = [1,4,3,5,2]
y = [1,4,3,5,2]

#list.sortはオベジェクト自身を並び替える
x.sort()
#sortedは新しいオブジェクトを返す
z = sorted(y)
#reverse = Trueを指定すると逆順になる
z = sorted(y,reverse = True)

#sortedの引数keyに、引数を一つだけ取る関数を指定する
#sortが行われる際、この関数に各要素が渡される
#比較結果が等しい場合、元の順序が保持される
x = ["1","4",3,1,"1"]
#各要素をint型の値として比較
x = sorted(x,key = lambda v: int(v))

x = (1,4,3,5,2)
print(19,filter(lambda v: v>3,x))
filterd = list(filter(lambda v : v>3, x))
#filterの第１引数の関数をNoneにすると各要素の真理値を判定し、Trueの要素のみ返る
x = (1,0,None,2,[],"python")
filterd = list(filter(None,x))

x = (1,4,3,5,2)
print(20,map(lambda i: i*10,x))
mapped = list(map(lambda i: i*10,x))

keys = ("q","limit","page")
values = ("python",10,2)

#関数が受け取る引数の数と渡すイテラブルの数は一致させる
mapped2 = list(map(lambda k,v: f"{k}={v}" ,keys,values))
#joinと組み合わせてクエリ文字列を作成
query = "?"+"&".join(list(map(lambda k,v:f"{k}={v}",keys,values)))


#all()は全ての要素が真の場合にTrueを返す
print(21,all(["python","practice","book"]))
#空文字が偽なので、結果もFalse
print(22,all(["python","practice",""]))

#any()は一つでも真であればTrue
print(23,any(["python","",""]))
#真の値がないのでFalse
print(24,["","",""])