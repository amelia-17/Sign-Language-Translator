from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-sign/', views.get_sign, name='get_sign'),
    path('', views.video_feed, name='video_feed'),
    path('home/', views.index, name='index'),
]
