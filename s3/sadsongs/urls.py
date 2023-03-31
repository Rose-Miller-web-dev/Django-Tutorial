from . import views
from django.urls import path

urlpatterns = [
    path('player/', views.player, name="player"),
    path('player/singer/<str:pk>/', views.singer, name="singer"),
    path('song/', views.song, name="song"),
]