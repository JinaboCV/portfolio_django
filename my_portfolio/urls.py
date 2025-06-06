from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blogs', views.blogs, name='blogs'),
    path('blog_post', views.blog_post, name='blog_post'), 
]

