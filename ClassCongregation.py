from fake_useragent import UserAgent
class WriteFile:
    def Write(vul,FileName):
        FileNames = FileName + ".txt"
        with open(FileNames, 'a') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(vul+ "\n")
# class UserAgentS:
#
#     def DesignationAgent(Values):#用户指定头
#         ua = UserAgent()
#         return (ua.Values)
#     def RandomAgent():#随机头
#         ua = UserAgent()
#         return (ua.random)
# b=str("firefox")
# c=UserAgentS.RandomAgent()
# a=UserAgentS.DesignationAgent(b)
# print(a)
# print(c)