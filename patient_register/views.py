from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from patient_register.models import *

def home(request,*args, **kwargs):
    template = loader.get_template('home.html')
    all_patients = Patient.objects.all()
    # Création de dictionnaire
    #patient_count = all_patients.count()
    context = {'patients': all_patients}
    #return HttpResponse(template.render())
    return render(request, 'home.html', context)

def add_patient(request,*args, **kwargs):
    template = loader.get_template('add_patient.html')
    return HttpResponse(template.render())


def save(request):
    if request.method == 'POST':
        prenom = request.POST['prenom']
        nom = request.POST['nom']
        age = request.POST['age']
        sexe = request.POST['sexe']
        telephone = request.POST['telephone']
        adress = request.POST['adresse'],
        pays_origine = request.POST['pays_origine'],
        ambulancier = request.POST['ambulancier'],
        origine_appel = request.POST['origine_appel'],
        motif_appel = request.POST['motif_appel'],
        lieu_intervention = request.POST['lieu_intervention'],
        decision = request.POST['decision'],
        trajet = request.POST['trajet'],
        numero_ambu = request.POST['numero_ambulance'],
        diagnostic_evoq = request.POST['diagnostic_evoque'],
        patient = Patient.objects.create(prenom=prenom, nom=nom, age=age, sexe=sexe, adresse=adress, 
                                         telephone=telephone, pays_origine=pays_origine, ambulancier=ambulancier,
                                         origine_appel=origine_appel, motif_appel=motif_appel, lieu_intervention=lieu_intervention,
                                         decision=decision, trajet=trajet, numero_ambulance=numero_ambu, diagnostique_evoque=diagnostic_evoq)
    all_patients = Patient.objects.all()
    context = {'patients': all_patients}
    #return HttpResponse(template.render())
    return render(request, 'home.html', context)

def dossier_patient(request, id):
    patient = Patient.objects.get(pk=id)
    horaire_data = Horaires.objects.filter(patient=id)
    context = {'patient': patient, 'horaires': horaire_data}
    return render(request, 'dossier.html', context)

def save_horaire(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        ht     = request.POST['ht']
        d_base = request.POST['d_base']
        a_lieu = request.POST['a_lieu']
        d_lieu = request.POST['d_lieu']
        asr    = request.POST['asr']
        dsr    = request.POST['dsr']
        a_base = request.POST['a_base']
        duree  = request.POST['duree']
        Horaires.objects.create(
            ht = ht,
            d_base = d_base,
            a_lieu = a_lieu,
            d_lieu = d_lieu,
            asr = asr,
            dsr = dsr,
            a_base = a_base,
            duree = duree,
            patient = my_patient
        )
        horaire_data = Horaires.objects.filter(patient=request.POST['patient'])
        context = {'patient': my_patient, 'horaires' : horaire_data}
        return render(request, 'dossier.html', context)
        


