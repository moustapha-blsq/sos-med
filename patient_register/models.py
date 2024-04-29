from django.db import models


class Patient(models.Model):
  nom = models.CharField(max_length=100)
  prenom = models.CharField(max_length=150)
  sexe = models.CharField(max_length=10)
  age = models.IntegerField(null=True)
  adresse = models.CharField(max_length=255)
  telephone = models.CharField(max_length=50)
  pays_origine = models.CharField(max_length=50)
  ambulancier = models.CharField(max_length=50, null = True)
  origine_appel = models.CharField(max_length=50, null = True)
  motif_appel = models.CharField(max_length=150, null = True)
  lieu_intervention = models.CharField(max_length=50, null = True)
  decision = models.CharField(max_length=150, null = True)
  trajet = models.CharField(max_length=150, null = True)
  numero_ambulance = models.CharField(max_length=25, null = True)
  diagnostique_evoque = models.CharField(max_length=250, null = True)
  date_creation = models.DateTimeField(auto_now_add=True, null=True)
  class Meta:
        db_table = 'Patient'

class Intervention(models.Model):
  medecin = models.CharField(max_length=100)
  paramedical = models.CharField(max_length=100)
  ambulancier = models.CharField(max_length=100)
  origine_appel = models.CharField(max_length=100)
  motif_appel = models.CharField(max_length=255)
  lieux_intervention = models.CharField(max_length=100)
  decision = models.CharField(max_length=100)
  trajet = models.CharField(max_length=100)
  diagnostique_evoque = models.CharField(max_length=100)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
  class Meta:
        db_table = 'Intervention'

class Horaire(models.Model):
    ht = models.CharField(max_length=10)
    d_bae = models.CharField(max_length=10)
    a_lieu = models.CharField(max_length=10)
    d_lieu = models.CharField(max_length=10)
    asr = models.CharField(max_length=10)
    a_base = models.CharField(max_length=10)
    dsr = models.CharField(max_length=10)
    duree = models.CharField(max_length=15)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'Horaire'
class Lesion(models.Model):
    nom_lesion = models.CharField(max_length=50)
    organe = models.CharField(max_length=50)
    observation = models.CharField(max_length=150)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'Lesion'

class Horaires(models.Model):
    ht = models.CharField(max_length=15)
    d_base = models.CharField(max_length=15)
    a_lieu = models.CharField(max_length=15)
    d_lieu = models.CharField(max_length=15)
    asr = models.CharField(max_length=15)
    dsr = models.CharField(max_length=15)
    a_base = models.CharField(max_length=15)
    duree = models.CharField(max_length=25)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'Horaires'

class lesions(models.Model):
    denomination  = models.CharField(max_length=50, null=True)
    partie_lesion = models.CharField(max_length=25, null=True)
    crane         = models.CharField(max_length=50, null=True)
    face          = models.CharField(max_length=50, null=True)
    cou           = models.CharField(max_length=50, null=True)
    rachis        = models.CharField(max_length=50, null=True)
    thorax        = models.CharField(max_length=50, null=True)
    abdomen       = models.CharField(max_length=50, null=True)
    bassin        = models.CharField(max_length=50, null=True)
    msd           = models.CharField(max_length=50, null=True)
    msg           = models.CharField(max_length=50, null=True)
    mid           = models.CharField(max_length=50, null=True)
    mig           = models.CharField(max_length=50, null=True)
    autre         = models.CharField(max_length=150)
    patient       = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'Lesions'

class Ouverture_yeux(models.Model):
    spontane = models.IntegerField
    au_bruit = models.IntegerField
    a_la_douleur = models.IntegerField
    nulle = models.IntegerField
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'Ouverture_yeux'

class Reponse_verbale(models.Model):
    oriente = models.IntegerField
    confuse = models.IntegerField
    inaproprie = models.IntegerField
    incomprehensible = models.IntegerField
    nulle = models.IntegerField
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'Reponse_verbale'
    
class Reponse_motrice(models.Model):
    a_la_commande = models.IntegerField
    oriente = models.IntegerField
    flexion_retrait = models.IntegerField
    decortication = models.IntegerField
    decerebration = models.IntegerField
    nulle = models.IntegerField
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'Reponse_motrice'

class autre_signe_de_vie(models.Model):
    fourmillement_extremite = models.CharField(max_length=5)
    mouvement_de_ms = models.CharField(max_length=5)
    mouvement_de_mi = models.CharField(max_length=5)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'autre_signe_vie'

class Ouverture_des_yeux(models.Model):
    libelle = models.CharField(max_length=25)
    score   = models.IntegerField(null = True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'ouverture_des_yeux'

class Reponses_verbale(models.Model):
    libelle = models.CharField(max_length=25)
    score   = models.IntegerField(null = True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'reponses_verbale'

class Reponses_motrice(models.Model):
    libelle = models.CharField(max_length=25)
    score   = models.IntegerField(null = True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'reponses_motrice'

class Autres_signe_vie(models.Model):
    libelle = models.CharField(max_length=25)
    reponse = models.CharField(max_length=5)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'autres_signe_vie'

class Mise_en_condition(models.Model):
    scope               = models.CharField(max_length=15, null = True)
    dyn                 = models.CharField(max_length=15, null = True)
    oxy                 = models.CharField(max_length=15, null = True)
    coquille            = models.CharField(max_length=15, null = True)
    barquette           = models.CharField(max_length=15, null = True)
    vvp_kt              = models.CharField(max_length=15, null = True)
    bd                  = models.CharField(max_length=15, null = True)
    bg                  = models.CharField(max_length=15, null = True)
    ktc                 = models.CharField(max_length=15, null = True)
    sonde_gast          = models.CharField(max_length=15, null = True)
    sonde_vest          = models.CharField(max_length=15, null = True)
    collier_cervical    = models.CharField(max_length=15, null = True)
    attelles            = models.CharField(max_length=15, null = True)
    drain_pleural       = models.CharField(max_length=15, null = True)
    autre               = models.CharField(max_length=255, null = True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'mise_en_condition'

class Solutes_drogues(models.Model):
    libelle = models.CharField(max_length=150)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'solutes_drogues'

class Voies_aeriennes(models.Model):
    o2          = models.CharField(max_length=15)
    intubation  = models.CharField(max_length=15)
    sonde       = models.CharField(max_length=15)
    fio2        = models.CharField(max_length=15)
    frequence   = models.CharField(max_length=15)
    vol_courant = models.CharField(max_length=15)
    peep        = models.CharField(max_length=15)
    patient     = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'voies_aeriennes'

class Constant(models.Model):
    heure       = models.CharField(max_length=25)
    poul        = models.CharField(max_length=25)
    TA          = models.CharField(max_length=25)
    FR          = models.CharField(max_length=25)
    spo2_fioo2  = models.CharField(max_length=25)
    temperature = models.CharField(max_length=25)
    glasgow     = models.CharField(max_length=25)
    glycemie    = models.CharField(max_length=25)
    douleur     = models.CharField(max_length=25)
    diurese     = models.CharField(max_length=25)
    commentaire = models.CharField(max_length=155)
    patient     = models.ForeignKey(Patient, on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'constant'



