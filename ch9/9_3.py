#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 15:36:30 2020

@author: TakahiroKurokawa
"""

#with文に対応したしたオブジェクトをコンテキストマネージャーという
with open("some.txt","w") as f:
    f.write("python")
    
print(f.closed)

#with open("some.txt","w") as f:
    #f.read() #書き込みモードなので例外になる
#f.closedは例外でもTrue
#with文はtry：finally：の書き換え
#try:
    #f = open("some.txt","w")
    #f.read()
#finally:
    #f.close()

#このクラスのインスタンスがコンテキストマネージャー
class ContextManager:
    #前処理を実装
    def __enter__(self):
        print("__enter__ was called")
    #後処理を実装
    def __exit__(self,exc_type,exc_value,traceback):
        print("__exit__ was called")
        print(f"exc_type = {exc_type}")
        print(f"exc_value = {exc_value}")
        print(f"traceback = {traceback}")

with ContextManager():
    print("inside the block")

#もしwithブロック内から例外が送出された場合は、特殊メソッド__exit__()の引数でその情報を受け取る
#with ContextManager():
    #1/0

class ContextManager:
    #戻り値がasキーワードに渡される
    def __enter__(self):
        return 1
    def __exit__(self,exc_type,exc_value,traceback):
        pass

with ContextManager() as f:
    print(f)
#asキーワードの省略
with ContextManager():
    pass

#withブロック内から任意の値を特殊メソッド__exit__()に直接渡す方法はありません。
#その場合、インスタンス変数などを介する必要がある
class Point:
    def __init__(self,**kwargs):
        self.value = kwargs
    def __enter__(self):
        print("__enter__ was called")
        return self.value #as節で渡される
    def __exit__(self,exc_type,exc_value,traceback):
        print("__exit__ was called")
        print(self.value)

with Point(x=1,y=2) as p:
    print(p)
    p["z"] = 3
#標準ライブラリデコレータのcontextlib.contextmanagerは
#@contextmanagerをつけたジェネレータ関数を記述すると、コンテキストマネージャーを作成可
from contextlib import contextmanager
@contextmanager
def point(**kwargs):
    print("__enter__ was called")
    value = kwargs
    try:
        #yield式より上が前処理
        #valueがasキーワードに渡される
        yield value
        #yield式より下が後処理
    except Exception as e:
        #エラー時はこちらも呼ばれる
        print(e)
        raise
    finally:
        print("__exit__ was called")
        print(value)

with point(x=1,y=2) as p:
    print(p)
    p["z"] = 3



    
    
        

        