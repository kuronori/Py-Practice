#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:59:50 2020

@author: TakahiroKurokawa
"""
#__init__.pyが実行される
import b64

print(1,type(b64))
#dir(encoder2)にはなかった__path__が確認できる
print(2,dir(b64))
print(3,b64.__path__)

#from文でも__init__.pyが実行される
from b64 import encoder2,decoder2
#文字列のbase64形式表現
result = encoder2.str_to_base64("python")
print(4,result)
result2 = decoder2.base64_to_str(result)
print(5,result2)

#b64の属性として参照
result = b64.str_to_base64("python")
result2 = b64.base64_to_str(result)

#下記２文は同じ
from b64 import str_to_base64,base64_to_str
from b64 import (
    str_to_base64,
    base64_to_str)

#パッケージ内部のモジュールをインポート
from b64 import encoder2
result = encoder2.str_to_base64("python")

#属性を再帰的に指定してインポート
from b64.encoder2 import str_to_base64
result = str_to_base64("python")

#名前の衝突を防ぐas
print(6,open)
#from gzip import open as open
#print(7,open)

from gzip import open as gzip_open
print(8,open)
print(9,gzip_open)