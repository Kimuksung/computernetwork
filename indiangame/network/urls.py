from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.addid, name='addid'),
    path('register', views.register, name='register'),
    path('roomlist', views.roomlist, name='roomlist'),
    path('room', views.room, name='room'),
    path('waiting', views.game, name='game'),
    re_path(r'room/(?P<name>[a-zA-Z0-9]+)/$', views.game,name='game'),
    #path('room/<game:name>',views.game,name='game'),
    #path('room/<char:name>',views.game,name='game'),
]
