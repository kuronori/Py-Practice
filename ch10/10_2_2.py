#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:31:01 2020

@author: TakahiroKurokawa
"""

from concurrent.futures import (
    ThreadPoolExecutor,
    wait)

class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count = self.count + 1
def count_up(counter):
    #1,000,000回インクリメントする
    for _ in range(1_000_000):
        counter.increment()

counter = Counter()
threads = 2

with ThreadPoolExecutor() as e:
    #2つのスレッドを用意し、それぞれでcount_upを呼び出す
    futures = [e.submit(count_up,counter)
               for _ in range(threads)]
    done,not_done = wait(futures)
#2,000,000になっていない
print(f"{counter.count}")

import threading
class ThreadSafecounter:
    #ロックを用意する
    lock = threading.Lock()
    def __init__(self):
        self.count = 0
    def increment(self):
        with self.lock:
            #排他制御したい一連の処理をこのブロック内に書く
            self.count = self.count + 1

counter = ThreadSafecounter()
threads = 2

with ThreadPoolExecutor() as e:
    futures = [e.submit(count_up,counter)
               for _ in range(threads)]
    done,not_done = wait(futures)
#2,000,000になっている
print(f"{counter.count}")


           