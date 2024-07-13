from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('blogs/', views.blogs, name='blogs'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories'),
    path('blog/<int:id>/', views.blogdetails, name='blogdetails'),
]
