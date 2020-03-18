import ClassCongregation
import time
import hashlib
import tldextract
from nonebot import on_command, CommandSession,message
# on_command 装饰器将函数声明为一个命令处理器
@on_command('results:',only_to_me=False)
async def results(session: CommandSession):
    city = session.get('city', prompt='呐呐呐！Key和目标呐？')
    user_qq_id = session.self_id#获取用户QQ
    token = hashlib.md5(str(user_qq_id).encode("utf-8")).hexdigest()#获取对方QQ的MD5加密

    results_inquire_token,results_inquire_url= await message_processing(city)#处理后的token和url
    if token==results_inquire_token:
        results_inquire()#消息都正确后进行查询

        await session.send(message.MessageSegment.at(user_qq_id))#艾特用户表示发送结果
    else:
        await session.send("")#查询不到结果


#对函数进行处理提出去URL和用户token
async def message_processing(city: str) -> str:
    pass


#对目标进行查询是否有结果
async def results_inquire():
    pass
