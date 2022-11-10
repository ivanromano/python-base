# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Tarea
from django.shortcuts import get_object_or_404, render

# Create your views here.
def hello(request ):
    return render(request, 'index.html')

def mabe(request, username):
    print(username)
    return HttpResponse('<h1> mabe %s</h1>' % username)

def victini(request ):
    return render(request, 'about.html')

def project(request):
    projectss = Project.objects.values()
    return render(request, 'project.html', {
        'projectss': projectss
    })
    # return JsonResponse(project, safe=False)

def tareas(request):
    tareass = Tarea.objects.values()
    return render(request, 'tareas.html', {
        'tareass': tareass
    })
    # return HttpResponse('<h4> tareas %s </h4>' % tarea.tittle)
