from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.
def hello(request, username):
    return HttpResponse(f"<h1>Hello {username}</h1>")

def about(request):
    return HttpResponse('About')

def index(request):
    return HttpResponse("<h1>Index Page</h1>")

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, title):
    tasks = get_object_or_404(Task, title=title)
    return HttpResponse(f'task: {tasks.title}')