import os
import time
import sys
class WriteFile:#写入文件类
    def __init__(self,FileName):
        if FileName == None:
            self.FileName = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期作为文件
        else:
            self.FileName = FileName


    def Write(self,Medusa):
        global FileNames
        if sys.platform == "win32" or sys.platform == "cygwin":
            FileNames = os.path.split(os.path.realpath(__file__))[0]+"\\ScanResult\\"+self.FileName + ".txt"#不需要输入后缀，只要名字就好
        elif sys.platform=="linux" or sys.platform=="darwin":
            FileNames = os.path.split(os.path.realpath(__file__))[0] + "/ScanResult/" + self.FileName + ".txt"  # 不需要输入后缀，只要名字就好
        with open(FileNames, 'w+',encoding='utf-8') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(Medusa+"\n")

WriteFile("1111").Write("dsadasdadasd")