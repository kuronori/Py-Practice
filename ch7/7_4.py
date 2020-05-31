#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:48:49 2020

@author: TakahiroKurokawa
"""

def f():
    value = 'f_function'
    print(value)

def g():
    value = "g_function"
    print(value)

f()
g()
#print(value)

lists = [value for value in range(1)]
#print(value)

def f(x):
    #現在のローカルスコープの内容を表示
    print(locals())
    value = "book"
    #変数valueの定義後ローカルスコープの内容を表示
    print(locals())

f("python")

#モジュールのトップレベルでは、グローバルスコープと一致
print(locals())

x = "python"
print(x)

#グローバル変数を参照
def f():
    print(x)

f()

#グローバル変数の更新ではなくローカル変数の作成
def g():
    x = "g_function"
    print(x)

g()
#グローバル変数はそのまま
print(x)

#関数内でグローバル変数を参照した後で、その関数内でグローバル変数と同名のローカル変数を定義できない
x = "python"
def f():
    #グローバル変数への参照
    print(x)
    #グローバル変数と同名のローカル変数
    x = "f_function"
    print(x)

#f()

x = "python"
def f():
    global x
    #グローバル変数であることを宣言
    x = "book"
    print(x)

f()
#グローバル変数の値が更新されている
print(x)

#グローバル変数がコンテナオブジェクトなら、global文は不要
x = [0,1]
def f():
    x[0] = 2

print(x)
f()
print(x)

print(globals())

print(dir(__builtins__))

def f():
    x = "x"
    def g():
        #エンクロージングスコープ内の変数xを参照
        print(x)
    g()

f()

def f():
    x = "x"
    def g():
        nonlocal x #xがローカル変数ではないことを宣言
        x = 1
        print(x)
    g()
    print(x)

f()

#nonlocal文がない場合、新しいローカル変数として定義される
def f():
    x = "x"
    def g():
        x = 1
        print(x)
    g()
    print(x)
f()

        
        