#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:17:54 2020

@author: TakahiroKurokawa
"""

#yield式を含む関数はジェネレータ
#ジェネレータは値を要求されるまで、値を持たないため、メモリ使用量を抑えられる
def inf(n):
    while True:
        yield n
#戻り値はジェネレータイテレータ
#__next__()が呼ばれるたび、yield文までが実行され、一時中断
def gen_function(n):
    print("start")
    while n:
        print(f"yield:{n}")
        yield n #ここで一時中断される
        n -= 1

gen = gen_function(2)
print(gen)

#組み込み関数next()が呼ばれると
#__next__()が呼ばれる
result = next(gen)
result2 = next(gen)
#result3 = next(gen)


#ジェネレータ関数は戻り値がイテレータのため、for文や内包表記、引数にイテラブルをとる関数などで利用可
#for文での利用
for i in gen_function(2):
    print(i)

#内包表記での利用
lists = [i for i in gen_function(5)]

#イテラブルを受け取る関数を渡す
result3 = max(gen_function(5))

x =[1,2,3,4,5]
#これはリスト内包表記
listcomp = [i**2 for i in x]
print(listcomp)

#これはジェネレータ式
gen = (i**2 for i in x)
print(gen) #各要素が必要になるまで計算されない
#リストにすると最後の要素まで計算される
result4 = list(gen)

#関数の呼び出し時に渡したい引数がジェネレータ式1つだけの場合は、
#内包表記の()を省略できる
result5 = max(i**3 for i in x)

def chain(iterables):
    for iterable in iterables:
        for v in iterable:
            yield v
iterables = ["python","book"]
result6 = list(chain(iterables))

#chain関数の最後の２行はyield from式で書き換え可能
def chain(iterables):
    for iterable in iterables:
        yield from (v for v in iterable)

result7 = list(chain(iterables))

#ジェネレータ利用時の注意点
#ジェネレータはリストやタプルと同じくイテラブルとして使える
def gen(n):
    while n:
        yield n
        n -= 1

#zip()にリストとジェネレータを同時に渡す
result8 = [i for i in zip(x,gen(5))]
#filter()にジェネレータを渡す
odd = filter(lambda x: x % 2 == 1,gen(5))
result9 = [i for i in odd]

#ジェネレータはlen()の引数としては利用できない
#len(gen(5))
#ジェネレータをリスト化すればlen()の引数として利用可
result10 = len(list(gen(5)))

#ジェネレータは状態を保持する
g = gen(4)
#1回目のlen(list(g))で最後まで到達
result11 = len(list(g))
#2回目以降は0
result12 = len(list(g))
#2回目も使用したいならリスト化する
list_num = list(gen(4))
print(len(list_num))
print(len(list_num))

#ファイルの中身を大文字に変換し、新しいファイルに書き込むプログラム
#ファイルを１行ずつ読み込むジェネレータ関数reader()を作成
#その戻り値をwriter()に渡す
#writer()は受け取ったイテレータを利用してファイルを１行ずつ読込、convert()関数で変換しながら
#新ファイルに書込み

#ファイルの中身を１行づつ読み込む
def reader(src):
    with open(src,"r") as f:
        for line in f:
            yield line

#１行ずつ読み込んだ結果を大文字に変換
def convert(line):
    return line.upper()

#1行づつ大文字変換した結果を新ファイルに書込み
def writer(dest,reader):
    with open(dest,"w") as f:
        for line in reader:
            f.write(convert(line))
#reader()には存在するファイルのパスを渡す
writer("dest.rtf",reader("src.rtf"))
        
    
