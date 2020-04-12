#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import threading
import requests
from ClassCongregation import AgentHeader,ErrorLog,VulnerabilityDetails,WriteFile,UrlProcessing,ErrorHandling,Proxies
class TargetInfo:
    def __init__(self,Medusa,Algroup,Name,Affects):
        self.info = {}
        self.info['number'] = "0"  # 如果没有CVE或者CNVD编号就填0，CVE编号优先级大于CNVD
        self.info['author'] = "Ascotbe"  # 插件作者
        self.info['create_date'] = "2020-2-15"  # 插件编辑时间
        self.info['disclosure'] = '2020-2-15'  # 漏洞披露时间，如果不知道就写编写插件的时间
        self.info['algroup'] = Algroup  # 插件名称
        self.info['name'] = Name  # 漏洞名称
        self.info['affects'] = Affects  # 漏洞组件
        self.info['desc_content'] = "敏感文件未删除，导致用户可以访问或者下载，造成大量的数据或源码泄露。"  # 漏洞描述
        self.info['rank'] = "高危"  # 漏洞等级
        self.info['suggest'] = "删除文件或者对对路径限制访问"  # 修复建议
        self.info['version'] = "无"  # 这边填漏洞影响的版本
        self.info['details'] = Medusa  # 结果




class SensitiveFile:
    def __init__(self):
        self.Thread=[]#多线程列表
        self.TargetList=[]#存放目标URL
        self.headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'User-Agent': AgentHeader().result("chrome"),
        }
        # global TargetName
        # if sys.platform == "win32" or sys.platform == "cygwin":
        #     TargetName = os.path.split(os.path.realpath(__file__))[
        #                   0] + "\\Target\\"
        # elif sys.platform == "linux" or sys.platform == "darwin":
        #     TargetName = os.path.split(os.path.realpath(__file__))[0] + "/Target/"


    def GetRequest(self,url):#get请求模块
        return requests.get(url,headers=self.headers, timeout=5,proxies=self.proxies, verify=False)
    def PostRequest(self,url,data):#post请求模块
        return requests.post(url,headers=self.headers,data=data,proxies=self.proxies, timeout=5, verify=False)
    def Druid(self,url):
        Algroup="DruidMonitoringSystemLeakVulnerability"
        Name="Druid监控系统泄露漏洞"
        Affects="Druid"
        DruidThreadList=[]#该模块中的多线程
        list = ['/index.html', '/datasource.html', '/sql.html', '/wall.html', '/webapp.html', '/weburi.html',
                '/websession.html', '/spring.html']
        for payload in list:
            urls = url+ '/druid' + payload
            DruidThreadList.append(threading.Thread(target=self.DruidThread, args=(urls,Algroup,Name,Affects,)))
        for t in DruidThreadList:  # 开启列表中的多线程
            t.setDaemon(True)
            t.start()
        for t in DruidThreadList:
            t.join()


    def DruidThread(self,urls,Algroup,Name,Affects):
        try:
            resp=self.GetRequest(urls)
            con = resp.text
            code = resp.status_code
            if code == 200 and con.lower().find('druid.common') != -1:
                Medusa = "{}存在{}\r\n漏洞详情:{}\r\n".format(urls, Name, con)
                _t = TargetInfo(Medusa, Algroup, Name, Affects)
                VulnerabilityDetails(_t.info, urls,self.Token).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(self.TargetUrl), str(Medusa))
        except Exception as e:
            _l = ErrorLog().Write(urls, Name)  # 调用写入类传入URL和错误插件名
            _ = TargetInfo('',Algroup,Name,Affects).info.get('algroup')
            ErrorHandling().Outlier(e, _)

    def Git(self,url):
        Algroup="GitVersionManagementSourceLeakVulnerability"
        Name="Git版本管理源码泄露漏洞"
        Affects="Git"
        urls = url+ '/.git/config'
        try:
            resp=self.GetRequest(urls)
            con = resp.text
            code = resp.status_code
            if code==200 and con.lower().find('repositoryformatversion')!=-1 :
                Medusa = "{}存在{}\r\n漏洞详情:{}\r\n".format(urls,Name, con)
                _t = TargetInfo(Medusa,Algroup,Name,Affects)
                VulnerabilityDetails(_t.info, urls, self.Token).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(self.TargetUrl), str(Medusa))
        except Exception as e:
            _l = ErrorLog().Write(url, Name)  # 调用写入类传入URL和错误插件名
            _ = TargetInfo('', Algroup, Name, Affects).info.get('algroup')
            ErrorHandling().Outlier(e, _)
    def Java(self,url):
        Algroup="JavaConfigurationFile"
        Name="Java配置文件泄露漏洞"
        Affects="Java"
        urls = url+ "/WEB-INF/web.xml"
        try:
            resp=self.GetRequest(urls)
            con = resp.text
            code = resp.status_code
            if code == 200 and resp.headers["Content-Type"] == "application/xml":
                Medusa = "{}存在{}\r\n漏洞详情:{}\r\n".format(urls,Name, con)
                _t = TargetInfo(Medusa,Algroup,Name,Affects)
                VulnerabilityDetails(_t.info, urls,self.Token).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(self.TargetUrl), str(Medusa))

        except Exception as e:
            _l = ErrorLog().Write(url, Name)  # 调用写入类传入URL和错误插件名
            _ = TargetInfo('', Algroup, Name, Affects).info.get('algroup')
            ErrorHandling().Outlier(e, _)
    def JetBrains(self,url):
        Algroup="JetBrainsFileLeakVulnerability"
        Name="JetBrains文件泄露漏洞"
        Affects="JetBrains"
        urls = url+ "/.idea/workspace.xml"
        try:
            resp=self.GetRequest(urls)
            con = resp.text
            code = resp.status_code
            if code==200 and con.lower().find('<?xml version=')!=-1 and con.lower().find('project version')!=-1:
                Medusa = "{}存在{}\r\n漏洞详情:{}\r\n".format(urls,Name, con)
                _t = TargetInfo(Medusa,Algroup,Name,Affects)
                VulnerabilityDetails(_t.info, urls,self.Token).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(self.TargetUrl), str(Medusa))
        except Exception as e:
            _l = ErrorLog().Write(url, Name)  # 调用写入类传入URL和错误插件名
            _ = TargetInfo('', Algroup, Name, Affects).info.get('algroup')
            ErrorHandling().Outlier(e, _)
    def PhpApc(self,url):
        Algroup="PhpApcCachePageInformationDisclosureVulnerability"
        Name="PhpApc缓存页面信息泄露漏洞"
        Affects="PhpApc"
        urls = url+ '/apc.php'
        try:
            resp=self.GetRequest(urls)
            con = resp.text
            code = resp.status_code
            if code==200 and con.lower().find('apc version')!=-1:
                Medusa = "{}存在{}\r\n漏洞详情:{}\r\n".format(urls,Name, con)
                _t = TargetInfo(Medusa,Algroup,Name,Affects)
                VulnerabilityDetails(_t.info, urls,self.Token).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(self.TargetUrl), str(Medusa))
        except Exception as e:
            _l = ErrorLog().Write(url, Name)  # 调用写入类传入URL和错误插件名
            _ = TargetInfo('', Algroup, Name, Affects).info.get('algroup')
            ErrorHandling().Outlier(e, _)
    def Sftp(self,url):
        Algroup="SftpInformationDisclosureVulnerability"
        Name="Sftp信息泄露漏洞"
        Affects="Sftp"
        urls = url+ '/sftp-config.json'
        try:
            resp=self.GetRequest(urls)
            con = resp.text
            code = resp.status_code
            if code==200 and con.lower().find('remote_path')!=-1:
                Medusa = "{}存在{}\r\n漏洞详情:{}\r\n".format(urls,Name, con)
                _t = TargetInfo(Medusa,Algroup,Name,Affects)
                VulnerabilityDetails(_t.info, urls,self.Token).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(self.TargetUrl), str(Medusa))
        except Exception as e:
            _l = ErrorLog().Write(url, Name)  # 调用写入类传入URL和错误插件名
            _ = TargetInfo('', Algroup, Name, Affects).info.get('algroup')
            ErrorHandling().Outlier(e, _)
    def Svn(self,url):
        Algroup="SvnVersionManagementSourceCodeLeakVulnerability"
        Name="Svn版本管理源码泄露漏洞"
        Affects="Svn"
        urls = url+ '/.svn/entries'
        try:
            resp=self.GetRequest(urls)
            con = resp.text
            code = resp.status_code
            if code==200 and (con.lower().find('svn://')!=-1 or con.lower().find('svn://')!=-1 or con.lower().find('svn://')!=-1):
                Medusa = "{}存在{}\r\n漏洞详情:{}\r\n".format(urls,Name, con)
                _t = TargetInfo(Medusa,Algroup,Name,Affects)
                VulnerabilityDetails(_t.info, urls,self.Token).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(self.TargetUrl), str(Medusa))
        except Exception as e:
            _l = ErrorLog().Write(url, Name)  # 调用写入类传入URL和错误插件名
            _ = TargetInfo('', Algroup, Name, Affects).info.get('algroup')
            ErrorHandling().Outlier(e, _)
    def PhpInfo(self,url):
        Algroup="PhpInfoTestScriptLeakVulnerability"
        Name="PhpInfo测试脚本泄露漏洞"
        Affects="PhpInfo"
        PhpInfoThreadList=[]
        list = [
            '/index.php',
            '/1.php',
            '/2.php',
            '/3.php',
            '/4.php',
            '/5.php',
            '/6.php',
            '/7.php',
            '/8.php',
            '/9.php',
            '/10.php',
            '/11.php',
            '/12.php',
            '/13.php',
            '/123.php',
            '/1234.php',
            '/12345.php',
            '/123456.php',
            '/a.php',
            '/b.php',
            '/c.php',
            '/d.php',
            '/e.php',
            '/f.php',
            '/g.php',
            '/h.php',
            '/i.php',
            '/j.php',
            '/k.php',
            '/l.php',
            '/m.php',
            '/n.php',
            '/o.php',
            '/p.php',
            '/q.php',
            '/r.php',
            '/s.php',
            '/t.php',
            '/u.php',
            '/v.php',
            '/w.php',
            '/x.php',
            '/y.php',
            '/z.php',
            '/php.php',
            '/abc.php',
            '/test.php',
            '/test1.php',
            '/test2.php',
            '/test3.php',
            '/test123.php',
            '/info.php',
            '/phpinfo.php',
            '/iProber.php',
            '/iProber1.php',
            '/iProber2.php',
            '/iProber3.php',
            '/test_phpinfo.php',
            '/tools/info.php',
            '/ship/phpinfo.php',
            '/web/info.php',
            '/web/phpinfo.php',
            '/xampp/info.php',
            '/xampp/phpinfo.php',
            '/index.php?act=phpinfo',
            '/dashboard/phpinfo.php'
        ]
        for payload in list:
            urls = url+ payload
            PhpInfoThreadList.append(threading.Thread(target=self.PhpInfoThread, args=(urls,Algroup,Name,Affects,)))

        for t in PhpInfoThreadList:  # 开启列表中的多线程
            t.setDaemon(True)
            t.start()
        for t in PhpInfoThreadList:
            t.join()

    def PhpInfoThread(self,urls,Algroup,Name,Affects):
        try:
            resp=self.GetRequest(urls)
            con = resp.text
            code = resp.status_code
            if code == 200 and con.lower().find('<title>phpinfo()</title>') != -1:
                Medusa = "{}存在{}\r\n漏洞详情:{}\r\n".format(urls, Name, con)
                _t = TargetInfo(Medusa, Algroup, Name, Affects)
                VulnerabilityDetails(_t.info, urls,self.Token).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(self.TargetUrl), str(Medusa))
        except Exception as e:
            _l = ErrorLog().Write(urls, Name)  # 调用写入类传入URL和错误插件名
            _ = TargetInfo('',Algroup,Name,Affects).info.get('algroup')
            ErrorHandling().Outlier(e, _)
    def CompressedFile(self,url):
        Algroup="SensitiveCompressedFileDownloadVulnerability"
        Name="敏感压缩文件下载漏洞"
        Affects="CompressedFile"
        CompressedFileThreadList=[]
        suffixs = [".zip", ".rar", ".tar.gz", ".tgz", ".7z"]
        payloads = ["/www.root",
                    "/bbs",
                    "/www",
                    "/wwwroot",
                    "/web",
                    "/root",
                    "/database",
                    "/db",
                    "/website",
                    "/config_ucenter.php",
                    "/config_global.php",
                    "/1",
                    "/123",
                    "/a",
                    ]
        for payload in payloads:
            for suffix in suffixs:
                urls = url + payload+suffix
                CompressedFileThreadList.append(threading.Thread(target=self.CompressedFileThread, args=(urls, Algroup, Name, Affects,)))
        for suffix in suffixs:#域名加上后缀
            urls = url +"/" +self.TargetUrl + suffix
            CompressedFileThreadList.append(
                threading.Thread(target=self.CompressedFileThread, args=(urls, Algroup, Name, Affects,)))

        for t in CompressedFileThreadList:  # 开启列表中的多线程
            t.setDaemon(True)
            t.start()
        for t in CompressedFileThreadList:
            t.join()

    def CompressedFileThread(self, urls, Algroup, Name, Affects):
        try:
            resp = self.GetRequest(urls)
            con = resp.text
            code = resp.status_code
            if code==200 and (resp.headers.get("Content-Type")== "application/zip" or resp.headers.get("Content-Type") == "application/x-rar-compressed" or resp.headers.get("Content-Type") == "application/x-gzip" or resp.headers.get("Content-Type") == "application/gzip") :
                Medusa = "{}存在{}\r\n漏洞详情:{}\r\n".format(urls, Name, con)
                _t = TargetInfo(Medusa, Algroup, Name, Affects)
                VulnerabilityDetails(_t.info, urls,self.Token).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(self.TargetUrl), str(Medusa))
        except Exception as e:
            _l = ErrorLog().Write(urls, Name)  # 调用写入类传入URL和错误插件名
            _ = TargetInfo('',Algroup,Name,Affects).info.get('algroup')
            ErrorHandling().Outlier(e, _)

    def SensitiveFile(self,url):
        Algroup="SensitiveFileDownloadVulnerability"
        Name="敏感文件下载漏洞"
        Affects="SensitiveFile"
        SensitiveFileThreadList=[]
        payloads = ["/root.txt",
                          "/db.txt",
                          "/password.txt",
                          "/username.txt",
                          "/database.txt"
                          ]
        for payload in payloads:
            urls = url + payload
            SensitiveFileThreadList.append(threading.Thread(target=self.SensitiveFileThread, args=(urls, Algroup, Name, Affects,)))

        for t in SensitiveFileThreadList:  # 开启列表中的多线程
            t.setDaemon(True)
            t.start()
        SensitiveFileThreadList.clear()#清空列表

    def SensitiveFileThread(self, urls, Algroup, Name, Affects):
        try:
            resp = self.GetRequest(urls)
            con = resp.text
            code = resp.status_code
            if code == 200 and resp.headers["Content-Type"] == "text/plain":
                Medusa = "{}存在{}\r\n漏洞详情:{}\r\n".format(urls, Name, con)
                _t = TargetInfo(Medusa, Algroup, Name, Affects)
                VulnerabilityDetails(_t.info, urls,self.Token).Write()  # 传入url和扫描到的数据
                WriteFile().result(str(self.TargetUrl), str(Medusa))
        except Exception as e:
            _l = ErrorLog().Write(urls, Name)  # 调用写入类传入URL和错误插件名
            _ = TargetInfo('',Algroup,Name,Affects).info.get('algroup')
            ErrorHandling().Outlier(e, _)
    def File(self,Target,Token,ThreadNumber,proxies=None):
        self.Token=Token
        self.proxies = Proxies().result(proxies)
        with open(Target, 'r', encoding='UTF-8') as f:
            line = f.readline()
            while line:
                self.TargetList.append(line.replace('\n', ''))  # 删除\n符号
                line = f.readline()
        for url in self.TargetList:
            scheme, self.TargetUrl, port = UrlProcessing().result(url)  # 获取目标的url
            self.Thread.append(threading.Thread(target=self.Druid, args=(url,)))
            self.Thread.append(threading.Thread(target=self.Git, args=(url,)))
            self.Thread.append(threading.Thread(target=self.Java, args=(url,)))
            self.Thread.append(threading.Thread(target=self.JetBrains, args=(url,)))
            self.Thread.append(threading.Thread(target=self.PhpApc, args=(url,)))
            self.Thread.append(threading.Thread(target=self.Sftp, args=(url,)))
            self.Thread.append(threading.Thread(target=self.Svn, args=(url,)))
            self.Thread.append(threading.Thread(target=self.PhpInfo, args=(url,)))
            self.Thread.append(threading.Thread(target=self.CompressedFile, args=(url,)))
            self.Thread.append(threading.Thread(target=self.SensitiveFile, args=(url,)))

        for t in self.Thread:  # 开启总中的多线程
            t.start()
            while True:
                # 判断正在运行的线程数量,如果小于5则退出while循环,
                # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                if (len(threading.enumerate()) < ThreadNumber):
                    break
        for t in self.Thread:
            t.join()

    def Domain(self, url,Token,ThreadNumber,proxies=None):
        self.Token = Token
        self.proxies = Proxies().result(proxies)
        scheme, self.TargetUrl, port = UrlProcessing().result(url)  # 获取目标的url

        self.Thread.append(threading.Thread(target=self.Druid, args=(url,)))
        self.Thread.append(threading.Thread(target=self.Git, args=(url,)))
        self.Thread.append(threading.Thread(target=self.Java, args=(url,)))
        self.Thread.append(threading.Thread(target=self.JetBrains, args=(url,)))
        self.Thread.append(threading.Thread(target=self.PhpApc, args=(url,)))
        self.Thread.append(threading.Thread(target=self.Sftp, args=(url,)))
        self.Thread.append(threading.Thread(target=self.Svn, args=(url,)))
        self.Thread.append(threading.Thread(target=self.PhpInfo, args=(url,)))
        self.Thread.append(threading.Thread(target=self.CompressedFile, args=(url,)))
        self.Thread.append(threading.Thread(target=self.SensitiveFile, args=(url,)))

        for t in self.Thread:  # 开启总中的多线程
            t.start()
            while True:
                # 判断正在运行的线程数量,如果小于5则退出while循环,
                # 进入for循环启动新的进程.否则就一直在while循环进入死循环
                if (len(threading.enumerate()) < ThreadNumber):
                    break
        for t in self.Thread:
            t.join()


