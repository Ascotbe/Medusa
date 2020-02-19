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