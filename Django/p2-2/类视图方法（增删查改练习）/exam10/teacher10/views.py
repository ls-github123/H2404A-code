from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from django.views import View

# 展示教师信息视图模块
class ShowView(View):
    def get(self, request):
        data = models.TeacherModel.objects.all()
        return render(request, 'teacher/show.html', {'data':data})
    
    def post(self, request):
        select = request.POST['select']
        data = models.TeacherModel.objects.filter(tname__contains=select)
        return render(request, 'teacher/show.html', {'data':data})
    
# 添加教师信息视图模块
class AddInfoView(View):
    def get(self, request):
        return render(request, 'teacher/add.html')
    
    def post(self, request):
        teacherinfo = models.TeacherModel.objects.create(
            tname = request.POST.get('teach_name'),
            tclass = request.POST.get('teach_class'),
            tdesc = request.POST.get('teach_desc'),
        )
        if teacherinfo:
            return redirect('show')
        else:
            return HttpResponse('数据添加失败!', status=400)

# 教师信息编辑视图模块
class EditView(View):
    def get(self, request, id):
        data = models.TeacherModel.objects.get(id=id)
        return render(request, 'teacher/edit.html', locals())
    
    def post(self, request, id):
        result = models.TeacherModel.objects.get(id=id)
        result.tname = request.POST.get('teach_name')
        result.tclass = request.POST.get('teach_class')
        result.tdesc = request.POST.get('teach_desc')
        result.save()
        return redirect('show')

# 教师信息删除视图模块
class DeleteView(View):
    def get(self, request, id):
        res = models.TeacherModel.objects.filter(id=id).delete()
        if res[0]:
            return redirect('show')
        else:
            return HttpResponse('数据删除失败!', status=400)