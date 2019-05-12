from . import views
from django.urls import path

urlpatterns = [
    path('', views.Main.index),
    path('login/', views.Main.login),
    path('chatroom/', views.Main.chatroom),
    path('myaccount/', views.Main.myaccount)

    # path('models/',  views.Main.specific),
    # path('models/details/', views.Main.details),
]
