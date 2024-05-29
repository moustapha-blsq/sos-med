from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from patient_register.models import *
from consommables.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def login(request,*args, **kwargs):
    return render(request, 'index.html')

@login_required(login_url='login')
def home(request,*args, **kwargs):
    all_patients = Patient.objects.all()
    # Création de dictionnaire
    #patient_count = all_patients.count()
    context = {'patients': all_patients}
    #return HttpResponse(template.render())
    return render(request, 'home.html', context)

@login_required(login_url='login')
def add_patient(request,*args, **kwargs):
    personnels = Personnel.objects.all()
    context = {'personnels': personnels}
    return render(request, 'add_patient.html', context)

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
        statut = "Traité"
        diagnostic_evoq = request.POST['diagnostic_evoque']
        Patient.objects.create(prenom=prenom, nom=nom, age=age, sexe=sexe, adresse=adress, 
                                         telephone=telephone, pays_origine=pays_origine, ambulancier=ambulancier,
                                         origine_appel=origine_appel, statut = statut, motif_appel=motif_appel, lieu_intervention=lieu_intervention,
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
    
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def delete_horaire(request, id1, id2):
    horaire = Horaires.objects.get(pk=id1)
    horaire.delete()
    return redirect("/dossier_patient/"+str(id2))

@login_required(login_url='login')
def delete_lesion(request, id1, id2):
    lesion = lesions.objects.get(pk=id1)
    lesion.delete()
    return redirect("/dossier_patient/"+str(id2))

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
    
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def delete_ouverture_yeux(request, id1, id2):
    ouverture_yeux = Ouverture_des_yeux.objects.get(pk=id1)
    ouverture_yeux.delete()
    return redirect("/dossier_patient/"+str(id2))

@login_required(login_url='login')
def  save_reponse_verbale(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Reponses_verbale.objects.create(
            libelle         = request.POST['libelle_signe'],
            score           = int(request.POST['score']),
            patient         = my_patient
        )
    
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def delete_rep_verbale(request, id1, id2):
    rep_verb = Reponses_verbale.objects.get(pk=id1)
    rep_verb.delete()
    return redirect("/dossier_patient/"+str(id2))

@login_required(login_url='login')
def save_reponse_motrice(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        Reponses_motrice.objects.create(
            libelle         = request.POST['libelle_signe'],
            score           = int(request.POST['score']),
            patient         = my_patient
        )
    
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def delete_rep_motrice(request, id1, id2):
    rep_mot = Reponses_motrice.objects.get(pk=id1)
    rep_mot.delete()
    return redirect("/dossier_patient/"+str(id2))


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
    
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def delete_autre_signe(request, id1, id2):
    autre_signe = autre_signe_de_vie.objects.get(pk=id1)
    autre_signe.delete()
    return redirect("/dossier_patient/"+str(id2))

@login_required(login_url='login')
def save_mise_condition(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        scp     = request.POST['scope']
        dy      = request.POST['dyn']
        ox      = request.POST['oxy']
        coq     = request.POST['coquille']
        barq    = request.POST['barquette']
        vvp     = request.POST['vvp_kt']
        bd1     = request.POST['bd']
        bg1     = request.POST['bg']
        collier = request.POST['collier_cervical']
        attel   = request.POST['attelles']
        drain   = request.POST['drain_pleural']
        Mise_en_condition.objects.create(
            scope               = scp,
            dyn                 = dy,
            oxy                 = ox,
            coquille            = coq,
            barquette           = barq,
            vvp_kt              = vvp,
            bd                  = bd1,
            bg                  = bg1,
            ktc                 = request.POST['ktc'],
            sonde_gast          = request.POST['sonde_gast'],
            sonde_vest          = request.POST['sonde_ves'],
            collier_cervical    = collier,
            attelles            = attel,
            drain_pleural       = drain,
            autre               = request.POST['autre'],
            patient             = my_patient
        )
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def delete_mise_condition(request, id1, id2):
    conditions = Mise_en_condition.objects.get(pk=id1)
    conditions.delete()
    return redirect("/dossier_patient/"+str(id2))


@login_required(login_url='login')
def solute_drogue(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient'])
        solute = request.POST.getlist('solute_drogues')
        Solutes_drogues.objects.create(
        libelle = solute[0],
        patient = my_patient
        )
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def delete_sol_drogue(request, id1, id2):
    sol = Solutes_drogues.objects.get(pk=id1)
    sol.delete()
    return redirect("/dossier_patient/"+str(id2))


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
   
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def delete_voie_aerienne(request, id1, id2):
    va = Voies_aeriennes.objects.get(pk=id1)
    va.delete()
    return redirect("/dossier_patient/"+str(id2))


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
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def delete_constant(request, id1, id2):
    constant = Constant.objects.get(pk=id1)
    constant.delete()
    return redirect("/dossier_patient/"+str(id2))

@login_required(login_url='login')
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
    return redirect("/dossier_patient/"+str(my_patient.id))

@login_required(login_url='login')
def del_consommable_utilise(request, id1, id2):
    const_ut = Consommable_utilise.objects.get(pk=id1)
    const_ut.delete()
    return redirect("/dossier_patient/"+str(id2))

@login_required(login_url='login')
def list_personnel(request):
    all_personnel = Personnel.objects.all()
    context = {'personnels': all_personnel}
    return render(request, 'personnel.html', context)

@login_required(login_url='login')
def save_personnel(request):
    if request.method == 'POST':
        Personnel.objects.create(
            matricule           = request.POST['matricule'],
            nom                 = request.POST['nom'],
            prenom              = request.POST['prenom'],
            telephone           = request.POST['tel'],
            specialite          = request.POST['specialite'],
            adresse             = request.POST['adresse'],
            email               = request.POST['email'],
            service             = request.POST['service'],
            annee_recrutement   = request.POST['annee_recrut'],
            diplome_obtenu      = request.POST['diplome'],
            grade               = request.POST['grade'],
            commentaire         = request.POST['commentaire'],
            #is_valid            = 1

        )
    return redirect("personnel")

@login_required(login_url='login')
def edit_patient(request, id):
    patient = Patient.objects.get(pk=id)
    all_personnel = Personnel.objects.all()
    context = {'patient' : patient, 'personnels': all_personnel}
    return render(request, 'edit_patient.html', context)

@login_required(login_url='login')
def update_patient(request):
    if request.method == 'POST':
        my_patient = Patient.objects.get(pk=request.POST['patient_id'])
        my_patient.nom          = request.POST['nom']
        my_patient.prenom       = request.POST['prenom']
        if request.POST['sexe'] != "Choisir...":
            my_patient.sexe     = request.POST['sexe']
        my_patient.age          = request.POST['age']
        my_patient.adresse      = request.POST['adresse']
        my_patient.telephone    = request.POST['telephone']
        if request.POST['pays_origine'] != "Choisir...":
            my_patient.pays_origine = request.POST['pays_origine']
        if request.POST['ambulancier'] != "Choisir...":
            my_patient.ambulancier = request.POST['ambulancier']
        my_patient.origine_appel   = request.POST['origine_appel']
        my_patient.motif_appel     = request.POST['motif_appel']
        if request.POST['lieu_intervention'] != "Choisir...":
            my_patient.lieu_intervention = request.POST['lieu_intervention']
        if request.POST['decision'] != "Choisir...":
            my_patient.decision = request.POST['decision']
        my_patient.trajet = request.POST['trajet']
        my_patient.numero_ambu = request.POST['numero_ambulance']
        if request.POST['statut'] != "Choisir...":
            my_patient.statut = request.POST['statut']
        #statut = "Traité"
        diagnostic_evoq = request.POST['diagnostic_evoque']
        my_patient.save()
    return redirect("home")

def logout_view(request):
    logout(request)
    return redirect('/')







        

        

