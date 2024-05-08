from django.urls import path
from . import views


app_name = "consommable"

urlpatterns = [
    path('home/', views.get_consommable, name= 'home'),
    path('addConsommable', views.addConsommable)
]