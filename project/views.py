import re
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Task
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
# Create your views here.

def loginpage(request):
    if request.method =='POST':
        username=request.POST['username'] 
        password=request.POST['password']

    
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:8000/')

    return render(request,'project/register.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

def Registerpage(request):
    form=UserCreationForm()
    context={'form':form}
    return render (request,'project/register1.html',context)




@login_required(login_url='login')
def list(request):
    Tasks = {'list' : Task.objects.all()}
    return render(request, 'project/project.html',Tasks)

@login_required(login_url='login')
def insert(request: HttpRequest):
    insert = Task(text = request.POST.get('text', False))
    insert.save()
    return redirect('http://127.0.0.1:8000/')

@login_required(login_url='login')
def delete(request,todo_id):
    delete = Task.objects.get(id=todo_id)
    delete.delete()
    return redirect('http://127.0.0.1:8000/')
