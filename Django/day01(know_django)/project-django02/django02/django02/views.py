from django.http import HttpResponse
from django.shortcuts import render
def books(request):
    print('当前Books函数被调用')
    return HttpResponse('你好Django!')

def title(request):
    print('title函数已调用')
    return HttpResponse('title页面展示!')

def shop(request):
    print('shop模块已调用')
    return HttpResponse('shop模块展示')

def cdn(request):
    print('cdn模块已调用')
    return HttpResponse('cdn模块展示')

def book(request):
    return render(request, 'book.html')

def index1(request):
    return render(request, 'index1.html')