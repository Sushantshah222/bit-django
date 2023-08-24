from django.urls import path


from .views import *

urlpatterns = [
    path('blog/',blog_index,name="blog_index"),
    path('blog_detail/',blog_detail)

]