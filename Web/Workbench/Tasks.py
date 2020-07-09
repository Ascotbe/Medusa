from Web.celery import app
from Modules.Confluence import Confluence
from Modules.Struts2 import Struts2
from Modules.Nginx import Nginx
from Modules.Jenkins import Jenkins
from Modules.Cms import Cms
from Modules.FastJson import FastJson
from Modules.Harbor import Harbor
from Modules.Citrix import Citrix
from Modules.InformationLeakage import InformationLeakage
from Modules.Rails import Rails
from Modules.Kibana import Kibana
from Modules.PHPStudy import PHPStudy
from Modules.Mongo import Mongo
from Modules.Liferay import Liferay
from Modules.Weblogic import Weblogic
from Modules.OA.Seeyou import Seeyou
from Modules.OA.Tongda import Tongda
from Modules.OA.Weaver import Weaver
from Modules.OA.Ruvar import Ruvar
from Modules.Windows import Windows
from Modules.Spring import Spring
from Modules.Apache.Shiro import Shiro
from Modules.Apache.Flink import Flink
from Modules.Apache.Log4j import Log4j
from Modules.Apache.ActiveMQ import ActiveMQ
from Modules.Apache.Solr import Solr
from Modules.Apache.Tomcat import Tomcat
from Modules.Subdomain.SubdomainSearch import SubdomainSearch
from ClassCongregation import ProcessPool
MedusaVulnerabilityList={
"Struts2":Struts2.Main,
"Confluence":Confluence.Main,
"Nginx":Nginx.Main,
"PHPStudy": PHPStudy.Main,
"Cms": Cms.Main,
"Jenkins": Jenkins.Main,
"Harbor": Harbor.Main,
"Rails":Rails.Main,
"Kibana":Kibana.Main,
"Citrix":Citrix.Main,
"Mongo":Mongo.Main,
"Spring":Spring.Main,
"FastJson":FastJson.Main,
"Windows":Windows.Main,
"Liferay":Liferay.Main,
"Shiro":Shiro.Main,
"Flink":Flink.Main,
"Log4j":Log4j.Main,
"ActiveMQ":ActiveMQ.Main,
"Solr":Solr.Main,
"Tomcat":Tomcat.Main,
"Ruvar":Ruvar.Main,
"Seeyou":Seeyou.Main,
"Tongda":Tongda.Main,
"Weaver":Weaver.Main,
"Weblogic":Weblogic.Main,
"InformationLeakage":InformationLeakage.Main
}

@app.task
def MedusaScan(Url,Module,ScanThreads,Values,proxies,**kwargs):
    WebProcessPool =ProcessPool()#定义一个线程池
    if Module=="all":
        for MedusaVulnerability in MedusaVulnerabilityList:
            MedusaVulnerabilityList[MedusaVulnerability](WebProcessPool, Url, Values, proxies,**kwargs)#调用列表里面的值

    else:
        try:
            MedusaVulnerabilityList[Module](WebProcessPool, Url, Values, proxies,**kwargs)  # 调用列表里面的值
        except:#如果传入非法字符串会调用出错
            pass
    WebProcessPool.Start(ScanThreads)






