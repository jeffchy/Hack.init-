from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .extend.greeting import getResponse


food = ""



def index(request):

    context = {

    }
    return render(request, 'banatalk/index.html',context)

def chatroom(request):
    context = {

    }
    print(request.POST)
    print(request.GET)
    if request.GET:

        print(request.GET['res1'])
        quest = request.GET['res1']

        ans = getResponse("雪碧",quest)
        print(ans)
        context = {
            "ans":ans,
        }


        return render(request, 'banatalk/chatroom.html',context)


    else:
        return render(request, 'banatalk/chatroom.html',context)

def stat(request):
    print("askdjfslad")
    context = {}

    return render(request, 'banatalk/stat.html',context)
