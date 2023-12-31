from django.urls import path
from . import views

urlpatterns = [
    
    path('buscar_habitaciones/', views.buscar_habitaciones, name='buscar_habitaciones'),
    path('crear_reserva/<int:id_habitacion>/', views.crear_reserva, name='crear_reserva'),
    path('detalle_habitacion/<int:id_habitacion>/', views.detalle_habitacion, name='detalle_habitacion'),
    path('detalle_reserva/<int:id_reserva>/', views.detalle_reserva, name='detalle_reserva'),
    path('', views.homepage, name='homepage'),
    path('registro/', views.registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    
 
]