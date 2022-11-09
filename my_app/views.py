# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1> VICTINI </h1')

def mabe(request):
    return HttpResponse('<h1> mabe </h1')
