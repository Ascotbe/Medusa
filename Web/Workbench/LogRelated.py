from Web.WebClassCongregation import RequestLog,UserOperationLog
import base64
def GetIp(request):
    '''获取请求者的IP信息'''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP
    return ip

def UserOperationLogRecord(request,**kwargs):#用户操作写入SDK
    RequestApi = kwargs.get("request_api")
    Uid = kwargs.get("uid")
    Headers=base64.b64encode(str(request.headers).encode(encoding="utf-8"))
    PostDate=base64.b64encode(str(request.body).encode(encoding="utf-8"))
    UserOperationLog().Write(uid=Uid,request_ip=GetIp(request),request_url=request.get_full_path(),request_api=RequestApi,header=Headers,request_method=request.method,post_date=PostDate)

def RequestLogRecord(request,**kwargs):#操作写入SDK
    RequestApi = kwargs.get("request_api")
    Headers=base64.b64encode(str(request.headers).encode(encoding="utf-8"))
    PostDate=base64.b64encode(str(request.body).encode(encoding="utf-8"))
    RequestLog().Write(request_ip=GetIp(request),request_url=request.get_full_path(),request_api=RequestApi,header=Headers,request_method=request.method,post_date=PostDate)