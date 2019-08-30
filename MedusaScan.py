from optparse import OptionParser
#import Weblogic.WeblogicMain
import Confluence.ConfluenceMain
import Struts2.Struts2Main
import Nginx.Nginx
import time
Version = '0.08'
banner='''
                   __  __          _                   ____                  
                  |  \/  | ___  __| |_   _ ___  __ _  / ___|  ___ __ _ _ __  
                  | |\/| |/ _ \/ _` | | | / __|/ _` | \___ \ / __/ _` | '_ \ 
                  | |  | |  __/ (_| | |_| \__ \ (_| |  ___) | (_| (_| | | | |
                  |_|  |_|\___|\__,_|\__,_|___/\__,_| |____/ \___\__,_|_| |_|
                                    
                                         By Ascotbe |  V {}

'''.format(Version)


parser = OptionParser()
'''
第一个参数表示option的缩写，以单个中划线引导，例如-f、-d，只能用单个字母，可以使用大写;
第二个参数表示option的全拼，以两个中划线引导，例如--file、--Opencv_version;
第一第二个参数可以单独使用，也可以同时使用，但必须保证有其中一个;
从第三个参数开始是命名参数，是可选参数，常用的几个：
type=: 表示输入命令行参数的值的类型，默认为string，可以指定为string, int, choice, float，complex其中一种;
default=: 表示命令参数的默认值；
metavar=: 显示到帮助文档中用来提示用户输入期望的命令参数；
dest=：指定参数在options对象中成员的名称，如果没有指定dest参数，将用命令行参数名来对options对象的值进行存取。
help=:  显示在帮助文档中的信息;
'''
parser.add_option('-t','--text',type=str,help='The file where the url is located,If you do not enter the location, the default is written to the root directory.',dest='filename')
parser.add_option('-u','--url',type=str,help="Target url",dest='url')
parser.add_option('-a','--agent',type=str,help="Specify a header file or use a random header",dest='agent')



#Port=options.port

def San(FileName,Url,Values):
    # try:
    #     Weblogic.WeblogicMain.Main(Url)#调用weblogic主函数
    # except:
    #     print("WeblogicSanExcept")
    try:
        Struts2.Struts2Main.Main(Url,FileName,Values)  # 调用Struts2主函数
    except:
        print("Struts2SanExcept")
    try:
        Confluence.ConfluenceMain.Main(Url,FileName,Values)# 调用 Confluence主函数
    except:
        print("ConfluenceExcept")
    try:
        Nginx.Nginx.Main(Url,FileName,Values)# 调用 Confluence主函数
    except:
        print("NginxExcept")

if __name__ == '__main__':
    print(banner)
    (options, args) = parser.parse_args()  # options里面存了所有的dest中的值

    FileName = options.filename
    Url = options.url
    Values=options.agent#判断是否使用随机头，判断写在Class里面

    try:
        San(FileName,Url,Values)
        print("Scan is complete, please see the result file")
    except KeyboardInterrupt as e:
        exit(0)




