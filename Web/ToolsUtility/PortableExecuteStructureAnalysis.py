from Web.WebClassCongregation import UserInfo
from django.http import JsonResponse
from ClassCongregation import ErrorLog,randoms,GetPortableExecuteFilePath
import time
from config import portable_execute_file_size
from Web.Workbench.LogRelated import UserOperationLogRecord,RequestLogRecord
import pefile
from cryptography import x509
from cryptography.hazmat.backends import default_backend
import re
import magic
import os
import hashlib
from asn1crypto import cms

def Windows(request):  # 用于提取保存文件后调用相应的处理函数
    RequestLogRecord(request, request_api="windows_portable_execute_structure_analysis")
    if request.method == "POST":
        try:
            Token =request.headers["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="windows_portable_execute_structure_analysis", uid=Uid)  # 查询到了在计入
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

def Linux(request):  # 用于提取保存文件后调用相应的处理函数
    RequestLogRecord(request, request_api="linux_portable_execute_structure_analysis")
    if request.method == "POST":
        try:
            Token =request.headers["token"]
            Uid = UserInfo().QueryUidWithToken(Token)  # 如果登录成功后就来查询UID
            if Uid != None:  # 查到了UID
                UserOperationLogRecord(request, request_api="linux_portable_execute_structure_analysis", uid=Uid)  # 查询到了在计入
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

class WindowsPortableExecute:
    def __init__(self):
        self.IMAGE_DOS_HEADER = []  # 存放DOS头数据
        self.IMAGE_NT_HEADERS = {}  # 存放NT头数据
        self.IMAGE_FILE_HEADER = []  # 存放NT头某个字段数据
        self.IMAGE_OPTIONAL_HEADER = []  # 存放NT头某个字段数据
        self.IMAGE_SECTION_HEADER = []  # 存放节表数据
        self.IMAGE_IMPORT_DESCRIPTOR = []  # 存放导入表数据
        self.IMAGE_EXPORT_DIRECTORY = []  # 存放导出表数据
        self.CertificateDataContainer = []  # 存放证书数据容器
        self.IMAGE_RESOURCE_DIRECTORY=[]#存放资源数据
    def DOS(self):#dos头处理函数
        _IMAGE_DOS_HEADER = str(self.PE.DOS_HEADER)  # DOS头
        for i in _IMAGE_DOS_HEADER.splitlines()[1:]:  # 对dos头进行清洗
            self.IMAGE_DOS_HEADER.append(i.strip('\n'))
    def NT(self):
        _IMAGE_FILE_HEADER = str(self.PE.FILE_HEADER)  # NT头中的_IMAGE_FILE_HEADER
        _IMAGE_NT_HEADERS = self.PE.NT_HEADERS  # NT头
        _IMAGE_OPTIONAL_HEADER = str(self.PE.OPTIONAL_HEADER)  # nt里面的IMAGE_OPTIONAL_HEADER
        for i in _IMAGE_FILE_HEADER.splitlines()[1:]:  # 对FILE头进行清洗
            self.IMAGE_FILE_HEADER.append(i.strip('\n'))
        for i in _IMAGE_OPTIONAL_HEADER.splitlines()[1:]:  # 对OPTIONAL头进行清洗
            self.IMAGE_OPTIONAL_HEADER.append(i.strip('\n'))
            # 把清洗后数据放入字典中

        self.IMAGE_NT_HEADERS["Signature"] = hex(_IMAGE_NT_HEADERS.Signature)
        self.IMAGE_NT_HEADERS["IMAGE_FILE_HEADER"] = self.IMAGE_FILE_HEADER
        self.IMAGE_NT_HEADERS["IMAGE_OPTIONAL_HEADER"] = self.IMAGE_OPTIONAL_HEADER
    def SECTION(self):#对节表数据进行清洗

        _IMAGE_SECTION_HEADER = self.PE.sections  # 节表

        for i in _IMAGE_SECTION_HEADER:  # 对节表数据进行处理
            try:
                IMAGE_SECTION_HEADER_TMP = {}  # 存放单个节表的临时容器
                IMAGE_SECTION_HEADER_TMP["name"] = i.Name.decode('utf-8')  # 节名
                IMAGE_SECTION_HEADER_TMP["virtual_address"] = hex(i.VirtualAddress)  # 虚拟地址(RVA)
                IMAGE_SECTION_HEADER_TMP["virtual_size"] = hex(i.Misc_VirtualSize)  # 虚拟大小
                IMAGE_SECTION_HEADER_TMP["physical_address"] = hex(i.PointerToRawData)  # 物理地址
                IMAGE_SECTION_HEADER_TMP["physical_size"] = hex(i.SizeOfRawData)  # 物理大小
                self.IMAGE_SECTION_HEADER.append(IMAGE_SECTION_HEADER_TMP)
            except Exception as e:
                ErrorLog().Write(
                    "Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(class)_SECTION(def)",
                    e)
    def CA(self):#对证书进行处理
        try:  # 获取证书资源段
            CertificateListAddress = self.PE.OPTIONAL_HEADER.DATA_DIRECTORY[
                pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_SECURITY"]].VirtualAddress
            CertificateListSize = self.PE.OPTIONAL_HEADER.DATA_DIRECTORY[
                pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_SECURITY"]].Size
            with open(self.FilePath, 'rb') as f:  # 读取进程中证书的完整数据
                f.seek(CertificateListAddress)
                CertificateListRawData = f.read(CertificateListSize)

            CertificateList = cms.ContentInfo.load(CertificateListRawData[8:])

            for Certificate in CertificateList["content"]["certificates"]:
                try:
                    TMP = {}  # 存放临时数据的容器
                    ParsedCertificate = x509.load_der_x509_certificate(Certificate.dump(), default_backend())
                    TMP["valid_to"] = str(int(time.mktime(ParsedCertificate.not_valid_after.timetuple())))  # valid to#结束时间#需要处理成Unix的样式
                    TMP["valid_from"] = str(int(time.mktime(ParsedCertificate.not_valid_before.timetuple())))  # valid from#开始时间
                    TMP["version"] = ParsedCertificate.version.name  # 版本
                    TMP["algorithm"] = ParsedCertificate.signature_hash_algorithm.name  # algorithm #加密方式
                    TMP["serial_number"] = hex(ParsedCertificate.serial_number)  # serial number #需要转16禁止
                    # cert status 利用创建时间是否在证书区间来判断
                    TMP["thumbprint"] = Certificate.chosen.sha1_fingerprint  # thumbprint
                    try:  # 正则匹配问题
                        TMP["cert_issuer"] = re.findall(r'CN=(.*?)\)', str(ParsedCertificate.subject.rdns), re.I)[
                            0]  # cert issuer
                    except:
                        TMP["cert_issuer"] = None
                    self.CertificateDataContainer.append(TMP)  # 存放证书数据
                    print(TMP)
                except:
                    pass
        except Exception as e:
            ErrorLog().Write(
                "Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(class)_CA(def)", e)
    def IMPORT(self):#对导入表进行处理
        try:
            _IMAGE_IMPORT_DESCRIPTOR = self.PE.DIRECTORY_ENTRY_IMPORT  # 导入表

            for ENTRY_IMPORT in _IMAGE_IMPORT_DESCRIPTOR:  # 对导入表信息进行提取
                try:
                    IMAGE_IMPORT_DESCRIPTOR_TMP = {}  # 存放临时导入表信息
                    IMAGE_IMPORT_DESCRIPTOR_TMP["dynamic_link_library_name"] = ENTRY_IMPORT.dll.decode('utf-8')  # DLL名字
                    FunctionAndAddress = []  # 存放函数和地址的列表
                    for i in ENTRY_IMPORT.imports:
                        TMP = []  # 存放处理后相关数据
                        TMP.append(hex(i.address))  # 函数地址
                        TMP.append(i.name.decode('utf-8'))  # 函数名
                        FunctionAndAddress.append(TMP)
                    IMAGE_IMPORT_DESCRIPTOR_TMP["data"] = FunctionAndAddress  # 发送数据
                    self.IMAGE_IMPORT_DESCRIPTOR.append(IMAGE_IMPORT_DESCRIPTOR_TMP)  # 把最终结果发到列表里面
                except:
                    pass
        except Exception as e:
            ErrorLog().Write(
                "Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(class)_IMPORT(def)",
                e)

    def EXPORT(self):#对导出表数据进行处理
        try:
            _IMAGE_EXPORT_DIRECTORY = self.PE.DIRECTORY_ENTRY_EXPORT  # 导出表

            for i in _IMAGE_EXPORT_DIRECTORY.symbols:  # 对导出表信息进行提取
                try:
                    TMP = {}
                    TMP["function_address"] = hex(i.address)  # 函数地址
                    TMP["function_number"] = i.ordinal  # 函数序号
                    TMP["name"] = i.name.decode('utf-8')  # 函数名
                    self.IMAGE_EXPORT_DIRECTORY.append(TMP)
                except:
                    pass
        except Exception as e:
            ErrorLog().Write(
                    "Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(class)-EXPORT(def)",
                    e)

    def RESOURCE(self):#对资源文件进行处理
        try:
            _IMAGE_RESOURCE_DIRECTORY=self.PE.DIRECTORY_ENTRY_RESOURCE#资源文件
            for ResourceOne in _IMAGE_RESOURCE_DIRECTORY.entries:  # 根据数据资源来判断循环几次
                try:
                    TMP = {}  # 临时存储数据
                    TMP["resource_type"] = str(ResourceOne.id) # 资源类型
                    """资源类型表
                    0x00000001	鼠标指针（Cursor）	   0x00000008	字体（Font）
                    0x00000002	位图（Bitmap）	       0x00000009	快捷键（Accelerators）
                    0x00000003	图标（Icon）	           0x0000000A	非格式化资源（Unformatted）
                    0x00000004	菜单（Menu）	           0x0000000B	消息列表（Message Table）
                    0x00000005	对话框（Dialog）	       0x0000000C	鼠标指针组（Group Cursor）
                    0x00000006	字符串列表（String Table）0x0000000E	图标组（Group Icon）
                    0x00000007	字体目录（Font Directory）0x00000010	版本信息（Version Information）
                    """
                    for ResourceTwo in ResourceOne.directory.entries:
                        try:
                            TMP["resource_name"] = str(ResourceTwo.id)  # 资源名
                            for ResourceThree in ResourceTwo.directory.entries:
                                try:
                                    #资源语言对照表
                                    #https://www.science.co.il/language/Locale-codes.php
                                    TMP["resource_language"] = str(ResourceThree.id)  # 资源语言
                                    TMP["offset_to_data"] = str(hex(ResourceThree.data.struct.OffsetToData))  # 偏移地址
                                    TMP["size"] = str(hex(ResourceThree.data.struct.Size))  # 资源大小
                                    TMP["code_page"] = str(ResourceThree.data.struct.CodePage)  # 代码页，暂时不需要
                                    # TMP["reserved"]=ResourceThree.data.struct.Reserved#保留字段
                                    TMP["resource_sublanguage"] = str(ResourceThree.data.sublang)  # 资源子语言
                                except Exception as e:
                                    ErrorLog().Write(
                                        "Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(class)_RESOURCE(def)_ResourceThree",
                                        e)
                        except Exception as e:
                            ErrorLog().Write(
                                "Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(class)_RESOURCE(def)_ResourceTwo",
                                e)
                    self.IMAGE_RESOURCE_DIRECTORY.append(TMP)  # 发送数据到容器中
                except Exception as e:
                    ErrorLog().Write(
                        "Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(class)_RESOURCE(def)_ResourceOne",
                        e)
        except Exception as e:
            ErrorLog().Write(
                "Web_ToolsUtility_PortableExecuteStructureAnalysis_WindowsPortableExecute(class)_RESOURCE(def)",
                e)
    def Run(self,**kwargs):
        self.FilePath = kwargs.get("path")  # 传入的文件路径
        self.PE = pefile.PE(self.FilePath)  # 获取路径
        self.MIME = magic.from_file(self.FilePath)  #获取文件MIME类型
        self.FileSize =os.path.getsize(self.FilePath) # 传入的文件大小
        self.FileRawDataStream=open(self.FilePath, "rb").read()#获取文件原始数据流
        self.MD5=hashlib.md5(self.FileRawDataStream).hexdigest()#文件的MD5加密
        self.SHA1=hashlib.sha1(self.FileRawDataStream).hexdigest()#文件的sha1加密
        self.SHA256=hashlib.sha256(self.FileRawDataStream).hexdigest()#文件的sha256加密
        self.RESOURCE()
        self.EXPORT()
        self.IMPORT()
        self.CA()
        self.SECTION()
        self.NT()
        self.DOS()


