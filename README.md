# Assignment 1 Django project SE-2004 Dias Karibaev

## Installation
$ pip install django
$ pip install psycopg2
$ pip install mysql
$pip install mysqlclient

## Usage
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Task
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import path
from . import views


## Examples

![1](https://user-images.githubusercontent.com/51242971/150444690-2f743f66-aec3-42cf-a241-42b36b5a712f.png)
![2](https://user-images.githubusercontent.com/51242971/150444696-2fe8fe25-cc4a-43d5-915a-472dc0ae4355.png)
![3](https://user-images.githubusercontent.com/51242971/150444701-afa8fe9a-a9b7-4f9b-98b2-a59507d801af.png)




