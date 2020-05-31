#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 13:44:41 2020

@author: TakahiroKurokawa
"""

#ThreadPoolExecutorはExecutorの具象サブクラス
from concurrent.futures import (
    ThreadPoolExecutor,
    Future)

#非同期に行いたい処理
def func():
    return 1

#非同期に行いたい処理をsubmit()に渡す
future = ThreadPoolExecutor().submit(func)
print(isinstance(future, Future))

#非同期で実行した処理の戻り値を取得
print(future.result())

#現在の状態を確認する
print(future.done())
print(future.running())
print(future.cancelled())

#マルチスレッドは、通信を伴うI/Oバウンド処理に有効
#複数のサイトのトップページを取得する処理

#download()関数は、URLを一つ受け取り、そのページをファイルに保存する関数
#対象ページのURL一覧
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
print(download(urls[0]))

#逐次処理を実装
import time
def elapsed_time(f):
    def wrapper(*args,**kwargs):
        st = time.time()
        v = f(*args,**kwargs)
        print(f"{f.__name__}:{time.time()-st}")
        return v
    return wrapper

@elapsed_time
def get_sequential():
    for url in urls:
        print(download(url))
get_sequential()

#マルチスレッドで実装
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
    )

@elapsed_time
def get_multi_thread():
    #max_workersのデフォルトはコア数5
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download,url)
                   for url in urls]
        for future in as_completed(futures):
            #完了したものから取得できる
            print(future.result())
get_multi_thread()        