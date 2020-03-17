from MedusaScan import San
import ClassCongregation
import time
import hashlib
import tldextract
from nonebot import on_command, CommandSession
# on_command 装饰器将函数声明为一个命令处理器
@on_command('Medusa:',only_to_me=False)
async def Medusa(session: CommandSession):
    city = session.get('city', prompt='呐呐呐！对方的域名呐？')
    Url = city[7:]
    url_refining=tldextract.extract(Url)
    if url_refining.suffix!="" and url_refining.domain!="":#判断提炼出来的东西是否符合二级域名
        token = hashlib.md5(str(int(time.time())).encode("utf-8")).hexdigest()#获取MD5加密
        await session.send("您的Key:" + token + "\r\n您的目标:" + Url)
        await MedusaScan(Url,token)
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
    return ""