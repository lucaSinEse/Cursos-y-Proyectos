from django.http import HttpResponse
# Create your views here.
def hello(request, username):
    return HttpResponse(f"<h1>Hello {username}</h1>")

def about(request):
    return HttpResponse('About')

def index(request):
    return HttpResponse("<h1>Index Page</h1>")
