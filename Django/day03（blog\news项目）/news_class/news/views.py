from .models import News
from django.http import JsonResponse
# Create your views here.

# 通过访问增加新闻视图
def add_news(request):
    for i in range(5):
        News.objects.create(
            title = f'News Title {i+1}',
            content = f'News Title {i+1}',
            views = i * 10,
            likes = i * 5
        )
    return JsonResponse({'message':'News added successfully'})


# 通过访问修改视图
def update_news(request):
    news = News.objects.get(id=1)
    news.title = 'Update News Title'
    news.save()
    return JsonResponse({'message':'News updated successfully'})

# 通过访问删除视图
def delete_news(request):
    news = News.objects.get(id=2)
    news.delete()
    return JsonResponse({'message':'News deleted successfully'})

# 访问查询视图
def query_news(request):
    news = News.objects.all().order_by('-id') # 以id值为降序返回
    result = [{'id':n.id, 'title':n.title,'content': n.content, 'views':n.views, 'likes':n.likes}for n in news]
    return JsonResponse(result, safe=False)

# 访问查询视图(查询阅读量大于100和点赞量大于50的新闻数据)
def query_news_filtered(request):
    news = News.objects.filter(views__gt=100,likes__gt=50)
    result = [{'id':n.id, 'title':n.title, 'views':n.views, 'likes':n.likes}for n in news]
    return JsonResponse(result,safe=False)