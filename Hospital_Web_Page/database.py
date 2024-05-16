import sqlite3

conn = sqlite3.connect('hospital.db')

c = conn.cursor()

'''
c.execute("""CREATE TABLE patients(
    patientID INTEGER PRIMARY KEY NOT NULL, 
    firstname TEXT NOT NULL,
    surname TEXT NOT NULL,
    birth TEXT NOT NULL,
    gender TEXT NOT NULL,
    phone INTEGER NOT NULL,
    address TEXT NOT NULL,
    password TEXT NOT NULL
    )""")

c.execute("""CREATE TABLE doctors(
    doctorID INTEGER PRIMARY KEY NOT NULL, 
    firstname TEXT NOT NULL,
    surname TEXT NOT NULL,
    specialty TEXT NOT NULL,
    workplace TEXT NOT NULL,
    password TEXT NOT NULL
    )""")

c.execute("""CREATE TABLE admins(
    adminID INTEGER PRIMARY KEY NOT NULL, 
    password TEXT NOT NULL
    )""")

c.execute("""CREATE TABLE appointment(
    appointmentID INTEGER PRIMARY KEY NOT NULL, 
    date TEXT NOT NULL,
    time INTEGER NOT NULL,
    doctorID INTEGER,
    patientID INTEGER,
    FOREIGN KEY (patientID) REFERENCES patients(patientID),
    FOREIGN KEY (doctorID) REFERENCES doctors(doctorID)
    )""")

c.execute("""CREATE TABLE report(
    reportID INTEGER PRIMARY KEY NOT NULL, 
    date TEXT NOT NULL,
    link TEXT NOT NULL,
    patientID INTEGER,
    FOREIGN KEY (patientID) REFERENCES patients(patientID)
    )""")
'''
#c.execute("INSERT INTO patients VALUES ('1', 'onur', 'varol', '02.11.2001', 'M', '055090943357', 'address', '1')") # tabloya veri ekleme

#c.execute("INSERT INTO admins VALUES ('0', '1')")


#c.execute("PRAGMA table_info(patients)") # sütunları döndürür

#c.execute("SELECT * FROM patients")
#print(c.fetchall())

conn.commit()
conn.close()