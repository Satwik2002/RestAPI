from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='indexpage'),
    path('getAll/',views.showALL, name='getallurl'),
    path('getData/<int:id>',views.getData, name='getdata'),
    path('create_item/',views.createItem),
    path('update_item/<int:id>', views.update_item),
    path('super/', views.super, name='super')
]