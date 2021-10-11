from django import forms
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import item, user
from .serializers import itemSerializer
from main import serializers
from .forms import itemForm

def home(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        if request.POST.get('mobile') is not None :
            mobile = request.POST.get('mobile')
            obj = user.objects.create(name=username,phone=mobile,password=password)
            obj.save()
            return HttpResponse('you are registered!')
        else:
            li = user.objects.get(name=username,password=password)
            if li is not None :
                items = item.objects.all()
                return render(request, 'main/mainpage.html', { 'items': items})
            else:
                return HttpResponse('sorry! try again')
    else:   
        return render(request,'main/index.html')


def showALL(request):
    items = item.objects.all()
    serializer = itemSerializer(items,many=True)
    return JsonResponse(serializer.data, safe=False)

def getData(request, id):
    info = item.objects.get(id = id)
    serializer = itemSerializer(info)
    return JsonResponse(serializer.data, safe=False)

def super(request):
    items = item.objects.all()
    return render(request, 'main/super.html', {'items': items})

    
def createItem(request):
    form = itemForm()
    s = ''
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid:
            form.save()
            s='created item and saved to db'
        return HttpResponse(s)
    return render(request, 'main/itemform.html', {'form':itemForm()})

def update_item(request, id):
    items = item.objects.get(id=id)
    print(items)
    form = itemForm(instance=items)
    if request.method == 'POST':
        form = itemForm(request.POST,instance=items)
        if form.is_valid:
            form.save()
        return HttpResponse('updated item on db')
    return render(request, 'main/itemform.html', {'form':form})



