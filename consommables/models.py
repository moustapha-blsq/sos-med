from django.db import models

class Consommable(models.Model):
    libelle = models.CharField(max_length=150)
    class Meta:
        db_table = 'Consommables'
