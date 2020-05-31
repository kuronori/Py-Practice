#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:58:45 2020

@author: TakahiroKurokawa
"""

async def coro():
    return 1

import asyncio
import random
async def call_web_api(url):
    print(f'send a request:{url}')
    await asyncio.sleep(random.random())
    print(f'got a response:{url}')
    return url

async def async_download(url):
    response = await call_web_api(url)
    return response

result = asyncio.run(async_download('https://twitter.com/'))