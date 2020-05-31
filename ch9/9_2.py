#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 20:21:24 2020

@author: TakahiroKurokawa
"""
#デコレータの実例
#functools.lru_cache関数の出力結果をキャッシュし、同じ引数の呼び出しを再計算しない
#dataclasses.dataclass()よくある特殊メソッドをクラスに自動追加するクラスデコレータ
from functools import lru_cache
from time import sleep

#最近の呼び出し最大32回までキャッシュ
@lru_cache(maxsize = 32)
def heavy_function(n):
    sleep(3) #重い処理をシミュレート
    return n + 1

#初回は時間がかかる
print(heavy_function(2))

#キャッシュにヒットするので、すぐに結果を得られる
print(heavy_function(2))

from dataclasses import dataclass
#引数frozenにTrueを渡すと、特殊メソッド__init__に加え、__setattr__を追加
#読み取り専用のクラスを定義可能
@dataclass(frozen = True)
class Fruit:
    name: str #型ヒントをつけて属性を定義
    price: int = 0 #初期値も指定
#__init__()や__repr__()が自動で追加されている
apple = Fruit(name="apple",price = 120)
print(apple)
#forzen=Trueとしたので読み取り専用
#apple.price = 256

#デコレートしたい関数を受け取る
#デコレート対象関数の呼び出し前後でログ出力
def deco1(f):
    def wrapper():
        print("before exec")
        v = f()
        print("after exec")
        return v
    return wrapper

@deco1
def func():
    print("exec")
    return 1
print(func.__name__)
a = func()

#deco1内でv = f()が引数のない関数を想定するため、下記はエラー
@deco1
def func(x,y):
    print("exec")
    return x,y

#a = func(1,2)

#deco1を引数を受け取る関数にも対応可能に改良
#デコレートした関数を実行すると、プログラム実行中に実際に呼び出される関数はwrapper()のため
#wrapper()関数が任意の引数を受け取り、元の関数を呼び出す際に受け取った引数をそのまま渡す
def deco2(f):
    def wrapper(*args,**kwargs):
        print("before exec")
        print("posi_args:",args)
        print("kw_args:",kwargs)
        v = f(*args,**kwargs)
        print("after exec")
        return v
    return wrapper

@deco2
def func(x,y):
    print("exec")
    return x,y
result = func(1,2)

#デコレータ自身が引数を受け取るデコレータ
#デコレータを返す関数を作成すると、あたかもデコレータ自身が引数を
#受け取っているかのような処理を実現可能
#引数zを受け取る
def deco3(z):
    def _deco3(f):
        def wrapper(*args,**kwargs):
            #ここでzを参照できる
            print("before exec",z)
            v = f(*args,**kwargs)
            print("after exec",z)
            return v
        return wrapper
    return _deco3 #デコレータを返す
#deco3(z=3)の戻り値がデコレータの実態
#つまりfunc = deco3(z=3)(func)
@deco3(z = 3)
def func(x,y):
    print("exec")
    return x,y
#zに渡した値は保持されている
result = func(1,2)

#複数のデコレータを同時に利用する
#一つの関数定義に複数のデコレータを利用できる
#内側のデコレータから適用される
@deco3(z=3)
@deco3(z=4)
def func(x,y):
    print("exec")
    return x,y

#deco3(z=4)が適用された結果に
#deco3(z=3)が適用される
result = func(1,2)

#functools.wraps()でデコレータの問題点
#関数名がデコレータの内部関数wrapperになる問題点を解消可能
#デコレータを使うときは、通常functools.wraps()を使う
#バグ要因が特定できるから
from functools import wraps
def deco4(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        print("before exec")
        v = f(*args,**kwargs)
        print("after exec")
        return v
    return wrapper

@deco4
def func():
    """
    func()です
    """
    print("exec")

print(func.__name__)
print(func.__doc__)

#関数の処理時間を計測するデコレータ
import time
def elapsed_time(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        start = time.time()
        v = f(*args,**kwargs)
        print(f"{f.__name__}:{time.time()-start}")
        return v
    return wrapper
#0からn-1までの総和を計算する関数
@elapsed_time
def func(n):
    return sum(i for i in range(n))

a = func(10000000)