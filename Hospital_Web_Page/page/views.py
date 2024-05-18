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
                request.session['patient_id'] = id
                request.session['appointment_id'] = id
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

def patient_index(request):
    return render(request, 'page/patient_index.html')

def doctor_index(request):
    return render(request, 'page/doctor_index.html')

def patient_table_admin(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM patients")
        books = cursor.fetchall()
    return render(request, 'page/patient_table_admin.html', {'books': books})

def doctor_table_admin(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM doctors")
        books = cursor.fetchall()
    return render(request, 'page/doctor_table_admin.html', {'books': books})

def appointment_table_admin(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM appointment")
        books = cursor.fetchall()
    return render(request, 'page/appointment_table_admin.html', {'books': books})

def report_table_admin(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM report")
        books = cursor.fetchall()
    return render(request, 'page/report_table_admin.html', {'books': books})

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


def create_patient_admin(request):
    if request.method == 'POST':
        action = request.POST.get('action')
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

        if action == 'create_user':
            if row is None:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO patients VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                   [id, firstname, surname, birth, gender, phone, address, password])

                return redirect ('patient_table_admin')
            else:
                return HttpResponse("Bu ID zaten kullanımda!")

        elif action == 'update_patient':
            if row is None:
                return HttpResponse("Bu ID bulunamadı")
            else:
                with connection.cursor() as cursor:
                    cursor.execute("""UPDATE patients SET 
                                    firstname = COALESCE(NULLIF(%s, ''), firstname),
                                    surname = COALESCE(NULLIF(%s, ''), surname),
                                    birth = COALESCE(NULLIF(%s, ''), birth),
                                    gender = COALESCE(NULLIF(%s, ''), gender),
                                    phone = COALESCE(NULLIF(%s, ''), phone),
                                    address = COALESCE(NULLIF(%s, ''), address),
                                    password = COALESCE(NULLIF(%s, ''), password) WHERE patientID = %s""",
                                   [firstname, surname, birth, gender, phone, address, password, id])
                return redirect('patient_table_admin')

def delete_patient_admin(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        # SQL silme ifadesi
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM patients WHERE patientID = %s", [patient_id])
        return redirect('patient_table_admin')


def create_report_admin(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        id = request.POST.get('id')
        date = request.POST.get('date')
        link = request.POST.get('link')
        tckn = request.POST.get('tckn')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM report WHERE reportID = %s", [id])
            row = cursor.fetchone()

        if action == 'create_report':
            if row is None:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO report VALUES (%s, %s, %s, %s)",
                                   [id, date, link, tckn])

                return redirect ('report_table_admin')
            else:
                return HttpResponse("Bu ID zaten kullanımda!")

        elif action == 'update_report':
            if row is None:
                return HttpResponse("Bu ID bulunamadı")
            else:
                with connection.cursor() as cursor:
                    cursor.execute("""UPDATE report SET 
                                    date = COALESCE(NULLIF(%s, ''), date),
                                    link = COALESCE(NULLIF(%s, ''), link),
                                    patientID = COALESCE(NULLIF(%s, ''), patientID) WHERE reportID = %s""",
                                   [date, link, tckn, id])
                return redirect('report_table_admin')

def delete_report_admin(request):
    if request.method == 'POST':
        report_id = request.POST.get('report_id')
        # SQL silme ifadesi
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM report WHERE reportID = %s", [report_id])
        return redirect('report_table_admin')


def create_doctor_admin(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        id = request.POST.get('id')
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        specialty = request.POST.get('specialty')
        workplace = request.POST.get('workplace')
        password = request.POST.get('password')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM doctors WHERE doctorID = %s", [id])
            row = cursor.fetchone()

        if action == 'create_doctor':
            if row is None:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO doctors VALUES (%s, %s, %s, %s, %s, %s)",
                                   [id, firstname, surname, specialty, workplace, password])

                return redirect ('doctor_table_admin')
            else:
                return HttpResponse("Bu ID zaten kullanımda!")

        elif action == 'update_doctor':
            if row is None:
                return HttpResponse("Bu ID bulunamadı")
            else:
                with connection.cursor() as cursor:
                    cursor.execute("""UPDATE doctors SET 
                                    firstname = COALESCE(NULLIF(%s, ''), firstname),
                                    surname = COALESCE(NULLIF(%s, ''), surname),
                                    specialty = COALESCE(NULLIF(%s, ''), specialty),
                                    workplace = COALESCE(NULLIF(%s, ''), workplace),
                                    password = COALESCE(NULLIF(%s, ''), password) WHERE doctorID = %s""",
                                   [firstname, surname, specialty, workplace, password, id])
                return redirect('doctor_table_admin')

def delete_doctor_admin(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        # SQL silme ifadesi
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM doctors WHERE doctorID = %s", [doctor_id])
        return redirect('doctor_table_admin')


def create_appointment_admin(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        id = request.POST.get('id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        doctorid = request.POST.get('doctorid')
        patientid = request.POST.get('patientid')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM appointment WHERE appointmentID = %s", [id])
            row = cursor.fetchone()

        if action == 'create_appointment':
            if row is None:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO appointment VALUES (%s, %s, %s, %s, %s)",
                                   [id, date, time, doctorid, patientid])

                return redirect ('appointment_table_admin')
            else:
                return HttpResponse("Bu ID zaten kullanımda!")

        elif action == 'update_appointment':
            if row is None:
                return HttpResponse("Bu ID bulunamadı")
            else:
                with connection.cursor() as cursor:
                    cursor.execute("""UPDATE appointment SET 
                                    date = COALESCE(NULLIF(%s, ''), date),
                                    time = COALESCE(NULLIF(%s, ''), time),
                                    doctorID = COALESCE(NULLIF(%s, ''), doctorID),
                                    patientID = COALESCE(NULLIF(%s, ''), patientID) WHERE appointmentID = %s""",
                                   [date, time, doctorid, patientid, id])
                return redirect('appointment_table_admin')

def delete_appointment_admin(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        # SQL silme ifadesi
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM appointment WHERE appointmentID = %s", [appointment_id])
        return redirect('appointment_table_admin')



def report_table_patient(request):
    patient_id = request.session.get('patient_id')
    if patient_id is None:
        return HttpResponse("Giriş yapmalısınız.")

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM report WHERE patientID = %s", [patient_id])
        books = cursor.fetchall()
    return render(request, 'page/report_table_patient.html', {'books': books})

def create_report_patient(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        id = request.POST.get('id')
        date = request.POST.get('date')
        link = request.POST.get('link')
        tckn = request.session.get('patient_id')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM report WHERE reportID = %s", [id])
            row = cursor.fetchone()

        if action == 'create_report':
            if row is None:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO report VALUES (%s, %s, %s, %s)",
                                   [id, date, link, tckn])

                return redirect ('report_table_patient')
            else:
                return HttpResponse("Bu ID zaten kullanımda!")

        elif action == 'update_report':
            if row is None:
                return HttpResponse("Bu ID bulunamadı")
            else:
                with connection.cursor() as cursor:
                    cursor.execute("""UPDATE report SET 
                                    date = COALESCE(NULLIF(%s, ''), date),
                                    link = COALESCE(NULLIF(%s, ''), link),
                                    patientID = COALESCE(NULLIF(%s, ''), patientID) WHERE reportID = %s""",
                                   [date, link, tckn, id])
                return redirect('report_table_patient')

def delete_report_patient(request):
    if request.method == 'POST':
        report_id = request.POST.get('report_id')

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM report WHERE reportID = %s", [report_id])
        return redirect('report_table_patient')


def appointment_table_patient(request):
    patient_id = request.session.get('patient_id')
    if patient_id is None:
        return HttpResponse("Giriş yapmalısınız.")

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM appointment WHERE patientID = %s", [patient_id])
        books = cursor.fetchall()
    return render(request, 'page/appointment_table_patient.html', {'books': books})

def update_appointment_patient(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        id = request.POST.get('id')
        date = request.POST.get('date')
        time = request.POST.get('time')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM appointment WHERE appointmentID = %s", [id])
            row = cursor.fetchone()

        if action == 'update_appointment':
            if row is None:
                return HttpResponse("Bu ID bulunamadı")
            else:
                with connection.cursor() as cursor:
                    cursor.execute("""UPDATE appointment SET 
                                    date = COALESCE(NULLIF(%s, ''), date),
                                    time = COALESCE(NULLIF(%s, ''), time) WHERE appointmentID = %s""",
                                   [date, time, id])
                return redirect('appointment_table_patient')

def delete_appointment_patient(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')

        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM appointment WHERE appointmentID = %s", [appointment_id])
        return redirect('appointment_table_patient')

def doctor_table_patient(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM doctors")
        books = cursor.fetchall()
    return render(request, 'page/appointment_make_patient.html', {'books': books})

def doctor_select_patient(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        request.session['doctor_id'] = doctor_id
        return render(request, 'page/appointment_info_patient.html')
    else:
        return HttpResponse("Bu URL sadece POST istekleriyle çalışır.")

def create_appointment_patient(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        doctor_id = request.session.get('doctor_id')
        patient_id = request.session.get('patient_id')

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM appointment WHERE appointmentID = %s", [id])
            row = cursor.fetchone()

        if row is None:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO appointment VALUES (%s, %s, %s, %s, %s)",
                               [id, date, time, doctor_id, patient_id])

            return redirect ('patient_index')
        else:
            return HttpResponse("Bu ID zaten kullanımda!")