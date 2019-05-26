from django.urls import path
from . import views

urlpatterns = [
    path('', views.addid, name='addid'),
    path('register', views.register, name='register'),
    path('roomlist', views.roomlist, name='roomlist'),
]
