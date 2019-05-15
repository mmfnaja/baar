from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('', views.Main.index),
    path('login/', auth_views.LoginView.as_view(template_name='signup.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('chatroom/', views.Main.chatroom),
    path('myaccount/', views.Main.myaccount),
    path('projects/', views.ProjectListView.as_view(), name='project')

    # path('models/',  views.Main.specific),
    # path('models/details/', views.Main.details),
]
