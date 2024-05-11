from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from patient_register.models import *
from consommables.models import *
from django.contrib.auth.decorators import login_required

def login(request,*args, **kwargs):
    return render(request, 'index.html')

@login_required(login_url='login')
def home(request,*args, **kwargs):
    template = loader.get_template('home.html')
    all_patients = Patient.objects.all()
    # Création de dictionnaire
    #patient_count = all_patients.count()
    context = {'patients': all_patients}
    #return HttpResponse(template.render())
    return render(request, 'home.html', context)

@login_required(login_url='login')
def add_patient(request,*args, **kwargs):
    template = loader.get_template('add_patient.html')
    return HttpResponse(template.render())

@login_required(login_url='login')
def save(request):
    if request.method == 'POST':
        prenom = request.POST['prenom']
        nom = request.POST['nom']
        age = request.POST['age']
        sexe = request.POST['sexe']
        telephone = request.POST['telephone']
        adress = request.POST['adresse']
        pays_origine = request.POST['pays_origine']
        ambulancier = request.POST['ambulancier']
        origine_appel = request.POST['origine_appel']
        motif_appel = request.POST['motif_appel']
        lieu_intervention = request.POST['lieu_intervention']
        decision = request.POST['decision']
        trajet = request.POST['trajet']
        numero_ambu = request.POST['numero_ambulance']
        diagnostic_evoq = request.POST['diagnostic_evoque']
        patient = Patient.objects.create(prenom=prenom, nom=nom, age=age, sexe=sexe, adresse=adress, 
                                         telephone=telephone, pays_origine=pays_origine, ambulancier=ambulancier,
                                         origine_appel=origine_appel, motif_appel=motif_appel, lieu_intervention=lieu_intervention,
                                         decision=decision, trajet=trajet, numero_ambulance=numero_ambu, diagnostique_evoque=diagnostic_evoq)
    all_patients = Patient.objects.all()
    context = {'patients': all_patients}
    #return HttpResponse(template.render())
    #return render(request, 'home.html', context)
    return redirect("/home")

@login_required(login_url='login')
def dossier_patient(request, id):
    patient         = Patient.objects.get(pk=id)
    horaire_data    = Horaires.objects.filter(patient=id)
    lesion          = lesions.objects.filter(patient=id)
    ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=id)
    rep_verbale     = Reponses_verbale.objects.filter(patient=id)
    horaire_data    = Horaires.objects.filter(patient=id)
    rep_motrice     = Reponses_motrice.objects.filter(patient=id)
    autre_signe     = autre_signe_de_vie.objects.filter(patient=id)
    mise_condition  = Mise_en_condition.objects.filter(patient=id)
    voies           = Voies_aeriennes.objects.filter(patient=id)
    drogue          = Solutes_drogues.objects.filter(patient=id)
    constant        = Constant.objects.filter(patient=id)
    consommables    = Consommable.objects.all()
    consommables_utilises        = Consommable_utilise.objects.filter(patient=id)
    context = {'patient': patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables': consommables, 'consommables_utilises': consommables_utilises}
    return render(request, 'dossier.html', context)

@login_required(login_url='login')
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
    ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale     = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion          = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data    = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice     = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    autre_signe     = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
    mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
    voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
    drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
    constant        = Constant.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')   
def save_lesion(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        denomination  = request.POST['nom_lesion']
        #partie_lesion = request.POST[''],
        crane         = request.POST['crane']
        face          = request.POST['face']
        cou           = request.POST['cou']
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
    ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale     = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion          = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data    = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice     = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    autre_signe     = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
    mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
    voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
    drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
    constant        = Constant.objects.filter(patient=request.POST['patient'])
    consommables_utilises        = Consommable_utilise.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables_utilises': consommables_utilises}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def save_ouverture_yeux(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Ouverture_des_yeux.objects.create(
            libelle         = request.POST['libelle_signe'],
            score           = int(request.POST['score']),
            patient         = my_patient
        )
    ouverture_yeux = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale    = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion         = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data   = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice    = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    autre_signe    = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
    mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
    voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
    drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
    constant        = Constant.objects.filter(patient=request.POST['patient'])
    consommables_utilises        = Consommable_utilise.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables_utilises': consommables_utilises}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def  save_reponse_verbale(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Reponses_verbale.objects.create(
            libelle         = request.POST['libelle_signe'],
            score           = int(request.POST['score']),
            patient         = my_patient
        )
    ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale     = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion          = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data    = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice     = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    autre_signe     = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
    mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
    voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
    drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
    constant        = Constant.objects.filter(patient=request.POST['patient'])
    consommables_utilises        = Consommable_utilise.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables_utilises': consommables_utilises}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def save_reponse_motrice(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Reponses_motrice.objects.create(
            libelle         = request.POST['libelle_signe'],
            score           = int(request.POST['score']),
            patient         = my_patient
        )
    ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale     = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion          = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data    = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice     = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    autre_signe     = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
    mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
    voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
    drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
    constant        = Constant.objects.filter(patient=request.POST['patient'])
    consommables_utilises        = Consommable_utilise.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables_utilises': consommables_utilises}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def save_mouvement(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        autre_signe_de_vie.objects.create(
            fourmillement_extremite = request.POST['fourmillement'],
            mouvement_de_ms = request.POST['mouvement_ms'],
            mouvement_de_mi = request.POST['mouvement_mi'],
            patient = my_patient
        )
    ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale     = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion          = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data    = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice     = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    autre_signe     = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
    mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
    voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
    drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
    constant        = Constant.objects.filter(patient=request.POST['patient'])
    consommables_utilises        = Consommable_utilise.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables_utilises': consommables_utilises}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def save_mise_condition(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        scp     = request.POST.getlist('scope')
        dy      = request.POST.getlist('dyn')
        ox      = request.POST.getlist('oxy')
        coq     = request.POST.getlist('coquille')
        barq    = request.POST.getlist('barquette')
        vvp     = request.POST.getlist('vvp_kt')
        bd1     = request.POST.getlist('bd')
        bg1     = request.POST.getlist('bg')
        collier = request.POST.getlist('collier_cervical')
        attel   = request.POST.getlist('attelles')
        drain   = request.POST.getlist('drain_pleural')
        Mise_en_condition.objects.create(
            scope               = scp[0],
            dyn                 = dy[0],
            oxy                 = ox[0],
            coquille            = coq[0],
            barquette           = barq[0],
            vvp_kt              = vvp[0],
            bd                  = bd1[0],
            bg                  = bg1[0],
            ktc                 = request.POST['ktc'],
            sonde_gast          = request.POST['sonde_gast'],
            sonde_vest          = request.POST['sonde_ves'],
            collier_cervical    = collier[0],
            attelles            = attel[0],
            drain_pleural       = drain[0],
            autre               = request.POST['autre'],
            patient             = my_patient
        )
    ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale     = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion          = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data    = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice     = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    autre_signe     = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
    mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
    voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
    drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
    constant        = Constant.objects.filter(patient=request.POST['patient'])
    consommables_utilises        = Consommable_utilise.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables_utilises': consommables_utilises}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def solute_drogue(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        solute = request.POST.getlist('solute_drogues')
        Solutes_drogues.objects.create(
        libelle = solute[0],
        patient = my_patient
        )
    ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale     = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion          = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data    = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice     = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    autre_signe     = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
    mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
    voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
    drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
    constant        = Constant.objects.filter(patient=request.POST['patient'])
    consommables_utilises        = Consommable_utilise.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables_utilises': consommables_utilises}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def voie_aerienne(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Voies_aeriennes.objects.create(
            o2          = request.POST['o2'],
            intubation  = request.POST['intubation'],
            sonde       = request.POST['sonde'],
            fio2        = request.POST['fio2'],
            frequence   = request.POST['frequence'],
            vol_courant = request.POST['vol_courant'],
            peep        = request.POST['peep'],
            patient     = my_patient
        )
    ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale     = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion          = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data    = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice     = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    autre_signe     = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
    mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
    voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
    drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
    constant        = Constant.objects.filter(patient=request.POST['patient'])
    consommables_utilises        = Consommable_utilise.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables_utilises': consommables_utilises}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def save_constant(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Constant.objects.create(
            heure       = request.POST['heure'],
            poul        = request.POST['poul'],
            TA          = request.POST['ta'],
            FR          = request.POST['fr'],
            spo2_fioo2  = request.POST['spo2_fio2'],
            temperature = request.POST['temperature'],
            glasgow     = request.POST['glasgow'],
            glycemie    = request.POST['glycemie'],
            douleur     = request.POST['douleur'],
            diurese     = request.POST['diurese'],
            commentaire = request.POST['commentaire'],
            patient     = my_patient
        )
    ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
    rep_verbale     = Reponses_verbale.objects.filter(patient=request.POST['patient'])
    lesion          = lesions.objects.filter(patient=request.POST['patient'])
    horaire_data    = Horaires.objects.filter(patient=request.POST['patient'])
    rep_motrice     = Reponses_motrice.objects.filter(patient=request.POST['patient'])
    autre_signe     = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
    mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
    voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
    drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
    constant        = Constant.objects.filter(patient=request.POST['patient'])
    consommables_utilises        = Consommable_utilise.objects.filter(patient=request.POST['patient'])
    context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables_utilises': consommables_utilises}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

def save_consomm_utilise(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Consommable_utilise.objects.create(
            nom_consommable = request.POST['nom_consommable'],
            nombre          = request.POST['nombre'],
            charges         = request.POST['charges'],
            fnc             = request.POST['fnc'],
            patient         = my_patient
        )
        ouverture_yeux  = Ouverture_des_yeux.objects.filter(patient=request.POST['patient'])
        rep_verbale     = Reponses_verbale.objects.filter(patient=request.POST['patient'])
        lesion          = lesions.objects.filter(patient=request.POST['patient'])
        horaire_data    = Horaires.objects.filter(patient=request.POST['patient'])
        rep_motrice     = Reponses_motrice.objects.filter(patient=request.POST['patient'])
        autre_signe     = autre_signe_de_vie.objects.filter(patient=request.POST['patient'])
        mise_condition  = Mise_en_condition.objects.filter(patient=request.POST['patient'])
        voies           = Voies_aeriennes.objects.filter(patient=request.POST['patient'])
        drogue          = Solutes_drogues.objects.filter(patient=request.POST['patient'])
        constant        = Constant.objects.filter(patient=request.POST['patient'])
        consommables_utilises        = Consommable_utilise.objects.filter(patient=request.POST['patient'])
        context = {'patient': my_patient, 'horaires' : horaire_data, 'list_lesion': lesion,
               'ouverture_des_yeux': ouverture_yeux, 'reponses_verbale': rep_verbale, 
               'reponses_mot': rep_motrice, 'autres_signe': autre_signe, 'mise_en_cond': mise_condition,
               'voies_aerien': voies, 'solute_drogue': drogue, 'my_constants': constant, 'consommables_utilises': consommables_utilises}
    #return render(request, 'dossier.html', context)
    return redirect("/dossier_patient/"+str(my_patient.id))

def logout(request):
    return render(request, 'index.html')







        

        

