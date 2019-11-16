from django.http import HttpResponse
from django.http import JsonResponse
def hello(request):
    return HttpResponse("Hello world ! ")

def api(request):
    return JsonResponse({"result": 0, "msg": "执行成功"})

def get(request):
    id = request.GET.get("id")
    pid = request.GET.get("pid")
    return HttpResponse("获得数据 %s %s"%(id,pid))
def test(request):
    print("the POST method")
    concat = request.POST.get("id")
    postBody = request.body
    print(concat)
    print(type(postBody))
    print(postBody)
    return JsonResponse({"result": 0, "msg": "执行成功"})