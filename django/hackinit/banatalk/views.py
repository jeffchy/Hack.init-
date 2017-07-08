from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse

def index(request):

    context = {
    
    }
    return render(request, 'banatalk/index.html',context)
