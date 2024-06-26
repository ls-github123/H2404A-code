from django.shortcuts import render

# Create your views here.
def index(request):
    # 定义一个字典数据
    data = {
        'title':'welcome to the News Portal',
        'description':'Here you can find the latest news',
        'author':'Admin'
    }
    
    # 定义一个列表数据
    news_list = [
        'News Item 1',
        'News Item 2',
        'News Item 3'
    ]
    
    context = {
        'data':data,
        'news_list':news_list
    }
    
    return render(request, 'news/index.html', context)

def login(request):
    return render(request, 'news/login.html')