import requests
import re


class Proxies:
    def __init__(self):
        self.proxy_list = []
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/45.0.2454.101 Safari/537.36",
            'Accept-Encoding': 'gzip, deflate, sdch',
        }

    # 爬取西刺代理的国内高匿代理
    def get_proxy_nn(self):
        proxy_list = []
        res = requests.get("http://www.xicidaili.com/nn", headers=self.headers)
        ip_list = re.findall('<td>(\d+\.\d+\.\d+\.\d+)</td>', res.text)
        port_list = re.findall('<td>(\d+)</td>', res.text)
        for ip, port in zip(ip_list, port_list):
            proxy_list.append(ip + ":" + port)
        return proxy_list

    # 验证代理是否能用
    def verify_proxy(self, proxy_list):
        for proxy in proxy_list:
            proxies = {
                "http": proxy
            }
            try:
                if requests.get('http://www.baidu.com', proxies=proxies, timeout=2).status_code == 200:
                    print('success %s' % proxy)
                    if proxy not in self.proxy_list:
                        self.proxy_list.append(proxy)
            except:
                print('fail %s' % proxy)

    # 保存到proxies.txt里
    def save_proxy(self):
        # 验证代理池中的IP是否可用
        print("开始清洗代理池...")
        with open("proxies.txt", 'a', encoding="utf-8") as f:
            txt = f.read()
        # 判断代理池是否为空
        if txt != '':
            self.verify_proxy(txt.strip().split('\n'))
        else:
            print("代理池为空！\n")
        print("开始存入代理池...")
        # 把可用的代理添加到代理池中
        with open("proxies.txt", 'a', encoding="utf-8") as f:
            for proxy in self.proxy_list:
                f.write(proxy + "\n")


if __name__ == '__main__':
    p = Proxies()
    results = p.get_proxy_nn()
    print("爬取到的代理数量", len(results))
    print("开始验证：")
    p.verify_proxy(results)
    print("验证完毕：")
    print("可用代理数量：", len(p.proxy_list))
    p.save_proxy()

