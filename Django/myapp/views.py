from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
# Create your views here.
def hello(request, username):
    return HttpResponse(f"hola, {username}")

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')


def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def tasks(request):
    #tasks = get_object_or_404(Task, title=title)
    return render(request, 'tasks.html')