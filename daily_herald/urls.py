from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.HomePageView.as_view(), name='homepage'),
]
