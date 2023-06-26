import sqlite3

# Povezivanje sa bazom podataka (kreiranje nove baze ako ne postoji)
conn = sqlite3.connect('ski_baza.db')

# Kreiranje objekta kursora za interakciju sa bazom
cursor = conn.cursor()

# Kreiranje tabele za ski-instruktore
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ski_instruktori (
        id INTEGER PRIMARY KEY,
        ime TEXT,
        prezime TEXT,
        godine INTEGER,
        iskustvo TEXT
    )
''')

# Ubacivanje SKI INSTRUKTORA -----------------------------
cursor.execute('''
    INSERT INTO ski_instruktori (ime, prezime, godine, iskustvo)
    VALUES ('Marko', 'Marković', 35, '10 godina iskustva')
''')
cursor.execute('''
    INSERT INTO ski_instruktori (ime, prezime, godine, iskustvo)
    VALUES ('Ana', 'Jugović', 28, '5 godina iskustva')
''')
cursor.execute('''
    INSERT INTO ski_instruktori (ime, prezime, godine, iskustvo)
    VALUES ('Nikola', 'Nikolić', 40, '15 godina iskustva')
''')

conn.commit()


def izaberi_ski_instruktore():
    """Izaberi sve ski-instruktore iz tabele ski_instruktori."""
    cursor.execute("SELECT * FROM ski_instruktori")
    instruktori = cursor.fetchall()
    return instruktori



def prikazi_ski_instruktore(instruktori):
    """Prikazi detalje o ski-instruktorima."""
    print("Ski Instruktori:")
    for instruktor in instruktori:
        print(instruktor)
    print()



def dodaj_ski_instruktora():
    """Dodaj novog ski instruktora u tabelu ski_instruktori."""
    ime = input("Unesite ime ski instruktora: ")
    prezime = input("Unesite prezime ski instruktora: ")
    godine = input("Unesite godine ski instruktora: ")
    iskustvo = input("Unesite iskustvo ski instruktora: ")

    cursor.execute("INSERT INTO ski_instruktori (ime, prezime, godine, iskustvo) VALUES (?, ?, ?, ?)",
                   (ime, prezime, godine, iskustvo))
    conn.commit()
    print("Ski instruktor uspešno dodat.")

while True:
    print("Opcije:")
    print("1. Prikazi ski instruktore")
    print("2. Dodaj novog ski instruktora")
    print("3. Izlaz")

    izbor = input("Unesite izbor: ")

    if izbor == "1":
        instruktori = izaberi_ski_instruktore()
        prikazi_ski_instruktore(instruktori)

    elif izbor == "2":
        dodaj_ski_instruktora()

    elif izbor == "3":
        break

    else:
        print("Pogrešan unos. Pokušajte ponovo!")