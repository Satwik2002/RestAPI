from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import item, user
from .serializers import itemSerializer

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

# Create your views here.
