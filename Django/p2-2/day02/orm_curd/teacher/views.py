from django.shortcuts import render, HttpResponseRedirect
from . import models
# Create your views here.
def show(request):
    if 'select' in request.GET or 'sex' in request.GET:
        select = request.GET['select']
        sex = request.GET['sex']
        data = models.TeachersInfo.objects.filter(name__contains=select, gender=sex)
        print(data)
    else:
        data = models.TeachersInfo.objects.all()
    return render(request, 'teacher/list.html', {'data':data})

def add(request):
    if request.method == 'POST':
        teachinfo = models.TeachersInfo.objects.create(
            name = request.POST['teach_name'],
            gender = request.POST['teach_sex'],
            age = request.POST['teach_age'],
            course = request.POST['teach_course'],
            salary = request.POST['teach_salary'],
            address = request.POST['teach_address'],
            onboarding_time = request.POST['onboarding_time'],
            personal_info = request.POST['teach_info']
        )
        
        if teachinfo:
            return HttpResponseRedirect('/teacher/show')
    else:
        return render(request, 'teacher/add.html')
    
def deldata(request):
    pk = request.GET['id']
    res = models.TeachersInfo.objects.filter(id=pk).delete()
    if res:
        return HttpResponseRedirect('teacher/show')