from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from patient_register.models import *
from django.shortcuts import render, redirect


def login_user(request):
    if request.method == 'POST':
        user = request.POST['username']
        pw   = request.POST['password']
        user = authenticate(request, username = user, password = pw)

        if user is not None:
            login(request, user)
            template = loader.get_template('home.html')
            all_patients = Patient.objects.all()
            #patient_count = all_patients.count()
            context = {'patients': all_patients}
            return render(request, 'home.html', context)
        
        else:
            msg = "User ou mot de passe incorrect"
            context = {'message': msg}
            return render(request, 'index.html', context)


def logout_user(request):
    logout(request)
    return redirect("patient_register:index")