from ClassCongregation import BotVulnerabilityInquire
import hashlib
import base64
from nonebot import on_command, CommandSession,message
import re
# on_command 装饰器将函数声明为一个命令处理器
@on_command('查询个数')
async def ResultsNumber(session: CommandSession):
    message_txt = session.get('MessageTxt', prompt='呐呐呐！Key和Token呐？')
    message_txt_token,message_txt_key=message_txt_re(message_txt)#调用正则进行匹配,返回token和key
    user_qq_id = session.ctx['user_id']  # 获取用户QQ
    encrypted_string = str(user_qq_id) + str(message_txt_key.strip())  # 对两个参数进行合并
    token = hashlib.md5(str(encrypted_string).encode("utf-8")).hexdigest()  # 对encrypted_string进行加密
    if token==message_txt_token.strip():#对输入的信息进行加密看看是否本用户使用
        number=BotVulnerabilityInquire(token).Number()
        await session.send(message.MessageSegment.at(user_qq_id)+"查询到漏洞个数："+str(number))#艾特用户表示发送结果
    else:
        await session.send(message.MessageSegment.at(user_qq_id) + "未查到结果")  # 查询不到结果

@on_command('查询')
async def ResultsContent(session: CommandSession):
    message_txt = session.get('MessageTxt', prompt='呐呐呐！Key和Token呐？')
    message_txt_token,message_txt_key=message_txt_re(message_txt)#调用正则进行匹配,返回token和key
    user_qq_id = session.ctx['user_id']  # 获取用户QQ
    encrypted_string = str(user_qq_id) + str(message_txt_key.strip())  # 对两个参数进行合并
    token = hashlib.md5(str(encrypted_string).encode("utf-8")).hexdigest()  # 对encrypted_string进行加密
    if token==message_txt_token.strip():#对输入的信息进行加密看看是否本用户使用
        database_query_results=BotVulnerabilityInquire(token).Inquire()
        if len(database_query_results)!=0:
            await session.send(message.MessageSegment.at(user_qq_id)+JsonProcessing(database_query_results))#艾特用户表示发送结果
        else:
            await session.send(message.MessageSegment.at(user_qq_id)+"未查到结果")#查询不到结果

#对函数进行处理提出去URL和用户token
@ResultsNumber.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text
    session.state['MessageTxt'] = stripped_arg#把内容复制到里面，可以再上面提取aims参数就行

#对函数进行处理提出去URL和用户token
@ResultsContent.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text
    session.state['MessageTxt'] = stripped_arg#把内容复制到里面，可以再上面提取aims参数就行

#对目标进行查询是否有结果
def JsonProcessing(database_query_results):#对返回的json进行处理
    database_query_results_processing=""

    for i in database_query_results:
        b64=base64.b64decode(i["details"])
        if len(b64)>100:
            details="由于内容过长不予展示"
        else:
            details=str(b64)
        processing="目标："+i["url"]+"\r\n"+"漏洞名称："+i["name"]+"\r\n"+"返回内容："+details+"\r\n"
        database_query_results_processing+= processing
    return database_query_results_processing

def message_txt_re(txt):
    message_txt_token= re.search(r'Token:([\w\u4e00-\u9fa5!@#$%^*()&-=+_`~/?.,<>\\|\[\]{}]*)',txt).group(1)
    message_txt_key= re.search(r'Key:([\w\u4e00-\u9fa5!@#$%^*()&-=+_`~/?.,<>\\|\[\]{}]*)',txt).group(1)
    return message_txt_token,message_txt_key