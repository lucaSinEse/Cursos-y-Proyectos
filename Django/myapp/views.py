from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.
def hello(request, username):
    return HttpResponse(f"hola, {username}")

def about(request):
    username = 'Luca'
    return render(request, 'about.html',{
        'username': username
    })

def index(request):
    title = "Django Course!!"
    return render(request, 'index.html',{
        'title': title
    })


def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def tasks(request):
    #tasks = get_object_or_404(Task, title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html',{
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        #Show interface
        return render(request, 'tasks/create_task.html',{
            'form': CreateNewTask()})
    else:
        Task.objects.create(
            title = request.POST['title'], 
            description = request.POST['description'], 
            project = Project.objects.get(id=2)
        )
        return redirect("tasks")

def create_project(request):
    if request.method == 'GET':
            return render(
                request, 'projects/create_project.html',
                {'form': CreateNewProject()}
            )
    else:
        Project.objects.create(
            name = request.POST['name']
        )
        return redirect("projects")

def project_details(request, id):
    print(id)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id = id)
    return render(request, 'projects/detail.html',{
        'project': project,
        'tasks': tasks
    })