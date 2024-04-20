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
    lesion = lesions.objects.filter(patient=id)
    ouverture_yeux = Ouverture_des_yeux.objects.filter(patient=id)
    rep_verbale = Reponses_verbale.objects.filter(patient=id)
    horaire_data = Horaires.objects.filter(patient=id)
    rep_motrice = Reponses_motrice.objects.filter(patient=id)
    context = {'patient': patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 'reponses_mot': rep_motrice}
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
    ouverture_yeux = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 'reponses_mot': rep_motrice}
    return render(request, 'dossier.html', context)
        
def save_lesion(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        denomination  = request.POST['nom_lesion'],
        #partie_lesion = request.POST[''],
        crane         = request.POST['crane']
        face          = request.POST['face']
        cou           = request.POST['cou'],
        rachis        = request.POST['rachis']
        thorax        = request.POST['thorax']
        abdomen       = request.POST['abdomen']
        bassin        = request.POST['bassin']
        msd           = request.POST['msd']
        msg           = request.POST['msg']
        mid           = request.POST['mid']
        mig           = request.POST['mig']
        autre         = request.POST['autre']
        #patient       = my_patient
        lesions.objects.create(
            denomination  = denomination,
            #partie_lesion = request.POST[''],
            crane         = crane,
            face          = face,
            cou           = cou,
            rachis        = rachis,
            thorax        = thorax,
            abdomen       = abdomen,
            bassin        = bassin,
            msd           = msd,
            msg           = msg,
            mid           = mid,
            mig           = mig,
            autre         = autre,
            patient       = my_patient
        )
    ouverture_yeux = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 'reponses_mot': rep_motrice}
    return render(request, 'dossier.html', context)
    
def save_ouverture_yeux(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Ouverture_des_yeux.objects.create(
            libelle         = request.POST['libelle_signe'],
            score           = int(request.POST['score']),
            patient         = my_patient
        )
    ouverture_yeux = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 'reponses_mot': rep_motrice}
    return render(request, 'dossier.html', context)
    
def  save_reponse_verbale(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Reponses_verbale.objects.create(
            libelle         = request.POST['libelle_signe'],
            score           = int(request.POST['score']),
            patient         = my_patient
        )
    ouverture_yeux = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 'reponses_mot': rep_motrice}
    return render(request, 'dossier.html', context)

def save_reponse_motrice(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Reponses_motrice.objects.create(
            libelle         = request.POST['libelle_signe'],
            score           = int(request.POST['score']),
            patient         = my_patient
        )
    ouverture_yeux = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 'reponses_mot': rep_motrice}
    return render(request, 'dossier.html', context)



        

        

