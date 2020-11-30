from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,GetPortableExecuteFilePath
import time
from config import portable_execute_file_size
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import pefile
def StructureExtraction(request):  # 用于提取保存文件后调用相应的处理函数
    RequestLogRecord(request, request_api="portable_execute_structure_analysis")
    if request.method == "POST":
        try:
            Token =request.headers["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="portable_execute_structure_analysis", uid=Uid)  # 查询到了在计入
                PictureData = request.FILES.get('file', None)  # 获取文件数据
                if 0>=PictureData.size:#判断是不是空文件
                    return JsonResponse({'message': "宝贝数据这么小的嘛？", 'code': 400, })
                elif portable_execute_file_size < PictureData.size:  #和配置文件中做对比
                    SaveFileName = randoms().result(10) + str(int(time.time()))   # 重命名文件
                    SaveRoute = GetPortableExecuteFilePath().Result() + SaveFileName  # 获得保存路径
                    with open(SaveRoute, 'wb') as f:
                        for line in PictureData:
                            f.write(line)
                    #接下来调用处理函数，接着再调用删除函数
                    return JsonResponse({'message': "成功了", 'code': 200, })
                else:
                    return JsonResponse({'message': "文件太大啦~(๑•̀ㅂ•́)و✧", 'code': 501, })
            else:
                return JsonResponse({'message': "小宝贝这是非法查询哦(๑•̀ㅂ•́)و✧", 'code': 403, })
        except Exception as e:
            ErrorLog().Write("Web_ToolsUtility_AntivirusSoftware_Compared(def)", e)
    else:
        return JsonResponse({'message': '请使用Post请求', 'code': 500, })


def WindowsPortableExecute(Path):
    try:
        PE = pefile.PE(Path)
        IMAGE_DOS_HEADER=[]#存放DOS头数据
        IMAGE_NT_HEADERS = {} # 存放NT头数据
        IMAGE_FILE_HEADER=[]#存放NT头某个字段数据
        IMAGE_OPTIONAL_HEADER=[]#存放NT头某个字段数据
        IMAGE_SECTION_HEADER=[]#存放节表数据
        IMAGE_IMPORT_DESCRIPTOR=[]#存放导入表数据
        IMAGE_EXPORT_DIRECTORY=[]#存放导出表数据
        _IMAGE_DOS_HEADER=str(PE.DOS_HEADER)#DOS头
        _IMAGE_NT_HEADERS=PE.NT_HEADERS#NT头
        _IMAGE_FILE_HEADER=str(PE.FILE_HEADER)#NT头中的_IMAGE_FILE_HEADER
        _IMAGE_OPTIONAL_HEADER=str(PE.OPTIONAL_HEADER)#nt里面的IMAGE_OPTIONAL_HEADER
        _IMAGE_SECTION_HEADER = PE.sections # 节表
        try:
            _IMAGE_IMPORT_DESCRIPTOR=PE.DIRECTORY_ENTRY_IMPORT#导入表
        except Exception as e:
            ErrorLog().Write("Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(def)-DIRECTORY_ENTRY_IMPORT", e)
            _IMAGE_IMPORT_DESCRIPTOR=None
        try:
            _IMAGE_EXPORT_DIRECTORY = PE.DIRECTORY_ENTRY_EXPORT  # 导出表
        except Exception as e:
            ErrorLog().Write("Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(def)-DIRECTORY_ENTRY_EXPORT", e)
            _IMAGE_EXPORT_DIRECTORY=None
        for i in _IMAGE_DOS_HEADER.splitlines()[1:]:#对dos头进行清洗
            IMAGE_DOS_HEADER.append(i.strip('\n'))
        for i in _IMAGE_FILE_HEADER.splitlines()[1:]:#对FILE头进行清洗
            IMAGE_FILE_HEADER.append(i.strip('\n'))
        for i in _IMAGE_OPTIONAL_HEADER.splitlines()[1:]:#对OPTIONAL头进行清洗
            IMAGE_OPTIONAL_HEADER.append(i.strip('\n'))
        #把清洗后数据放入字典中

        IMAGE_NT_HEADERS["Signature"] = hex(_IMAGE_NT_HEADERS.Signature)
        IMAGE_NT_HEADERS["IMAGE_FILE_HEADER"] = IMAGE_FILE_HEADER
        IMAGE_NT_HEADERS["IMAGE_OPTIONAL_HEADER"]=IMAGE_OPTIONAL_HEADER

        for i in _IMAGE_SECTION_HEADER:#对节表数据进行处理
            try:
                IMAGE_SECTION_HEADER_TMP={}#存放单个节表的临时容器
                IMAGE_SECTION_HEADER_TMP["Name"]=i.Name.decode('utf-8')#节名
                IMAGE_SECTION_HEADER_TMP["VirtualAddress"]=hex(i.VirtualAddress)#虚拟地址(RVA)
                IMAGE_SECTION_HEADER_TMP["VirtualSize"]=hex(i.Misc_VirtualSize)#虚拟大小
                IMAGE_SECTION_HEADER_TMP["PhysicalAddress"]=hex(i.PointerToRawData)#物理地址
                IMAGE_SECTION_HEADER_TMP["PhysicalSize"]=hex(i.SizeOfRawData)#物理大小
                IMAGE_SECTION_HEADER.append(IMAGE_SECTION_HEADER_TMP)
            except Exception as e:
                ErrorLog().Write("Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(def)-FOR-IMAGE_SECTION_HEADER",e)


        for ENTRY_IMPORT in _IMAGE_IMPORT_DESCRIPTOR:#对导入表信息进行提取
            try:
                IMAGE_IMPORT_DESCRIPTOR_TMP={}#存放临时导入表信息
                IMAGE_IMPORT_DESCRIPTOR_TMP["DynamicLinkLibraryName"]=ENTRY_IMPORT.dll.decode('utf-8')#DLL名字
                FunctionAndAddress=[]#存放函数和地址的列表
                for i in ENTRY_IMPORT.imports:
                    TMP = []#存放处理后相关数据
                    TMP.append(hex(i.address))#函数地址
                    TMP.append(i.name.decode('utf-8')) # 函数名
                    FunctionAndAddress.append(TMP)
                IMAGE_IMPORT_DESCRIPTOR_TMP["data"]=FunctionAndAddress#发送数据
                IMAGE_IMPORT_DESCRIPTOR.append(IMAGE_IMPORT_DESCRIPTOR_TMP)#把最终结果发到列表里面
            except Exception as e:
                ErrorLog().Write("Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(def)-FOR-IMAGE_IMPORT_DESCRIPTOR",e)

        for i in _IMAGE_EXPORT_DIRECTORY.symbols:  # 对导入表信息进行提取
            try:
                TMP={}
                TMP["FunctionAddress"]=hex(i.address)#函数地址
                TMP["FunctionNumber"]=i.ordinal#函数序号
                TMP["Name"]=i.name.decode('utf-8')  # 函数名
                IMAGE_EXPORT_DIRECTORY.append(TMP)
            except Exception as e:
                ErrorLog().Write("Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(def)-FOR-IMAGE_EXPORT_DIRECTORY",e)

    except Exception as e:
        ErrorLog().Write("Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(def)", e)



#WindowsPortableExecute("/Users/ascotbe/Downloads/nbtscan-1.0.35.exe")
#WindowsPortableExecute("/Users/ascotbe/Downloads/04a584091f2a2f48a50c9513fb4f75187f9edf87106f3ab011ba502988d8e9cf.exe")
#WindowsPortableExecute("/Users/ascotbe/Downloads/twain_32.dll")