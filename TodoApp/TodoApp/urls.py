"""
URL configuration for TodoApp project.

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
from todo import views

urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('signup',views.SignUpView.as_view(),name="signup"),
    path('signin',views.SignInView.as_view(),name="signin"),
    path('signout',views.SignOutView.as_view(),name="signout"),
    path('todoform',views.ToDoView.as_view(),name="todoform"),
    path('list',views.TodoListView.as_view(),name="list"),
    path('deletedata/<int:id>',views.TodoDelete.as_view(),name="deletedata"),
    path('todoeditdata/<int:id>',views.TodoEdit.as_view(),name="todoeditdata"),
    path('tododetail/<int:id>',views.ToDoDetailView.as_view(),name="tododetail"),
    path('todoedit/<int:id>',views.ToDoEditView.as_view(),name="todoedit"),
]
