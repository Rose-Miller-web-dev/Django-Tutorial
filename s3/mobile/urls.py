from django.urls import path
from . import views

urlpatterns = [
    path('mobile/', views.mobile, name="mobile"),
    path('mobile/info/<str:pk>/', views.info, name="info"),
]