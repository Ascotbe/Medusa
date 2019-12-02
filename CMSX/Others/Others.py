#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import Cms.Others.Alkawebs_viewnews_sqli
import Cms.Others.Anmai_grghjl_stuNo_sqli
import Cms.Others.Anmai_teachingtechnology_sqli

import Cms.Others.Caitong_multi_sqli
import Cms.Others.Clib_kindaction_fileread
import Cms.Others.Clib_kinweblistaction_download
import Cms.Others.Damall_selloffer_sqli
import Cms.Others.Dkcms_database_disclosure
import Cms.Others.Domino_unauth
import Cms.Others.Efuture_downloadAct_filedownload
import Cms.Others.Eis_menu_left_edit_sqli
import Cms.Others.Euse_study_multi_sqli
import Cms.Others.Gevercms_downLoadFile_filedownload
import Cms.Others.Gn_consulting_sqli
import Cms.Others.Gxwssb_fileDownloadmodel_download
import Cms.Others.Gpcsoft_ewebeditor_weak
import Cms.Others.Haohan_FileDown_filedownload
import Cms.Others.Hezhong_list_id_sqli

import Cms.Others.Hnkj_researchinfo_dan_sqli
import Cms.Others.Hongan_dlp_struts_exec
import Cms.Others.Huaficms_bypass_js
import Cms.Others.Ips_community_suite_code_exec
import Cms.Others.Jiuyu_library_struts_exec
import Cms.Others.Jxt1039_unauth
import Cms.Others.Kj65n_monitor_sqli
import Cms.Others.Lianbang_multi_bypass_priv
import Cms.Others.Mainone_b2b_Default_sqli
import Cms.Others.Mainone_ProductList_sqli
import Cms.Others.Mainone_SupplyList_sqli
import Cms.Others.Mallbuilder_change_status_sqli
import Cms.Others.Mingteng_cookie_deception
import Cms.Others.Newedos_multi_sqli
import Cms.Others.Nongyou_Item2_sqli
import Cms.Others.Nongyou_multi_sqli
import Cms.Others.Nongyou_ShowLand_sqli

import Cms.Others.Rap_interface_struts_exec
import Cms.Others.Shiyou_list_keyWords_sqli
import Cms.Others.Sinda_downloadfile_download
import Cms.Others.Skytech_bypass_priv
import Cms.Others.Skytech_geren_list_page_sqli
import Cms.Others.Star_PostSuggestion_sqli
import Cms.Others.Suntown_upfile_fileupload
import Cms.Others.Tianbo_Class_Info_sqli
import Cms.Others.Tianbo_St_Info_sqli
import ClassCongregation
import Cms.Others.Tianbo_TCH_list_sqli
import Cms.Others.Tianbo_Type_List_sqli
import Cms.Others.Tpshop_eval_stdin_code_exec
import Cms.Others.Workyi_multi_sqli
import Cms.Others.Zhuofan_downLoadFile_download

def Main(Url,FileName,Values,ProxyIp):
    WriteFile = ClassCongregation.WriteFile(FileName)  # 声明调用类集合中的WriteFile类,并传入文件名字(这一步是必须的)
    ua=ClassCongregation.UserAgentS(Values)#传入用户输入用户指定的浏览器头
    RandomAgent=ua.UserAgent()#获取生成的头文件
    try:
        Medusa=Cms.Others.Alkawebs_viewnews_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Anmai_grghjl_stuNo_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Anmai_teachingtechnology_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")

    try:
        Medusa=Cms.Others.Caitong_multi_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Clib_kindaction_fileread.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Clib_kinweblistaction_download.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")

    try:
        Medusa=Cms.Others.Damall_selloffer_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Dkcms_database_disclosure.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa= Cms.Others.Domino_unauth.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Efuture_downloadAct_filedownload.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Eis_menu_left_edit_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")

    try:
        Medusa=Cms.Others.Euse_study_multi_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Gevercms_downLoadFile_filedownload.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Gn_consulting_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Gxwssb_fileDownloadmodel_download.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Gpcsoft_ewebeditor_weak.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")

    try:
        Medusa=Cms.Others.Haohan_FileDown_filedownload.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Hezhong_list_id_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")

    try:
        Medusa=Cms.Others.Hnkj_researchinfo_dan_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Hongan_dlp_struts_exec.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")

    try:
        Medusa=Cms.Others.Huaficms_bypass_js.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Ips_community_suite_code_exec.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Jiuyu_library_struts_exec.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Jxt1039_unauth.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Kj65n_monitor_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")

    try:
        Medusa=Cms.Others.Lianbang_multi_bypass_priv.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Mainone_b2b_Default_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Mainone_ProductList_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Mainone_SupplyList_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Mallbuilder_change_status_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")

    try:
        Medusa=Cms.Others.Mingteng_cookie_deception.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Newedos_multi_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Nongyou_Item2_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Nongyou_multi_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Nongyou_ShowLand_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")

    try:
        Medusa=Cms.Others.Rap_interface_struts_exec.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Shiyou_list_keyWords_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Sinda_downloadfile_download.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Skytech_bypass_priv.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Skytech_geren_list_page_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Star_PostSuggestion_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Suntown_upfile_fileupload.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Tianbo_Class_Info_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Tianbo_St_Info_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Tianbo_TCH_list_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Tianbo_Type_List_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Tpshop_eval_stdin_code_exec.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Workyi_multi_sqli.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")
    try:
        Medusa=Cms.Others.Zhuofan_downLoadFile_download.medusa(Url,RandomAgent,ProxyIp)
        WriteFile.Write(Medusa)
    except:
        pass
        #print("[-]NginxDirectoryTraversalVulnerability Scan error")

