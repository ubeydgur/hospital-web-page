from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password




def index(request):
    return render(request, 'page/index.html')
def patient(request):
    return render(request,  'page/patient.html')

def doctor(request):
    return render(request, 'page/doctor.html')

def admins(request):
    return render(request, 'page/admins.html')


def patient_create(request):
    return render(request, 'page/patient_create_account.html')

def run_custom_query(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM patients;")
        columns = [col[0] for col in cursor.description]  # Sütun adlarını al
        rows = cursor.fetchall()
        data = [dict(zip(columns, row)) for row in rows]  # Satırları sözlük olarak biçimlendir

    # JSON olarak döndür
    return JsonResponse(data, safe=False)

def login_process(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # SQL sorgusu ile kullanıcıyı bul
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM patients WHERE firstname = %s", [email])
            row = cursor.fetchone()

        if row is not None:
            print(password)
            if password == row[7]:
                # Kullanıcı doğrulandı
                return render(request, 'page/index.html')
            else:
                return HttpResponse("Hatalı şifre.")
        else:
            return HttpResponse("Belirtilen e-posta adresine sahip bir kullanıcı bulunamadı.")
    else:
        return HttpResponse("Bu URL sadece POST istekleriyle çalışır.")



