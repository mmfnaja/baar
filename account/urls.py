from django.urls import path
from . import views




urlpatterns = [
    path('myaccount/', views.myaccount),
]

