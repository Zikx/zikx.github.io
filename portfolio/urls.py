from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('newport/', views.newport, name='newport'),
    path('portcreate/', views.portcreate, name='portcreate'),
]