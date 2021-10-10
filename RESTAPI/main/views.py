from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == 'POST' :
        return HttpResponse("Hello")
    else:   
        return render(request,'main/index.html')

# Create your views here.
