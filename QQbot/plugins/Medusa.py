from MedusaScan import San
import ClassCongregation
from nonebot import on_command, CommandSession
# on_command 装饰器将函数声明为一个命令处理器
@on_command('Medusa', aliases=('扫描域名'))
async def Medusa(session: CommandSession):
    city = session.get('city', prompt='公子需要查询的城市是什么呢？')
    weather_report = await MedusaScan(city)
    await session.send(weather_report)

@Medusa.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('公子需要查询的城市是什么呢？')
    session.state[session.current_key] = stripped_arg


async def MedusaScan(city: str) -> str:
    Url=city
    #设置一个时间搓这样可以直接用时间搓查
    ThreadPool =ClassCongregation.ThreadPool()#定义一个线程池
    Values=ClassCongregation.AgentHeader().result("None")
    San(ThreadPool,Url,Values,ProxyIp=None,Module=None)
    return ""