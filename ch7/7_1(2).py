#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:36:16 2020

@author: TakahiroKurokawa
"""

import encoder2
#変数encoder2はmoduleクラスのインスタンス
print(1,type(encoder2))
#encoder2モジュールのトップレベルのオブジェクトが確認できる
print(2,dir(encoder2))
result = encoder2.str_to_base64("python")
print(3,result)