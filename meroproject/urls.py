"""
URL configuration for meroproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse , render
import random

def index(request):
    mylist= [
        
        {'name':"Aarav",
              'address':"Dharan",
              'profile_url':"https://pbs.twimg.com/profile_images/1099246432727560193/1WfFmMB9_400x400.jpg"
              },

              {'name':"Sujan",
               'address':"Biratnagar",
               'profile_url':""
               
               }
              
              ]
    context = {
        'mydata':random.randint(0,11000),
        'title':"Aarav Poudel Blog",
        'person_list':mylist
    }
    return render(request,'index.html',context)

def index1(request):
    return HttpResponse("OK")

def home(request):
    return HttpResponse("<h1>This is homepage</h1>")

def about(request):
    return HttpResponse("<h1>About Page</h1> <p>We are Mahendra Morang Adarsh Multiple Campus,<br>Biratnagar,Morang</p>")

def profile(request,username):
    print(username)


    profile_data = {
        'aarav':"Aarav Poudel",
        'hari22':"Hari Prasad Sharma",
        'sita':"Sita Mahalaxmi",
        'allu':"Allu Arjun"

    }


    result = profile_data.get(username)
    if result is not None:
        return HttpResponse(f"<h1>Profile of @{username}</h1> <p>{result}</p>")
    else:
        return HttpResponse(f"<h1>Profile of @{username} doesn't exist</h1> <p>error</p>")
    # return HttpResponse(f'<h1> This is profile page of {username}</h1> <img src="https://pbs.twimg.com/media/ECfs_66VAAAIKfp?format=jpg&name=900x900" style="height:200px;" >')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('new/',index1),
    path('home/',home),
    path('about/',about),
    path('profile/<str:username>/',profile)
]
