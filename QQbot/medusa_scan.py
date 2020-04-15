import ClassCongregation
import time
import hashlib
import tldextract
from Confluence import ConfluenceMain
from Struts2 import Struts2
from Apache import ApacheMain
from Nginx import NginxMain
from Jenkins import JenkinsMain
from Cms import CmsMain
from FastJson import FastJson
from Harbor import Harbor
from Citrix import CitrixMain
from Rails import RailsMain
from Kibana import KibanaMain
from PHPStudy import PHPStudy
from Mongo import MongoMain
from OA import OaMian
from Windows import Windows
from Spring import SpringMain
from nonebot import on_command, CommandSession,message
from config import whitelist_group_list,whitelist_group_status
# on_command 装饰器将函数声明为一个命令处理器
@on_command('扫描')
async def Medusa(session: CommandSession):
    aims = session.get('aims', prompt='呐呐呐！对方的域名呐？')#如果用户输入扫描后面跟上空格就能识别了
    #user_url = aims[3:]#去除了@后面的值还有个空格所以要删3个字符
    print(aims)
    user_qq_id = session.event['user_id']#获取用户QQ
    user_scan_time=str(int(time.time()))#获取用户扫描时间轴
    encrypted_string=str(user_qq_id)+user_scan_time#对两个参数进行合并
    token = hashlib.md5(str(encrypted_string).encode("utf-8")).hexdigest()  # 对encrypted_string进行加密
    url_refining=tldextract.extract(aims)
    if whitelist_group_status:#开启白名单
        for whitelist_group in whitelist_group_list:
            if session.event['group_id'] == whitelist_group:#获取群ID
                if url_refining.suffix!="" and url_refining.domain!="" and url_refining.suffix!="gov.cn":#判断提炼出来的东西是否符合二级域名,限制政府网站
                    await session.send(message.MessageSegment.at(user_qq_id)+"\r\nToken:" + token + "\r\nKey:"+user_scan_time+"\r\nUrl:" + aims)
                    number_of_scan_results=await MedusaScan(aims,token)
                    if len(str(number_of_scan_results))>0:#扫描成功返回
                        await session.send(message.MessageSegment.at(user_qq_id)+ "\r\n存在漏洞个数:"+str(number_of_scan_results)+"\r\n如果需要查询结果请参考help中格式！")#艾特用户表示扫描完成科研查询了
                else:
                    await session.send("呐呐呐！小哥哥域名不合规呐(｡・`ω´･)")
            else:
                await session.send("呐呐呐！该群未开启扫描功能呐(｡・`ω´･)")
    else:#未开启白名单
        if url_refining.suffix != "" and url_refining.domain != "" and url_refining.suffix!="gov.cn":  # 判断提炼出来的东西是否符合二级域名
            await session.send(message.MessageSegment.at(
                user_qq_id) + "\r\nToken:" + token + "\r\nKey:" + user_scan_time + "\r\nUrl:" + aims)
            number_of_scan_results = await MedusaScan(aims, token)
            if len(str(number_of_scan_results)) > 0:  # 扫描成功返回
                await session.send(message.MessageSegment.at(user_qq_id) + "\r\n存在漏洞个数:" + str(
                    number_of_scan_results) + "\r\n如果需要查询结果请参考help中格式！")  # 艾特用户表示扫描完成科研查询了
        else:
            await session.send("呐呐呐！小哥哥域名不合规呐(｡・`ω´･)")



@Medusa.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text

    session.state['aims'] = stripped_arg#把内容复制到里面，可以再上面提取aims参数就行



async def MedusaScan(url: str,token: str) -> str:
    ThreadPool =ClassCongregation.ThreadPool()#定义一个线程池
    Values=ClassCongregation.AgentHeader().result("None")
    BotScan(ThreadPool,url,Values,token)
    ThreadPool.Start(30)  # 启动多线程
    number_of_scan_results=ClassCongregation.BotNumberOfLoopholes()#输出个数
    return number_of_scan_results

def BotScan(ThreadPool,url, Values, token):
    Struts2.Main(ThreadPool, url, Values, token,None)  # 调用Struts2主函数
    ConfluenceMain.Main(ThreadPool, url, Values, token,None)  # 调用 Confluence主函数
    NginxMain.Main(ThreadPool, url, Values, token,None)  # 调用Nginx主函数
    ApacheMain.Main(ThreadPool, url, Values, token,None)  # 调用Apache主函数
    PHPStudy.Main(ThreadPool, url, Values, token,None) # 调用Php主函数
    CmsMain.Main(ThreadPool, url, Values, token,None)  # 调用Cms主函数
    OaMian.Main(ThreadPool, url, Values, token,None) # 调用OA主函数
    JenkinsMain.Main(ThreadPool, url, Values, token,None)  # 调用Jenkins主函数
    Harbor.Main(ThreadPool, url, Values, token,None) # 调用Harbor主函数
    RailsMain.Main(ThreadPool, url, Values, token,None) # 调用RailsMain主函数
    KibanaMain.Main(ThreadPool, url, Values, token,None)  # 调用KibanaMain主函数
    CitrixMain.Main(ThreadPool, url, Values, token,None)  # 调用CitrixMain主函数
    MongoMain.Main(ThreadPool, url, Values, token,None) # 调用MongoMain主函数
    SpringMain.Main(ThreadPool, url, Values, token,None)  # 调用SpringMain主函数
    FastJson.Main(ThreadPool, url, Values, token,None)  # 调用FastJson主函数
    Windows.Main(ThreadPool, url, Values, token,None)  # 调用Windwos主函数

