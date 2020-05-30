from Web.WebClassCongregation import GetTemplateFolderLocation,GetDownloadFolderLocation
from docxtpl import DocxTemplate,InlineImage
import time
import base64
from ClassCongregation import ErrorLog,UrlProcessing
from docx.shared import Mm
def GenerateWordReport(VulnerabilityDataList,**kwargs):
    #读取模板文档
    try:
        tpl = DocxTemplate(GetTemplateFolderLocation().Result()+'WordTemplate.docx')
        Vulnerabulity=[]
        scheme, url, port = UrlProcessing().result(kwargs.get("target_url"))

        VulnerabilityNumber=0#计算漏洞个数用最后清零
        for i in VulnerabilityDataList:
            VulnerabilityNumber+=+1#自增
            Vulnerabulity.append({'vulnerability_name': i.get("vulnerability_name"),#漏洞名称
                 'vulnerability_level': i.get("vulnerability_level"),#漏洞级别
                'find_the_time': i.get("find_the_time"),#发现时间
                 'vulnerability_description': i.get("vulnerability_description"),#漏洞描述
                'vulnerability_details': str(base64.b64decode(i.get("vulnerability_details")),encoding='utf-8'),#.replace("\r\n","\a"),#漏洞细节，在word中\r\n需要替换成^l^p
                'vulnerability_number':VulnerabilityNumber,
                 'repair_suggestions': i.get("repair_suggestions")#修复建议
                                  })
        context = {
            'target_url':scheme + "://" + url,#传入处理过的URL
            'number_of_vulnerabilities_in_the_target_website':VulnerabilityNumber,
            'home_picture':InlineImage(tpl,GetTemplateFolderLocation().Result()+"home_picture.jpg",width=Mm(120)),
            'vulnerability' : Vulnerabulity,
            'report_export_time':int(time.time()),
        }
        tpl.render(context)
        WordName=str(int(time.time()))+"_"+url+'.docx'#生成报告名字，这边经过处理不然Windows报错
        tpl.save(GetDownloadFolderLocation().Result()+WordName)
        VulnerabilityNumber=0
        return WordName#返回模板名字
    except Exception as e:
        ErrorLog().Write("Web_Api_ProcessingReport_GenerateWordReport(def)", e)
        return None

