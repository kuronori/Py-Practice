#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:47:10 2020

@author: TakahiroKurokawa
"""

#マルチスレッドでの実装の注意点
#threading.Lockオブジェクトによる排他制御

#2つのスレッドが1,000,000回ずつカウンタをインクリメント
#self.count = self.count + 1が問題
#「現在の値を読み込む」、「１をたす」、「結果を代入する」
#この処理の途中でスレッドが切り替わるとself.countに同時に2つのスレッドがアクセスする

from concurrent.futures import (
    ThreadPoolExecutor,
    wait
    )

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        #問題の箇所
        self.count = self.count + 1

def count_up(counter):
    #1,000,000回インクリメントする
    for _ in range(1_000_000):
        counter.increment()

counter = Counter()
threads = 2
with ThreadPoolExecutor() as e:
    #2つのスレッドを用意し、それぞれでcount_upを呼び出す
    futures = [e.submit(count_up,counter) for _ in range(threads)]
    done,not_done = wait(futures)

print(9,f"counter.count = {counter.count:,}")

import threading
class ThreadSafeCounter:
    #ロックを用意する
    lock = threading.Lock()
    def __init__(self):
        self.count = 0
    def increment(self):
        with self.lock:
            #排他制御したい一連の処理をこのブロック内に書く
            self.count = self.count + 1

counter = ThreadSafeCounter()
threads = 2

with ThreadPoolExecutor() as e:
    futures = [e.submit(count_up,counter)
               for _ in range(threads)]
    done,not_done = wait(futures)

print(10,f"counter.count = {counter.count:,}")


     
