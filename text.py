#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
a=requests.post("http://127.0.0.1:8000/test/",data="id=11111111")
print(a.text)
print(a.status_code)
