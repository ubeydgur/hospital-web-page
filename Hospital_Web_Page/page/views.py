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
        id = request.POST.get('id')
        password = request.POST.get('password')

        # SQL sorgusu ile kullanıcıyı bul
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM patients WHERE patientID = %s", [id])
            row = cursor.fetchone()

        if row is not None:
            if password == row[7]:
                # Kullanıcı doğrulandı
                return render(request, 'page/index.html')
            else:
                return HttpResponse("Hatalı şifre.")
        else:
            return HttpResponse("Belirtilen e-posta adresine sahip bir kullanıcı bulunamadı.")
    else:
        return HttpResponse("Bu URL sadece POST istekleriyle çalışır.")

def create_user(request):
    if request.method == 'POST':
        # Formdan gelen verileri al
        id = request.POST.get('id')
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        birth = request.POST.get('birth')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM patients WHERE patientID = %s", [id])
            row = cursor.fetchone()

        if row is None:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO patients VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                               [id, firstname, surname, birth, gender, phone, address, password])

            # Başarıyla eklendi mesajı döndür
            return HttpResponse("Yeni kullanıcı başarıyla eklendi!")
        else:
            return HttpResponse("Bu ID zaten kullanımda!")
    else:
        return HttpResponse("Bu URL sadece POST istekleriyle çalışır.")


