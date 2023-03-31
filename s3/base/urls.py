from . import views 
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('nav/', views.nav, name="nav"),
    path('create-room/', views.createRoom, name="create-room"),
    path('create-message/', views.createMessage, name="create-message"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete/<str:pk>/', views.delete, name="delete"),
]
