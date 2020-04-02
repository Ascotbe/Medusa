# !/usr/bin/python env
# -*- coding:utf-8 -*-
from nonebot import on_command, CommandSession
import requests
import random
import datetime
from config import WeatherKey
# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('Weather', aliases=('天气',),only_to_me=False)
async def weather(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    city = session.get('city', prompt='公子需要查询的城市是什么呢？')
    # 获取城市的天气预报
    weather_report = await get_weather_of_city(city)
    # 向用户发送天气预报
    await session.send(weather_report)


@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    session.state['city'] = stripped_arg  # 把内容复制到里面，可以再上面提取aims参数就行


async def get_weather_of_city(city: str) -> str:
    try:
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
        }
        url = 'https://free-api.heweather.com/s6/weather/now?location=' + city + '&key='+WeatherKey
        PMurl = 'https://free-api.heweather.com/s6/air/now?parameters&location=' + city + '&key='+WeatherKey
        # 设定超时时间，防止被网站认为是爬虫
        timeout = random.choice(range(80, 180))
        rep = requests.get(url, headers=header, timeout=timeout)
        pm = requests.get(PMurl, headers=header, timeout=timeout)

        result = ''
        temp = rep.json()
        temp = temp['HeWeather6'][0]
        update = temp['update']
        now = temp['now']
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        pm = pm.json()
        pm = pm['HeWeather6'][0]

        # 区分县级市和市  免费接口没办法查到县级市的天气

        if pm['status'] == 'permission denied':
            # 县级市
            resulta = city + '实时天气预报-' + '\n' + '更新时间：' + update['loc'] + '\n' + '          当前天气：' + now[
                'cond_txt'] + '\n' + '          当前温度：' + now['tmp'] + '°C' + '\n' + '          体感温度：' + now[
                          'fl'] + '°C' + '\n' + '          风向：' + now['wind_dir'] + ' ' + now['wind_sc'] + '级 ' + now[
                          'wind_spd'] + '公里/小时' + '\n' + '          相对湿度：' + now[
                          'hum'] + '%' + '\n' + '          降水量：' + now['pcpn'] + 'ml' + '\n' + '          能见度：' + now[
                          'vis'] + '公里' + '\n' + '          云量：' + now['cloud'] + '\n'
            result = resulta + '发送时间：' + nowTime + '\n'
        else:  # 非县级市
            airnow = pm['air_now_city']
            result = city + '实时天气预报-' + '\n' \
                     + '更新时间：' + update['loc'] + '\n' \
                     + '          当前天气：' + now['cond_txt'] + '\n' \
                     + '          当前温度：' + now['tmp'] + '°C' + '\n' \
                     + '          体感温度：' + now['fl'] + '°C' + '\n' \
                     + '          风向：' + now['wind_dir'] + ' ' + now['wind_sc'] + '级 ' + now[
                         'wind_spd'] + '公里/小时' + '\n' \
                     + '          相对湿度：' + now['hum'] + '%' + '\n' \
                     + '          降水量：' + now['pcpn'] + 'ml' + '\n' \
                     + '          能见度：' + now['vis'] + '公里' + '\n' \
                     + '          云量：' + now['cloud'] + '\n' \
                     + '-----------------------------------' + '\n' \
                     + '当前空气质量：' + '\n' \
                     + '          空气质量指数：' + airnow['aqi'] + '\n' \
                     + '          主要污染物：' + airnow['main'] + '\n' \
                     + '          空气质量：' + airnow['qlty'] + '\n' \
                     + '          二氧化氮指数：' + airnow['no2'] + '\n' \
                     + '          二氧化硫指数：' + airnow['so2'] + '\n' \
                     + '          一氧化碳指数：' + airnow['co'] + '\n' \
                     + '          pm10指数：' + airnow['pm10'] + '\n' \
                     + '          pm25指数：' + airnow['pm25'] + '\n' \
                     + '          臭氧指数：' + airnow['o3'] + '\n'

            result = result + '发送时间：' + nowTime + '\n'
    except:
        result="呐呐呐~小女子好像查不到公子查询的城市呢"
    return result