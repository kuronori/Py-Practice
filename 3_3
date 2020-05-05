#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 18:12:42 2020

@author: TakahiroKurokawa
"""

items=[1,2,3]
for i in items:
    print(f"変数iの値は{i}")

for i in range(3):
    print(f"{i}番目の処理")
chars="word"

for i,char in enumerate(chars):
    print(f"{i}番目の文字は{char}")

#奇数がなければメッセージを表示する
#for文のelse節はbreakが実行されなければ、実行される
#ここは入門Python3の方が分かりやすい
#自分のミスはbreakを使わずにelse節を使おうとしたこと
#for num in nums:
#    if num % 2 == 0:
#           pass
def odd_in(nums):
    for num in nums:
        if num % 2 == 1:
            break
    else:
        print("奇数はありません")
nums=[2,4,6,8]
odd_in(nums)
nums=[2,4,6,7,8]
odd_in(nums)

n=0
while n<3:
    print(f"変数nの値は{n}")
    n+=1

while n<3:
    print(f'変数nの値は{n}')
    n+=1
else:
    print("終了")
    
def has_book(items):
    return "book" in items
def has_book2(items):
    for item in items:
        if item == "book":
            print("Found")
            break
    else:
        print("Not found")
has_book2(["a book","books"])

def has_book3(items):
    copied=items.copy()
    while copied:
        item=copied.pop()
        if "book" in item:
            print("Found")
            break
    else:
        print("Not found")
has_book3(["note"])
has_book3(["notebook"])

def list_books(items):
    for item in items:
        if "book" not in item:
            continue
        print(f"bookは{item}に含まれる")

list_books(["note","notebooks"])

def list_books2(items):
    copied=items.copy()
    while copied:
        item=copied.pop()
        if "book" not in item:
            continue
        print(f"bookは{item}に含まれる")

list_books(["note","notebooks"])

