#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:09:27 2020

@author: TakahiroKurokawa
"""

def get_book(index):
    items=["note","notebook","sketchbook"]
    try:
        return items[index]
    except IndexError:
        return "範囲外です"
print(get_book(0))
print(get_book(100))

def get_book2(index):
    items=["note","notebook","sketchbook"]
    try:
        return items[index]
    except (IndexError,TypeError) as e:
        print(f'例外が発生しました
：{e}')
        return '範囲外です'
print(get_book2(1))
print(get_book2(4))
print(get_book2("string"))

#tryの処理内容に問題あり
#itemはstr型のためupperメソッドは必ず成功する。そのため、try節に含める必要はない。
def get_book_upper(index):
    items=["note","notebook","sketchbook"]
    try:
        item=str(items[index])
        return item.upper()
    except (IndexError,TypeError) as e:
        print(f"例外が発生しました
：{e}")
get_book_upper(100)


def get_book_upper2(index):
    items=["note","notebook","sketchbook"]
    try:
        item=str(items[index])
    except (IndexError,TypeError) as e:
        print(f"例外が発生しました：{e}")
    else:
        return item.upper()
get_book_upper(100)

from io import UnsupportedOperation
f=open('some.txt','w')
try:
    #書き込みモードなので読み込めない
    f.read()
except UnsupportedOperation as e:
    print(f"例外が発生しました:{e}")
finally:
    print("ファイルをクローズします")
    f.close()

f=open('some.txt','r')

try:
    f.read()
finally:
    print('ファイルをクローズします')
    f.close()

#errorをexcept節で補足しないコードのため、実行するとここで止まる。これ以降に記述するため文字列
error_code="""f=open('some.txt','w')
try:
    f.read()
finally:
    print('ファイルをクローズします')
    f.close()
"""

error_code2="raise ValueError('不正な引数です')"
#例外をそのまま出力する
def get_book3(index):
    items=['note','notebook','sketchbook']
    try:
        return items[index]
    except IndexError as e:
        print('例外が発生しました')
        raise
error_code3='get_book3(100)'


class PracticeBookError(Exception):
    """モジュール独自の例外の基底クラス"""

class PageNotFoundError(PracticeBookError):
    """"ページが見つからない時の例外"""
    def __init__(self,message):
        self.message=message

class InvalidPageNumberError(PracticeBookError):
    """"不正なページ番号が指定された時の例外"""
    def __init__(self,message):
        self.message=message

with open('some.txt','w') as f:
    f.write('some text')
print(f.closed)