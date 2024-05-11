from django.contrib import admin
from django.urls import path, include
from patient_register.views import *
from consommables.views import *


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', login, name='login'),
    path('home', home, name='home'),
    path('new_patient/', add_patient, name='add_patient'),
    path('save_patient', save),
    path('dossier_patient/<id>/', dossier_patient, name='dossier'),
    path('save_horaire', save_horaire),
    path('save_lesion', save_lesion),
    path('save_ouverture_yeux', save_ouverture_yeux, name='ouverture_yeux'),
    path('save_reponse_verbale', save_reponse_verbale),
    path('save_reponse_motrice', save_reponse_motrice),
    path('save_mouvement', save_mouvement),
    path('save_mise_condition', save_mise_condition),
    path('solute_drogue', solute_drogue),
    path('voie_aerienne', voie_aerienne),
    path('save_constant', save_constant),
    path('logout', logout),
    path('accounts/', include('accounts.urls')),
    path('consommable/', include('consommables.urls')),
    path('save_consommable', save_consomm_utilise),
    path('addConsommable/', addConsommable, name="addconsomm"),
]
