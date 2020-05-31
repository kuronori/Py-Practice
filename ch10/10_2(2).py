#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:50:48 2020

@author: TakahiroKurokawa
"""

#ThreadPoolExecutorクラスはExecutorクラスのサブクラス
from concurrent.futures import ThreadPoolExecutor,Future

#非同期に行いたい処理
def func():
    return 1

#非同期に行いたい処理をThreadPoolExecutorクラスのメソッドsubmit()に渡す
future = ThreadPoolExecutor().submit(func)
print(1,isinstance(future,Future))
result = future.result()
print(2,f"result={result}")
print(3,f"done={future.done()}")
print(4,f"running={future.running()}")
print(5,f"cancelled={future.cancelled()}")


#対象ページのurl一覧
urls = [
        "https://twitter.com",
        "https://facebook.com",
        "https://instagram.com"
        ]

from hashlib import md5
from pathlib import Path
from urllib import request

def download(url):
    req = request.Request(url)
    #ファイル名に/などが含まれないようにする
    name = md5(url.encode("utf-8")).hexdigest()
    file_path = "./" + name
    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url,file_path

#動きを確認
print(6,download(urls[0]))


import time

def elapsed_time(f):
    def wrapper(*args,**kwargs):
        st = time.time()
        v = f(*args,**kwargs)
        print(f"{f.__name__}= {time.time()-st}")
        return v
    return wrapper

@elapsed_time
def sequential(urls):
    result = []
    for url in urls:
        print(download(url))
    
#逐次処理で実行
print(7,"逐次処理")
sequential(urls)

#マルチスレッドで実装
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
    )

@elapsed_time
def multi_thread(urls):
    with ThreadPoolExecutor(max_workers = 3) as executor:
        futures = [executor.submit(download,url) for url in urls]
    for future in as_completed(futures):
        print(future.result())

print(8,"マルチスレッド")
multi_thread(urls)
        
        




