from django import forms
from django.contrib.auth.models import User
from todo.models import ToDoModel

class SignUpForm(forms.ModelForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        
        
class SignInForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    
    
class ToDoModelForm(forms.ModelForm):
    class Meta:
        model= ToDoModel
        fields=['task_name']
        
class TodoEditModelForm(forms.ModelForm):
    class Meta:
        model= ToDoModel
        fields=['task_name','status']
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
        }