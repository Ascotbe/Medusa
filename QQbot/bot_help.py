from nonebot import on_command, CommandSession,message

help_list = """
[CQ:emoji,id=127773][CQ:emoji,id=127773][CQ:emoji,id=127773][CQ:emoji,id=127773][CQ:emoji,id=127773][CQ:emoji,id=127773][CQ:emoji,id=127773][CQ:emoji,id=127773][CQ:emoji,id=127773][CQ:emoji,id=127773]
扫描之前请遵守国家法律，任何未授权的扫描都会记录到数据库
1.天气查询 城市
[CQ:emoji,id=9757]天气 北京
2.漏洞扫描
[CQ:emoji,id=9757]@me 扫描 域名    
3.漏洞查询
[CQ:emoji,id=9757]@me 查询
Token:XXXXXXXXXXXXXXX\r\nKey:XXXXXXXXX
4.漏洞个数查询
[CQ:emoji,id=9757]@me 查询个数 
Token:XXXXXXXXXXXXXXX\r\nKey:XXXXXXXXXX
"""




@on_command('help')
async def BotHelp(session: CommandSession):
    user_qq_id = session.event['user_id']#获取用户QQ
    await session.send(message.MessageSegment.at(user_qq_id) + help_list)

