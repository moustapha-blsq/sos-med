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
    path('delete_horaire/<id1>/<id2>/', delete_horaire, name="delete_horaire"),
    path('delete_lesion/<id1>/<id2>/', delete_lesion, name="delete_lesion"),
    path('delete_ouverture_yeux/<id1>/<id2>/', delete_ouverture_yeux, name="delete_lesion"),
    path('delete_rep_verb/<id1>/<id2>/', delete_rep_verbale, name="delete_rep_verb"),
    path('delete_rep_motrice/<id1>/<id2>/', delete_rep_motrice, name="delete_rep_motrice"),
    path('delete_autre_signe/<id1>/<id2>/', delete_autre_signe, name="delete_rep_motrice"),
    path('mise_condition/<id1>/<id2>/', delete_mise_condition, name="delete_mise_condition"),
    path('delete_sol_drogue/<id1>/<id2>/', delete_sol_drogue, name="delete_solute_drogue"),
    path('delete_voie_aerienne/<id1>/<id2>/', delete_voie_aerienne, name="delete_voie_aerienne"),
    path('delete_constant/<id1>/<id2>/', delete_constant, name="delete_constant"),
    path('del_consommable_utilise/<id1>/<id2>/', del_consommable_utilise, name="del_consommable_utilise")
]
