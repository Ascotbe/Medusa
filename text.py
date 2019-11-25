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
        json_values={}
        for i in values:
            json_values["id"]=i[0]
            json_values["name"] =i[1]
            json_values["affects"] =i[2]
            json_values["rank"] =i[3]
            json_values["suggest"] =i[4]
            json_values["desc_content"] =i[5]
            json_values["details"] =i[6]
        self.con.close()
        return json_values
VulnerabilityInquire("6").Inquire()