from django.urls import path

from . import views

urlpatterns = [
    #요청 내용
    path('', views.post_list, name='post_list'),
    path('post_list', views.post_list, name='post_list'),
    path('add/', views.add_list, name='add_list'),
    path('register', views.registerPost, name ='register'),
    path('detail/<int:post_id>', views.detailPost,name='detailPost'),
    path('detail/<int:post_id>/remove', views.deletePost,name='delete'),
    path('detail/<int:post_id>/editPost', views.editPost,name='editPost'),
    path('detail/<int:post_id>/edit', views.edit,name='edit'),
]
