from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .extend.greeting import getResponse
from .extend.food_detect import detect
from .models import Food, User, Eat
import time


food = ""
url = ""


def index(request):
    context = {}
    return render(request, 'banatalk/index.html',context)

def chatroom(request):
    global food
    global url

    print(request.POST)
    print(request.GET)
    if request.GET:

        print(list(request.GET.keys()))
        if list(request.GET.keys())[0] == "res1":
            quest = request.GET['res1']
            ans = getResponse(food,quest)
            print(ans)
            context = {
                "ans":ans,
                "imglink":url,
                "foodname":food+"君",
            }

            return render(request, 'banatalk/chatroom.html',context)
        else:
            url =  request.GET['res2']
            food = detect(url)
            # new_reserve = Reserve(reserver_name=username,use_text='temp',start_time=start_time,end_time=end_time)
            print(time.localtime())
            temp = time.localtime()
            print()
            print(temp[1])
            # YY_MM_DD_HH
            timestr = str(temp[0]) + "_" + str(temp[1]) + "_" + str(temp[2]) + "_" + str(temp[3])
            print(timestr)
            new_eat = Eat(name=food,weight=1,time=timestr)
            new_eat.save()

            # new_reserve.save()
            ans = ""
            context = {
                "ans":ans,
                "imglink":url,
                "foodname":food+"君",
            }

            return render(request, 'banatalk/chatroom.html',context)

    else:
        return render(request, 'banatalk/chatroom.html',context)

def stat(request):
    print("askdjfslad")
    eat_set = Eat.objects.all()
    energy = 0 #in mg/100g
    protein = 0 #in mg/100g
    fat = 0 #in mg/100g
    carbohydrate = 0 #in mg/100g


    for i in eat_set:
        print(i.name)
        food_obj = Food.objects.get(name=i.name)

        energy += food_obj.energy*i.weight
        protein += food_obj.protein*i.weight
        fat += food_obj.fat*i.weight
        carbohydrate += food_obj.carbohydrate*i.weight

    print(energy,protein,fat,carbohydrate)
    context = {
        'energy' : energy,
        'protein' : protein,
        'fat' : fat,
        'carbohydrate' : carbohydrate,
    }

    return render(request, 'banatalk/stat.html',context)

def addimg(request):
    print("addimg")
    context = {}
    return render(request, 'banatalk/addimg.html',context)
