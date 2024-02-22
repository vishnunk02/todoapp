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