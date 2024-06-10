#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('I am at Home!')
    return render(request, 'home.html')

def about(request):
    #return HttpResponse('I am at About!')
    return render(request, 'about.html')