from django.http import HttpResponse
def blog(request):
    print('调用字符串显示模块str')
    return HttpResponse('str-hello Django!')