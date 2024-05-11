# Generated by Django 3.0.5 on 2024-05-11 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=150)),
                ('sexe', models.CharField(max_length=10)),
                ('age', models.IntegerField(null=True)),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=50)),
                ('pays_origine', models.CharField(max_length=50)),
                ('ambulancier', models.CharField(max_length=50, null=True)),
                ('origine_appel', models.CharField(max_length=50, null=True)),
                ('motif_appel', models.CharField(max_length=150, null=True)),
                ('lieu_intervention', models.CharField(max_length=50, null=True)),
                ('decision', models.CharField(max_length=150, null=True)),
                ('trajet', models.CharField(max_length=150, null=True)),
                ('numero_ambulance', models.CharField(max_length=25, null=True)),
                ('diagnostique_evoque', models.CharField(max_length=250, null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_valid', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'Patient',
            },
        ),
        migrations.CreateModel(
            name='Voies_aeriennes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o2', models.CharField(max_length=15)),
                ('intubation', models.CharField(max_length=15)),
                ('sonde', models.CharField(max_length=15)),
                ('fio2', models.CharField(max_length=15)),
                ('frequence', models.CharField(max_length=15)),
                ('vol_courant', models.CharField(max_length=15)),
                ('peep', models.CharField(max_length=15)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'voies_aeriennes',
            },
        ),
        migrations.CreateModel(
            name='Solutes_drogues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=150)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'solutes_drogues',
            },
        ),
        migrations.CreateModel(
            name='Reponses_verbale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=25)),
                ('score', models.IntegerField(null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'reponses_verbale',
            },
        ),
        migrations.CreateModel(
            name='Reponses_motrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=25)),
                ('score', models.IntegerField(null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'reponses_motrice',
            },
        ),
        migrations.CreateModel(
            name='Reponse_verbale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'Reponse_verbale',
            },
        ),
        migrations.CreateModel(
            name='Reponse_motrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'Reponse_motrice',
            },
        ),
        migrations.CreateModel(
            name='Ouverture_yeux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'Ouverture_yeux',
            },
        ),
        migrations.CreateModel(
            name='Ouverture_des_yeux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=25)),
                ('score', models.IntegerField(null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'ouverture_des_yeux',
            },
        ),
        migrations.CreateModel(
            name='Mise_en_condition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scope', models.CharField(max_length=15, null=True)),
                ('dyn', models.CharField(max_length=15, null=True)),
                ('oxy', models.CharField(max_length=15, null=True)),
                ('coquille', models.CharField(max_length=15, null=True)),
                ('barquette', models.CharField(max_length=15, null=True)),
                ('vvp_kt', models.CharField(max_length=15, null=True)),
                ('bd', models.CharField(max_length=15, null=True)),
                ('bg', models.CharField(max_length=15, null=True)),
                ('ktc', models.CharField(max_length=15, null=True)),
                ('sonde_gast', models.CharField(max_length=15, null=True)),
                ('sonde_vest', models.CharField(max_length=15, null=True)),
                ('collier_cervical', models.CharField(max_length=15, null=True)),
                ('attelles', models.CharField(max_length=15, null=True)),
                ('drain_pleural', models.CharField(max_length=15, null=True)),
                ('autre', models.CharField(max_length=255, null=True)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'mise_en_condition',
            },
        ),
        migrations.CreateModel(
            name='lesions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(max_length=50, null=True)),
                ('partie_lesion', models.CharField(max_length=25, null=True)),
                ('crane', models.CharField(max_length=50, null=True)),
                ('face', models.CharField(max_length=50, null=True)),
                ('cou', models.CharField(max_length=50, null=True)),
                ('rachis', models.CharField(max_length=50, null=True)),
                ('thorax', models.CharField(max_length=50, null=True)),
                ('abdomen', models.CharField(max_length=50, null=True)),
                ('bassin', models.CharField(max_length=50, null=True)),
                ('msd', models.CharField(max_length=50, null=True)),
                ('msg', models.CharField(max_length=50, null=True)),
                ('mid', models.CharField(max_length=50, null=True)),
                ('mig', models.CharField(max_length=50, null=True)),
                ('autre', models.CharField(max_length=150)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'Lesions',
            },
        ),
        migrations.CreateModel(
            name='Lesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_lesion', models.CharField(max_length=50)),
                ('organe', models.CharField(max_length=50)),
                ('observation', models.CharField(max_length=150)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'Lesion',
            },
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medecin', models.CharField(max_length=100)),
                ('paramedical', models.CharField(max_length=100)),
                ('ambulancier', models.CharField(max_length=100)),
                ('origine_appel', models.CharField(max_length=100)),
                ('motif_appel', models.CharField(max_length=255)),
                ('lieux_intervention', models.CharField(max_length=100)),
                ('decision', models.CharField(max_length=100)),
                ('trajet', models.CharField(max_length=100)),
                ('diagnostique_evoque', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'Intervention',
            },
        ),
        migrations.CreateModel(
            name='Horaires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ht', models.CharField(max_length=15)),
                ('d_base', models.CharField(max_length=15)),
                ('a_lieu', models.CharField(max_length=15)),
                ('d_lieu', models.CharField(max_length=15)),
                ('asr', models.CharField(max_length=15)),
                ('dsr', models.CharField(max_length=15)),
                ('a_base', models.CharField(max_length=15)),
                ('duree', models.CharField(max_length=25)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'Horaires',
            },
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ht', models.CharField(max_length=10)),
                ('d_bae', models.CharField(max_length=10)),
                ('a_lieu', models.CharField(max_length=10)),
                ('d_lieu', models.CharField(max_length=10)),
                ('asr', models.CharField(max_length=10)),
                ('a_base', models.CharField(max_length=10)),
                ('dsr', models.CharField(max_length=10)),
                ('duree', models.CharField(max_length=15)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'Horaire',
            },
        ),
        migrations.CreateModel(
            name='Constant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure', models.CharField(max_length=25)),
                ('poul', models.CharField(max_length=25)),
                ('TA', models.CharField(max_length=25)),
                ('FR', models.CharField(max_length=25)),
                ('spo2_fioo2', models.CharField(max_length=25)),
                ('temperature', models.CharField(max_length=25)),
                ('glasgow', models.CharField(max_length=25)),
                ('glycemie', models.CharField(max_length=25)),
                ('douleur', models.CharField(max_length=25)),
                ('diurese', models.CharField(max_length=25)),
                ('commentaire', models.CharField(max_length=155)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'constant',
            },
        ),
        migrations.CreateModel(
            name='Consommable_utilise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_consommable', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=5)),
                ('charges', models.CharField(max_length=25)),
                ('fnc', models.CharField(max_length=25)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'consommable_utilise',
            },
        ),
        migrations.CreateModel(
            name='Autres_signe_vie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=25)),
                ('reponse', models.CharField(max_length=5)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'autres_signe_vie',
            },
        ),
        migrations.CreateModel(
            name='autre_signe_de_vie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fourmillement_extremite', models.CharField(max_length=5)),
                ('mouvement_de_ms', models.CharField(max_length=5)),
                ('mouvement_de_mi', models.CharField(max_length=5)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_register.Patient')),
            ],
            options={
                'db_table': 'autre_signe_vie',
            },
        ),
    ]
