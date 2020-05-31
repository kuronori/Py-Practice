#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:48:38 2020

@author: TakahiroKurokawa
"""

book='book'
print(1,type(book))

notebook='note\nbook'
print(2,notebook)

notebook="""
note
book
"""
print(3,notebook)

URL=('https://gihyo.jp'
     '/magazine/wdpress/archive'
     '/2018/vol104')
print(4,URL)

book='book'
print(5,'note'+book)
print(6,book*4)

for char in book:
    print(char)

print(7,bool(""))
print(8,bool(book))
print(9,"oo" in book)
print(10,"x" not in book)

title="book"
print(11,f"python practice {title}")
print(12,f'python practice {"note" +title}')

def print_title():
    print(f"python practice {title}")
print_title()
title="sketchbook"
print_title()

note='note'
print(13,f'title={title},note={note}')
#print(f'{title=},{note=}')

book='Python実践入門'
print(14,type(book))
print(15,book)

encoded=book.encode('utf-8')
print(16,type(encoded))
print(17,encoded)

decoded=encoded.decode('utf-8')
print(18,decoded)
