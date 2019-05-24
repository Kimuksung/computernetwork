from django.urls import path
from . import views

urlpatterns = [
    path('', views.addid, name='addid'),
]
