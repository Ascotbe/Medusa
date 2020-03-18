from MedusaScan import San
import ClassCongregation
import time
import hashlib
import tldextract
from nonebot import on_command, CommandSession,message
# on_command 装饰器将函数声明为一个命令处理器
@on_command('Medusa:',only_to_me=False)
async def Medusa(session: CommandSession):
    city = session.get('city', prompt='呐呐呐！对方的域名呐？')
    Url = city[7:]
    user_qq_id = session.self_id#获取用户QQ
    url_refining=tldextract.extract(Url)
    if url_refining.suffix!="" and url_refining.domain!="":#判断提炼出来的东西是否符合二级域名
        token = hashlib.md5(str(user_qq_id).encode("utf-8")).hexdigest()#获取对方QQ的MD5加密
        await session.send("您的Key:" + token + "\r\n您的目标:" + Url)
        medusa_scan_success=await MedusaScan(Url,token)
        if medusa_scan_success=="1":
            #message.MessageSegment.at(user_qq_id)
            await session.send(message.MessageSegment.at(user_qq_id))#艾特用户表示扫描完成科研查询了
    else:
        await session.send("")


@Medusa.args_parser
async def _(session: CommandSession):

    session.state[session.current_key] = session.current_arg_text


async def MedusaScan(Url: str,token: str) -> str:
    ThreadPool =ClassCongregation.ThreadPool()#定义一个线程池
    Values=ClassCongregation.AgentHeader().result("None")
    San(ThreadPool,Url,Values,token,Module=None)
    ThreadPool.Start(30)  # 启动多线程
    return "1"