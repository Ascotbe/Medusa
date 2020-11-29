from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog
import json
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import pefile

def WindowsPortableExecute(Path):
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
    _IMAGE_IMPORT_DESCRIPTOR=PE.DIRECTORY_ENTRY_IMPORT#导入表
    _IMAGE_EXPORT_DIRECTORY = PE.DIRECTORY_ENTRY_EXPORT  # 导出表
    #str(PE.RICH_HEADER)
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
        IMAGE_SECTION_HEADER_TMP={}#存放单个节表的临时容器
        IMAGE_SECTION_HEADER_TMP["Name"]=i.Name.decode('utf-8')#节名
        IMAGE_SECTION_HEADER_TMP["VirtualAddress"]=hex(i.VirtualAddress)#虚拟地址(RVA)
        IMAGE_SECTION_HEADER_TMP["VirtualSize"]=hex(i.Misc_VirtualSize)#虚拟大小
        IMAGE_SECTION_HEADER_TMP["PhysicalAddress"]=hex(i.PointerToRawData)#物理地址
        IMAGE_SECTION_HEADER_TMP["PhysicalSize"]=hex(i.SizeOfRawData)#物理大小
        IMAGE_SECTION_HEADER.append(IMAGE_SECTION_HEADER_TMP)


    for ENTRY_IMPORT in _IMAGE_IMPORT_DESCRIPTOR:#对导入表信息进行提取
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

    for i in _IMAGE_EXPORT_DIRECTORY.symbols:  # 对导入表信息进行提取
        TMP={}
        TMP["FunctionAddress"]=hex(i.address)#函数地址
        TMP["FunctionNumber"]=i.ordinal#函数序号
        TMP["Name"]=i.name.decode('utf-8')  # 函数名
        IMAGE_EXPORT_DIRECTORY.append(TMP)



#WindowsPortableExecute("/Users/ascotbe/Downloads/nbtscan-1.0.35.exe")
#WindowsPortableExecute("/Users/ascotbe/Downloads/04a584091f2a2f48a50c9513fb4f75187f9edf87106f3ab011ba502988d8e9cf.exe")
WindowsPortableExecute("/Users/ascotbe/Downloads/twain_32.dll")