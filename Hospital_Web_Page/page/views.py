from django.http import HttpResponse
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages


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

def login_patient(request):
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
                return render(request, 'page/patient_index.html')
            else:
                return HttpResponse("Hatalı şifre.")
        else:
            return HttpResponse("Belirtilen e-posta adresine sahip bir kullanıcı bulunamadı.")
    else:
        return HttpResponse("Bu URL sadece POST istekleriyle çalışır.")

def login_admin(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('password')

        # SQL sorgusu ile kullanıcıyı bul
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM admins WHERE adminID = %s", [id])
            row = cursor.fetchone()

        if row is not None:
            if password == row[1]:
                # Kullanıcı doğrulandı
                return render(request, 'page/admin_index.html')
            else:
                return HttpResponse("Hatalı şifre.")
        else:
            return HttpResponse("Belirtilen e-posta adresine sahip bir kullanıcı bulunamadı.")
    else:
        return HttpResponse("Bu URL sadece POST istekleriyle çalışır.")

def login_doctor(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        password = request.POST.get('password')

        # SQL sorgusu ile kullanıcıyı bul
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM doctors WHERE doctorID = %s", [id])
            row = cursor.fetchone()

        if row is not None:
            if password == row[5]:
                # Kullanıcı doğrulandı
                return render(request, 'page/doctor_index.html')
            else:
                return HttpResponse("Hatalı şifre.")
        else:
            return HttpResponse("Belirtilen e-posta adresine sahip bir kullanıcı bulunamadı.")
    else:
        return HttpResponse("Bu URL sadece POST istekleriyle çalışır.")


def admin_index(request):
    return render(request, 'page/admin_index.html')


def table_patient(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM patients")
        books = cursor.fetchall()
    return render(request, 'page/patient_table.html', {'books': books})

def table_doctor(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM doctors")
        books = cursor.fetchall()
    return render(request, 'page/doctor_table.html', {'books': books})

def table_appointment(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM appointment")
        books = cursor.fetchall()
    return render(request, 'page/appointment_table.html', {'books': books})

def table_report(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM report")
        books = cursor.fetchall()
    return render(request, 'page/report_table.html', {'books': books})

def create_patient(request):
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


