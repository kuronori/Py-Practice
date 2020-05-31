#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:28:49 2020

@author: TakahiroKurokawa
"""

class Page:
    def __init__(self,num,content):
        self.num = num
        self.content = content
    def output(self):
        return(f'{self.content}')
#メソッドのオーバーライド

class TitlePage(Page):
    def output(self):
        #基底クラスのメソッドは自動では呼ばれないため
        #明示的に呼び出す
        title = super().output()
        return title.upper()

title = TitlePage(0,"Python Practice Book")
print(title.output())

#組み込み型のサブクラスを作成
class Length(float):
    def to_cm(self):
        return super().__str__() + "cm"

pencil_length = Length(16)
print(pencil_length.to_cm())

class HTMLPageMixin:
    def to_html(self):
        return f"<html><body>{self.output()}</body></html>"

#多重継承を使ったMixinの利用
class WebPage(Page,HTMLPageMixin):
    pass

page = WebPage(0,"web content")
print(1,page.to_html())

#多重継承の注意点
class A:
    def hello(self):
        print("Hello")
class B(A):
    def hello(self):
        print("Hola")
        super().hello()
class C(A):
    def hello(self):
        print("ニーハオ")
        super().hello()
class D(B,C):
    def hello(self):
        print("こんにちは")
        super().hello()
d=D()
d.hello()

#属性__mro__を利用したメソッド解決順序の確認
print(D.__mro__)

b=B()
b.hello()