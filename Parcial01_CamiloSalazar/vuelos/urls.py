from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                        
    path('registro/', views.crear_vuelo, name='create'),    
    path('lista/', views.listar_vuelos, name='list'),          
    path('estadisticas/', views.estadisticas, name='stats'),          
]
