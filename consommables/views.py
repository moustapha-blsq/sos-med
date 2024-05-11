from django.http import HttpResponse
from django.template import loader
from consommables.models import *
from patient_register.models import *
from django.shortcuts import render, redirect

def get_consommable(request):
    all_consommable = Consommable.objects.all()
    context = {'consommables': all_consommable}
    return render(request, 'consommable.html', context)


def addConsommable(request):
    if request.method == 'POST':
        nom_consom = request.POST['nom_consommable']
        Consommable.objects.create(
            libelle = nom_consom
        )
    all_consommable = Consommable.objects.all()
    context = {'consommables': all_consommable}
    #return render(request, 'consommable.html', context)
    return redirect("/consommable/home")

def delete_consommable(request, id):
    consommable = Consommable.objects.get(pk=id)
    nom = consommable.libelle
    supprim = consommable.delete()
    message = ""
    if(supprim):
        message = "Consommable supprimé avec succès"
    all_consommable = Consommable.objects.all()
    context = {'consommables': all_consommable, 'message_alert': message}
    return redirect("/consommable/home")
