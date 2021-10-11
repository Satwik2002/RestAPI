from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='indexpage'),
    path('getAll/',views.showALL, name='getallurl'),
    path('getData/<int:id>',views.getData, name='getdata')
]