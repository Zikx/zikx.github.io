from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('newport/', views.newport, name='newport'),
    path('portcreate/', views.portcreate, name='portcreate'),
]