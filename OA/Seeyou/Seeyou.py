#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from OA.Seeyou import Seeyou_a8_logs_disclosure
from OA.Seeyou import Seeyou_cm_info_content_sqli
from OA.Seeyou import Seeyou_ehr_ELTextFile
from OA.Seeyou import Seeyou_fe_treeXml_sqli
from OA.Seeyou import Seeyou_getemaildata_fileread
from OA.Seeyou import Seeyou_icc_struts2
from OA.Seeyou import Seeyou_multi_union_sqli
from OA.Seeyou import Seeyou_NCFindWeb_fileread
from OA.Seeyou import Seeyou_status_default_pwd
from OA.Seeyou import Seeyou_test_sqli
from OA.Seeyou import Seeyou_user_ids_sqli
import ClassCongregation
from tqdm import tqdm

def Main(Url, FileName, Values, ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua = ClassCongregation.UserAgentS(Values)  # 传入用户输入用户指定的浏览器头
    RandomAgent = ua.UserAgent()  # 获取生成的头文件

    Medusa = [Seeyou_a8_logs_disclosure.medusa(Url, RandomAgent, ProxyIp),Seeyou_cm_info_content_sqli.medusa(Url, RandomAgent, ProxyIp),Seeyou_ehr_ELTextFile.medusa(Url, RandomAgent, ProxyIp),Seeyou_fe_treeXml_sqli.medusa(Url, RandomAgent, ProxyIp),Seeyou_getemaildata_fileread.medusa(Url, RandomAgent, ProxyIp),Seeyou_icc_struts2.medusa(Url, RandomAgent, ProxyIp),Seeyou_multi_union_sqli.medusa(Url, RandomAgent, ProxyIp),Seeyou_NCFindWeb_fileread.medusa(Url, RandomAgent, ProxyIp),Seeyou_status_default_pwd.medusa(Url, RandomAgent, ProxyIp),Seeyou_test_sqli.medusa(Url, RandomAgent, ProxyIp),Seeyou_user_ids_sqli.medusa(Url, RandomAgent, ProxyIp),]
    try:
        for i in tqdm(Medusa, ascii=True, desc="Seeyou plugin progress"):
            WriteFile.Write(str(i))
    except:
        pass

