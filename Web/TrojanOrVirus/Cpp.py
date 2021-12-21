from jinja2 import Template
from ClassCongregation import randoms,Binary,ShellCode
def Run(**kwargs):

    RawData = kwargs.get("yaml_raw_data") #获取yaml的原始数据
    Include = RawData.get('include')  # 插件依赖
    Function=RawData.get('function') #插件函数
    #上述是必须使用的参数
    Expression=RawData.get('set') #插件表达式，内涵执行函数，会造成命令执行漏洞（
    State=RawData.get('state') #获取声明值
    Define=RawData.get('define') #插件额外定义
    Class=RawData.get('class') #插件的类

    if Expression is not None:
        Placeholder = {}
        TreatedFunction = []
        TreatedClass = []
        for i in Expression:
            Tmp = Template(Expression[i])#进行模板替换表达式中的占位符
            Replace=Tmp.render(Placeholder)#尝试进行替换，如果没有的占位符的话，就继续下一部
            Placeholder[i] = eval(Replace)
        for x in Function:
            Tmp = Template(x)
            TreatedFunction.append(Tmp.render(Placeholder)) #处理占位符
        Function=TreatedFunction
        if Class is not None:
            for a in Class:
                Tmp = Template(a)
                TreatedClass.append(Tmp.render(Placeholder))  # 处理占位符
            Class= TreatedClass

    #函数拼接
    SourceCode =r""
    for xx in Define,Include,State,Class,Function:
        if xx is not None:
            for x in xx:
                SourceCode += x+"\n"

    return SourceCode


# import yaml
# import time
# YamlRawData = yaml.safe_load(open("/Users/ascotbe/code/Medusa/Web/TrojanOrVirus/Modules/1630944000-Go-EXE-Windows-Null-Yes-Syscall.yaml")) # 读取yaml文件
#
# A=Run(yaml_raw_data = YamlRawData,shellcode="\\x75\\x33") # 读取yaml文件)
# time.sleep(1)