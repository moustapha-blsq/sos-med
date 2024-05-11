from django.urls import path
from . import views


app_name = "consommable"

urlpatterns = [
    path('home/', views.get_consommable, name= "homeconsom"),
    
    path('delete_consommable/<id>/', views.delete_consommable, name="delete_consommable")
]