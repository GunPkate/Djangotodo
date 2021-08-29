from django.shortcuts import render
from django.http import HttpResponse
from .models import Alltask, Project
# Create your views here.
def Home(request):

    myproject = 'Travel'
    # projectlist = ['Investment','Programming','Hobbies']
    projectlist = Project.objects.all().order_by('id').reverse() #.order_by('id').reverse() = new project comes first
    for p in projectlist:
        search = Alltask.objects.filter(project=p)
        p.alltask = search

    context = {'list':myproject,'list2':projectlist} #import to HTML
    return render(request,'task/home.html',context)

def Contact(request):
    return HttpResponse('<h1>Contact: 0832224644<h1>')

def About(request):
    return render(request,'task/about.html')

def AddProject(request):
    context = {}
    if request.method == 'POST':
        data = request.POST.copy()
        print('DATA',data)
        project_name = data.get('project_name')
        project_desc = data.get('project_desc')
        newproject = Project()
        newproject.project_name = project_name
        newproject.project_desc = project_desc
        newproject.save()
        context['alert'] = 'Saved'

    return render(request,'task/addproject.html',context)

def AddTask(request):
    context = {}
    allproject = Project.objects.all()
    context['allproject'] = allproject
    if request.method == 'POST':
        data = request.POST.copy()
        print('DATA',data)
        projectid = data.get('projectid')
        project = Project.objects.get(id=int(projectid))
        task_name = data.get('task_name')
        task_desc = data.get('task_desc')

        newtask = Alltask() #models.py
        newtask.project = project 
        newtask.task_name = task_name
        newtask.task_desc = task_desc
        newtask.save()
        context['alert'] = 'Saved'

    return render(request,'task/addtask.html',context)
