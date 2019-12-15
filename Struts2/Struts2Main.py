#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Struts2 import S2_001
from Struts2 import S2_007
from Struts2 import S2_012
from Struts2 import S2_013
from Struts2 import S2_016
from Struts2 import S2_052
from Struts2 import S2_053
from Struts2 import S2_057
import ClassCongregation
from tqdm import tqdm

def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    Medusa = [S2_001.medusa(Url,RandomAgent,ProxyIp),S2_007.medusa(Url,RandomAgent,ProxyIp),S2_012.medusa(Url,RandomAgent,ProxyIp),S2_013.medusa(Url,RandomAgent,ProxyIp),S2_016.medusa(Url,RandomAgent,ProxyIp),S2_052.medusa(Url,RandomAgent,ProxyIp),S2_053.medusa(Url,RandomAgent,ProxyIp),S2_057.medusa(Url,RandomAgent,ProxyIp),]
    try:
        for i in tqdm(Medusa, ascii=True, desc="Struts2 plugin progress:"):
            WriteFile.Write(str(i))
    except:
        pass

