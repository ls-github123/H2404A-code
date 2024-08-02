from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from . import models
import json
# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')
    
# 写一个类视图展示数据
class User(View):
    def get(self, request):
        # 拿到所有数据，转换为json返回
        users = models.Member.objects.all().values()
        userlist = json.dumps(list(users))
        # 通过json dumps将列表转换为json[{},{}]
        return JsonResponse({'status':200, 'data':userlist})
    
    
def show(request):
    return render(request, 'test_ajax.html')

class Member(View):
    def get(self, request):
        #通过all方法拿到的所有数据返回的是queryset 
        # json序列化只能是list list函数只能处理字典 不能处理queryset
        user = models.Member.objects.all().values()
        # values方法是将queryset转换为字典
        # JsonResponse({})自动将{}里的数据序列化
        print(user)
        return JsonResponse({'msg':'success','data':list(user)})
    
# 删除接口
class DelUser(View):
    def get(self, request):
        # 获取前端传递的id
        id = request.GET.get('id')
        # 执行删除
        res = models.Member.objects.filter(id=id).delete()
        if res:
            return JsonResponse({'mas':'删除成功','code':200})
        else:
            return JsonResponse({'msg':'删除失败','code':400})