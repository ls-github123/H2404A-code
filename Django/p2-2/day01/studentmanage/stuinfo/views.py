from django.shortcuts import render
from . import models

# Create your views here.
def list(request):
    data = models.StudentInfo.objects.all()
    return render(request, 'list.html', locals())