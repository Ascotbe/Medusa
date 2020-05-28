from Web.WebClassCongregation import GetTemplateFolderLocation,GetDownloadFolderLocation
from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm
def GenerateWordReport(VulnerabilityDataList,**kwargs):
    #读取模板文档
    tpl = DocxTemplate(GetTemplateFolderLocation().Result()+'WordTemplate.docx')
    vulnerabulity=[]
    for i in VulnerabilityDataList:
        vulnerabulity.append({'vulnerability_name': i.get("vulnerability_name"),
             'vulnerability_address': i.get("vulnerability_address"),
             'vulnerability_level': i.get("vulnerability_level"), 'find_the_time': i.get("find_the_time"),
             'vulnerability_description': i.get("vulnerability_description"),
             'vulnerability': i.get("vulnerability"), 'vulnerability_details': i.get("vulnerability_details"),
             'repair_suggestions': i.get("repair_suggestions")})
    context = {
        'target_url':kwargs.get("target_url"),
        'number_of_vulnerabilities_in_the_target_website':kwargs.get("number_of_vulnerabilities_in_the_target_website"),
        'home_picture':InlineImage(tpl,GetTemplateFolderLocation().Result()+"home_picture.jpg",width=Mm(600)),
        'vulnerability' : vulnerabulity,
    }
    tpl.render(context)
    tpl.save(GetDownloadFolderLocation().Result()+'test.docx')


# GenerateWordReport(VulnerabilityDataList=[{"vulnerability_name":"1111","vulnerability_address":"123","vulnerability_level":"114","find_the_time":"222","vulnerability_description":"1233","vulnerability":"3333","vulnerability_details":"fff","repair_suggestions":"4f"},{"vulnerability_name":"1111","vulnerability_address":"123","vulnerability_level":"114","find_the_time":"222","vulnerability_description":"1233","vulnerability":"3333","vulnerability_details":"fff","repair_suggestions":"4f"},{"vulnerability_name":"1111","vulnerability_address":"123","vulnerability_level":"114","find_the_time":"222","vulnerability_description":"1233","vulnerability":"3333","vulnerability_details":"fff","repair_suggestions":"4f"}
#                                           ],target_url="ddd.ddd",number_of_vulnerabilities_in_the_target_website="fafa",)