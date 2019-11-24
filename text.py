#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sqlite3
import os
class VulnerabilityInquire:
    def __init__(self,pid):#先通过id查，后面要是有用户ID 再运行的时候创建一个用户信息的表或者什么的到时候再说
        self.id=pid
        self.con = sqlite3.connect(os.path.split(os.path.realpath(__file__))[0] + "\\Medusa.db")
        # 获取所创建数据的游标
        self.cur = self.con.cursor()
    def Inquire(self):

        sql = "select * from Medusa where id ='"+self.id+"'"

        self.cur.execute(sql)
        values = self.cur.fetchall()
        print(values)
        self.con.close()

VulnerabilityInquire("5").Inquire()