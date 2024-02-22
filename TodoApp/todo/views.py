from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.views import View
from todo.models import ToDoModel
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,DeleteView
from todo.forms import SignUpForm,SignInForm,ToDoModelForm,TodoEditModelForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


class Home(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            form=ToDoModel.objects.filter(user=request.user)
            return render(request,'home.html',{"form":form})
        else:
            return render(request,'home.html')
    

class SignUpView(View):
    # template_name='register.html'
    # model=User
    # form_class=SignUpForm
    # success_url=reverse_lazy('home')
    def get(self,request,*args,**kwargs):
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    def post(self,request,*args,**kwargs):
        data=SignUpForm(request.POST)
        if data.is_valid():
            User.objects.create_user(**data.cleaned_data)
            return redirect("signin")
        
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=SignInForm()
        return render(request,'signin.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=SignInForm(request.POST)
        if form.is_valid():
            u=form.cleaned_data.get("username")
            p=form.cleaned_data.get("password")
            user=authenticate(request,username=u,password=p)
            if user:
                login(request,user)
                messages.success(request, "Login Successfull")
                return redirect('home')
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('signin')


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home')
    
    
    
    
class ToDoView(CreateView):
    form_class=ToDoModelForm
    template_name='todo.html'
    success_url=reverse_lazy('home')
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    # def get(self,request,*args,**kwargs):
    #     form1=ToDoModelForm()
    #     return render(request,'todo.html',{"form1":form1})
    # def post(self,request,*args,**kwargs):
    #     form=ToDoModelForm(request.POST)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #         return redirect('home')
        
        
class TodoListView(ListView):
    template_name='todolist.html'
    model=ToDoModel
    context_object_name="form"
    
    def get_queryset(self):
        return ToDoModel.objects.filter(user=self.request.user)
    # def get(self,request,*args,**kwargs):
    #     form=ToDoModel.objects.filter(user=request.user)
    #     return render(request,'todolist.html',{"form":form})
    

class TodoDelete(DeleteView):
    # template_name='deletetodo.html'
    # model=ToDoModel
    # pk_url_kwarg='id'
    # success_url=reverse_lazy('home')
    def get(self,request,*args,**kwargs):
        id = kwargs.get('id')
        ToDoModel.objects.get(id=id).delete()
        return redirect('home')
    
    
class TodoEdit(View):
    def post(self,request,*args,**kwargs):
        id = kwargs.get('id')
        todo = ToDoModel.objects.get(id=id)
        if todo.status == True:
            todo.status = False
            todo.save()
        else:
            todo.status = True
            todo.save()
        return redirect('home')
    
class ToDoDetailView(DetailView):
    template_name='tododetail.html'
    model=ToDoModel
    context_object_name='form'
    pk_url_kwarg='id'
    # def get(self, request, *args, **kwargs):
    #     id=kwargs.get("id") 
    #     form=ToDoModel.objects.get(id=id)
    #     return render(request, "tododetail.html",{"form":form})
    
class ToDoEditView(View):
    # template_name='todoedit.html'
    # model=ToDoModel
    # pk_url_kwarg='id'
    # form_class=TodoEditModelForm
    # context_object_name='form'
    # success_url="list"
    
    
    # def form_valid(self, form):
    #     messages.success(self.request, "Data Updated")
    #     return super().form_valid(form)
    
    
    def get(self, request, *args, **kwargs):
        id=kwargs.get("id")
        form1=ToDoModel.objects.get(id=id)
        form2=TodoEditModelForm(instance=form1)
        return render(request, 'todoedit.html', {'form':form2})
    def post(self, request, *args, **kwargs):
        id=kwargs.get("id")
        form1=ToDoModel.objects.get(id=id)
        form2=TodoEditModelForm(request.POST, instance=form1)
        if form2.is_valid():
            form2.save()
            messages.success(self.request, "Data Updated")
            return redirect('home')
        else:
            messages.error(self.request, "Something Went Wrong")
            return redirect('home')