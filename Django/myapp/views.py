from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask
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
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    #tasks = get_object_or_404(Task, title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks.html',{
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        #Show interface
        return render(request, 'create_task.html',{
            'form': CreateNewTask()})
    else:
        Task.objects.create(
            title = request.POST['title'], 
            description = request.POST['description'], 
            project = Project.objects.get(id=2)
        )
        return redirect("/tasks/")