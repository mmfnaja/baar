from . import views
from django.urls import path

urlpatterns = [
    path('', views.Main.index),
    path('login/', views.Main.login),
    path('chatroom/', views.Main.chatroom),
    path('myaccount/', views.Main.myaccount),
    path('projects/', views.ProjectListView.as_view(), name='project')

    # path('models/',  views.Main.specific),
    # path('models/details/', views.Main.details),
]
