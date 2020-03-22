from nonebot import on_command, CommandSession,message

help_list = """
1.天气查询 城市
天气 北京
2.漏洞扫描
@me扫描 域名    
3.漏洞查询
@me查询 (需要使用\\r\\n也就是需要对两个值分成两行)
Token:XXXXXXXXXXXXXXX\r\nKey:XXXXXXXXX
4.漏洞个数查询(需要使用\\r\\n也就是需要对两个值分成两行)
@me查询个数 
Token:XXXXXXXXXXXXXXX\r\nKey:XXXXXXXXXX
"""


@on_command('help')
async def BotHelp(session: CommandSession):
    user_qq_id = session.ctx['user_id']#获取用户QQ
    await session.send(message.MessageSegment.at(user_qq_id) + help_list)
