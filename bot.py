#!/usr/bin/python env
# -*- coding:utf-8 -*-

import nonebot
from os import path
import QQbot.bot_config

if __name__ == '__main__':
    nonebot.init(QQbot.bot_config)#使用默认配置初始化 NoneBot 包
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'QQbot'),
        'QQbot'
    )#加载 NoneBot 内置的插件
    nonebot.run()