import sqlite3

conn = sqlite3.connect('hospital.db')

c = conn.cursor()

'''c.execute("""CREATE TABLE patients(
    patientID INTEGER PRIMARY KEY NOT NULL, 
    firstname TEXT NOT NULL,
    surname TEXT NOT NULL,
    birth TEXT NOT NULL,
    gender TEXT NOT NULL,
    phone INTEGER NOT NULL,
    address TEXT NOT NULL,
    password TEXT NOT NULL
    )""")
'''

#c.execute("INSERT INTO patients VALUES ('0', 'ubeyd', 'gur', '05.04.2003', 'M', '05511643357', 'address', '1')") # tabloya veri ekleme

#c.execute("PRAGMA table_info(patients)") # sütunları döndürür

#c.execute("SELECT * FROM patients")
#print(c.fetchall())

conn.commit()
conn.close()