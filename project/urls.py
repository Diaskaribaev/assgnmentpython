from django.urls import path
from . import views

urlpatterns =[
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('register/',views.Registerpage,name='register'),
    path('',views.list),
    path('insert/',views.insert,name='insert_item'),
    path('delete/<int:todo_id>/',views.delete,name='delete'),
]
