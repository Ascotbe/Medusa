from Web.DatabaseHub import NistData
from Web.Notification.DingTalk import Send


a=NistData().Bot(time_difference=500000)
m=""
print(len(a))
for i in a[:50]:
    m+="### 编号:"+str(i["vulnerability_number"])+"\r\n"
    if i["v3_base_score"]!="" and i["v3_base_severity"]!="":
        if i["v3_base_severity"]=="HIGH":
            m+="CVSS3:"+str(i["v3_base_score"])+"🔴"+str(i["v3_base_severity"])+"\r\n  "
        elif i["v3_base_severity"]=="MEDIUM":
            m+="CVSS3:"+str(i["v3_base_score"])+"🟡"+str(i["v3_base_severity"])+"\r\n  "
        elif i["v3_base_severity"]=="LOW":
            m+="CVSS3:"+str(i["v3_base_score"])+"🟢"+str(i["v3_base_severity"])+"\r\n  "
    if i["v2_base_score"]!="" and i["v2_base_everity"]!="":
        if  i["v2_base_severity"]=="HIGH":
            m+="CVSS2:"+str(i["v2_base_score"])+"🔴"+str(i["v2_base_severity"])+"\r\n  "
        elif i["v2_base_severity"]=="MEDIUM":
            m+="CVSS2:"+str(i["v2_base_score"])+"🟠"+str(i["v2_base_severity"])+"\r\n  "
        elif i["v2_base_severity"]=="LOW":
            m+="CVSS2:"+str(i["v2_base_score"])+"🟢"+str(i["v2_base_severity"])+"\r\n  "

    m+="\n描述:\n > "+str(i["vulnerability_description"])+"\r\n  "
    if len(i["vendors"])>0:
        m+= "\n厂商:"
        for x in i["vendors"]:
            m+=x+" "
        m+="\r\n  "
    if len(i["products"])>0:
        m+= "\n产品:"
        for x in i["products"]:
            m+=x+" "
        m+="\r\n  "

Send(message=m)