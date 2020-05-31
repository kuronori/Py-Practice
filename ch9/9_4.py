#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:50:48 2020

@author: TakahiroKurokawa
"""

#デスクリプタとは、__set__,__get__,__delete__のうちいずれか一つ以上持っていれば
#そのオブジェクトはデスクリプタ
print(dir(property()))
#propertyの実体はクラスとして定義されている
print(type(property()))

#通常のメソッドもデスクリプタとして定義されている
class A:
    def f(self):
        pass

print(dir(A.f))

#__set__と__delete__のうちいずれか一つを持っているものをデータデスクリプタ
#__get__しか持たないものを日データデスクリプタ

#デスクリプタのインスタンスをクラス変数として定義すると
#そのクラス変数をインスタンス変数化のように扱える
#属性の取得、代入、削除時にはデスクリプタが実装している__get__、__set__、__delete__
#の対応するメソッドが呼ばれる

class TextField:
    def __set_name__(self,owner,name):
        print(f"__set_name__ was called")
        print(f"owner={owner},name={name}")
        self.name = name
    def __set__(self,instance,value):
        print("__set__ was called")
        if not isinstance(value,str):
            raise AttributeError("must be string")
        #ドット記法ではなく、属性辞書を使って格納
        instance.__dict__[self.name] = value
    def __get__(self,instance,owner):
        print("__get__ was called")
        return instance.__dict__[self.name]

#デスクリプタを利用するクラスは、デスクリプタのインスタンスをクラス変数として利用する
#この時デスクリプタの特殊メソッド__set_name__()には、
#そのデスクリプタを利用するクラスオブジェクトとデスクリプタに割り当てられた変数名が渡されてくる
class Book:
    title = TextField()

#Bookクラスを利用する際には、クラス変数titleをあたかもインスタンス変数であるかのように扱う
book = Book()

#代入時には__set__()が呼ばれる
book.title = "Python Practice Book"
print(book.title)

#別のインスタンスを作成して代入
notebook = Book()
notebook.title = "NoteBook"

#それぞれのデータを保持している
print(book.title)
print(notebook.title)

#__get__のみを実装した非データデスクリプタの優先度はインスタンス変数よりも低い
#そのため、インスタンス変数がある場合にはそちらが利用され、__get__()は呼ばれない
class TextField:
    def __init__(self,value):
        if not isinstance(value,str):
            raise AttributeError("must be str")
        self.value = value
    def __set_name__(self,owner,name):
        print(f"__set_name__ was called")
        print(f"owner={owner},name={name}")
        self.name = name
    def __get__(self,instance,owner):
        print("__get__ was called")
        return self.value

class Book:
    title = TextField("Python Practice Book")

book = Book()
print(book.title)

#代入するとインスタンス変数になる
book.title = "Book"

#インスタンス変数があると__get__()は呼ばれない
print(book.title)

class LazyProperty:
    def __init__(self,func):
        self.func = func
        self.name = func.__name__
    def __get__(self,instance,owner):
        if not instance:
            #クラス変数としてアクセスされた時の処理
            return self
        #self.funcは関数なので明示的にインスタンスを渡す
        v = self.func(instance)
        instance.__dict__[self.name] = v
        return v

TAX_RARE = 1.10
class Book:
    def __init__(self,raw_price):
        self.raw_price = raw_price
    @LazyProperty
    def price(self):
        print("calculate the price")
        return int(self.raw_price * TAX_RARE)

book = Book(1980)
print(book.price)
print(book.price)
    