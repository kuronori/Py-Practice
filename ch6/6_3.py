#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:56:38 2020

@author: TakahiroKurokawa
"""

class Page:
    book_title = "Python Practice Book"

print(1,Page.book_title)
#クラス変数の更新
Page.book_title = "No title"
print(2,Page.book_title)

#クラス変数にはインスタンスからもアクセス可能
first_page = Page()
second_page = Page()
print(3,first_page.book_title)
print(4,second_page.book_title)

#クラス変数は全てのインスタンスで共有される
Page.book_title = "Python Practice Book"
#クラス変数更新は必ずクラスオブジェクトから行う
#インスタンスからクラス変数更新すると、そのインスタンスの新しいインスタンス変数が定義される
#これはインスタンス変数になる
first_page.book_title = "[Draft]Python Practice Book"
print(5,first_page.book_title)
#クラス変数は変わっていない
print(6,Page.book_title)


#クラス変数と同名のインスタンス変数が定義された場合、そのインスタンスの属性からクラス変数にはアクセスできない
print(7,first_page.book_title)
del first_page.book_title
print(8,first_page.book_title)

#属性を使ったソートに使える標準ライブラリをインポート
from operator import attrgetter
class Page:
    book_title = "Python Practice Book"
    def __init__(self,num,content):
        self.num = num
        self.content = content
    def output(self):
        return f"{self.content}"
    #クラスメソッドの第１引数はクラスオブジェクト
    @classmethod
    def print_pages(cls,*pages):
        #クラスオブジェクトの利用
        print(cls.book_title)
        pages = list(pages)
        #ページ順に並べて出力
        for page in sorted(pages,key = attrgetter("num")):
            print(page.output())

first = Page(1,"first page")
second = Page(2,"second page")
third = Page(3,"third page")

#クラスメソッドの呼び出し
Page.print_pages(first,second,third)
#インスタンスからも呼び出せる
first.print_pages(first,second,third)

