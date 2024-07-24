from django.shortcuts import render
from . import models
# Create your views here.

def newslist(request):
    data = models.NewsItem.objects.all()
    return render(request, 'newslist.html', locals())