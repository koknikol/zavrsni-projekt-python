import sqlite3

# Povezivanje sa bazom podataka (kreiranje nove baze ako ne postoji)
conn = sqlite3.connect('ski_baza.db')

# Kreiranje objekta kursora za interakciju sa bazom
cursor = conn.cursor()


# Kreiranje tabele za iznajmljivanje opreme
cursor.execute('''
    CREATE TABLE IF NOT EXISTS iznajmljivanje_opreme (
        id INTEGER PRIMARY KEY,
        ime_klijenta TEXT,
        oprema TEXT,
        datum_iznajmljivanja TEXT,
        datum_vracanja TEXT
    )
''')

cursor.execute('''
    INSERT INTO iznajmljivanje_opreme (ime_klijenta, oprema, datum_iznajmljivanja, datum_vracanja)
    VALUES ('Milica', 'Skije', '02.01.2023', '10.01.2023')
''')
cursor.execute('''
    INSERT INTO iznajmljivanje_opreme (ime_klijenta, oprema, datum_iznajmljivanja, datum_vracanja)
    VALUES ('Stefan', 'Snowboard', '11.01.2023', '22.01.2023')
''')
cursor.execute('''
    INSERT INTO iznajmljivanje_opreme (ime_klijenta, oprema, datum_iznajmljivanja, datum_vracanja)
    VALUES ('Jovana', 'Skije', '05.02.2023', '19.02.2023')
''')

def izaberi_iznajmljivanja_opreme():
    """Izaberi sva iznajmljivanja opreme iz tabele iznajmljivanje_opreme."""
    cursor.execute("SELECT * FROM iznajmljivanje_opreme")
    iznajmljivanja = cursor.fetchall()
    return iznajmljivanja


def prikazi_iznajmljivanja_opreme(iznajmljivanja):
    """Prikazi detalje o iznajmljivanju opreme."""
    print("Iznajmljivanje opreme:")
    for iznajmljivanje in iznajmljivanja:
        print(iznajmljivanje)
    print()

def dodaj_iznajmljivanje_opreme():
    """Dodaj novo iznajmljivanje opreme u tabelu iznajmljivanje_opreme."""
    ime_klijenta = input("Unesite ime klijenta: ")
    oprema = input("Unesite vrstu iznajmljene opreme: ")
    datum_iznajmljivanja = input("Unesite datum iznajmljivanja (DD-MM-YYYY): ")
    datum_vracanja = input("Unesite datum vraćanja (DD-MM-YYYY): ")

    cursor.execute("INSERT INTO iznajmljivanje_opreme (ime_klijenta, oprema, datum_iznajmljivanja, datum_vracanja) "
                   "VALUES (?, ?, ?, ?)", (ime_klijenta, oprema, datum_iznajmljivanja, datum_vracanja))
    conn.commit()
    print("Iznajmljivanje opreme uspešno dodato.")


def obrisi_klijenta(id_iznajmljivanja):
    """Izbriši iznajmljivanje opreme iz tabele iznajmljivanje_opreme."""
    cursor.execute("DELETE FROM iznajmljivanje_opreme WHERE id = ?", (id_iznajmljivanja,))
    conn.commit()
    print("Iznajmljivanje opreme uspešno izbrisano.")


while True:
    print("Opcije:")
    print("1. Prikazi sva iznajmljivanja opreme")
    print("2. Dodaj novo iznajmljivanje opreme")
    print("3. Obrisi klijenta")
    print("4. Izlaz")

    izbor = input("Unesite izbor: ")

    if izbor == "1":
        iznajmljivanja = izaberi_iznajmljivanja_opreme()
        prikazi_iznajmljivanja_opreme(iznajmljivanja)

    elif izbor == "2":
        dodaj_iznajmljivanje_opreme()

    elif izbor == "3":
        iznajmljivanja = izaberi_iznajmljivanja_opreme()
        prikazi_iznajmljivanja_opreme(iznajmljivanja)

        id_iznajmljivanja = input("Unesite ID klijenta kojeg želite obrisati!")

        obrisi_klijenta(id_iznajmljivanja)
        # print("Klijent uspješno obrisan!")

        iznajmljivanja = izaberi_iznajmljivanja_opreme()
        prikazi_iznajmljivanja_opreme(iznajmljivanja)

    elif izbor == "4":
        break

    else:
        print("Pogrešan unos. Pokušaj ponovo!")
