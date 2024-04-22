"""sostransport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from patient_register.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('new_patient/', add_patient, name='home'),
    path('save_patient', save),
    path('dossier_patient/<id>/', dossier_patient),
    path('save_horaire', save_horaire),
    path('save_lesion', save_lesion),
    path('save_ouverture_yeux', save_ouverture_yeux),
    path('save_reponse_verbale', save_reponse_verbale),
    path('save_reponse_motrice', save_reponse_motrice),
    path('save_mouvement', save_mouvement),
    path('save_mise_condition', save_mise_condition)
]
