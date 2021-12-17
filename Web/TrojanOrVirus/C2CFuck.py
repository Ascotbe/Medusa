from jinja2 import Template
from ClassCongregation import randoms

def Run(**kwargs):

    RawData = kwargs.get("yaml_raw_data") #获取yaml的原始数据
    Include = RawData.get('include')  # 插件依赖
    Function=RawData.get('function') #插件函数
    #上述是必须使用的参数
    Expression=RawData.get('set') #插件表达式，内涵执行函数，会造成命令执行漏洞（
    Pragma=RawData.get('pragma') #编译额外参数
    Define=RawData.get('define') #插件额外定义
    Class=RawData.get('class') #插件的类

    if Expression is not None:
        Placeholder = {}
        TreatedFunction = []
        TreatedClass = []
        for i in Expression:
            Placeholder[i] = eval(Expression[i])
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
    for xx in Define,Include,Pragma,Class,Function:
        if xx is not None:
            for x in xx:
                SourceCode += x+"\n"

    return SourceCode



