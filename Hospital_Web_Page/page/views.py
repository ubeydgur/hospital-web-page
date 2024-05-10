from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'page/index.html')
def patient(request):
    return render(request,  'page/patient.html')

def doctor(request):
    return render(request, 'page/doctor.html')

def admins(request):
    return render(request, 'page/admins.html')