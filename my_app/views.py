# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request ):
    return HttpResponse('<h1> VICTINI </h1')

def mabe(request, username):
    print(username)
    return HttpResponse('<h1> mabe </h1')

def victini(request):
    return HttpResponse('<h4> victini </h4')
