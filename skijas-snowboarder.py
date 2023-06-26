import sqlite3

# Povezivanje sa bazom podataka (kreiranje nove baze ako ne postoji)
conn = sqlite3.connect('ski_baza.db')

# Kreiranje objekta kursora za interakciju sa bazom
cursor = conn.cursor()

# Kreiranje tabele za skijaše/snowboardere
cursor.execute('''
    CREATE TABLE IF NOT EXISTS skijasi_snowboarderi (
        id INTEGER PRIMARY KEY,
        ime TEXT,
        prezime TEXT,
        godine INTEGER,
        vrsta_aktivnosti TEXT
    )
''')

# Ubacivanje SKIJASA / SNOWBOARDERA
cursor.execute('''INSERT INTO skijasi_snowboarderi (ime, prezime, godine, vrsta_aktivnosti)
                  VALUES ('Marko', 'Markovic', 25, 'ski')''')
cursor.execute('''INSERT INTO skijasi_snowboarderi (ime, prezime, godine, vrsta_aktivnosti)
                  VALUES ('Ana', 'Jovanovic', 28, 'snowboard')''')
cursor.execute('''INSERT INTO skijasi_snowboarderi (ime, prezime, godine, vrsta_aktivnosti)
                  VALUES ('Nikola', 'Petrovic', 32, 'ski')''')
cursor.execute('''INSERT INTO skijasi_snowboarderi (ime, prezime, godine, vrsta_aktivnosti)
                  VALUES ('Jovana', 'Stojanovic', 27, 'snowboard')''')


def izaberi_skijase_snowboardere():
    """Izaberi sve skijaše/snowboardere iz tabele skijasi_snowboarderi."""
    cursor.execute("SELECT * FROM skijasi_snowboarderi")
    skijasi = cursor.fetchall()
    return skijasi


def prikazi_skijase_snowboardere(skijasi):
    """Prikazi detalje o skijašima/snowboarderima."""
    print("Skijaši/Snowboarderi:")
    for skijas in skijasi:
        print(skijas)
    print()


def dodaj_skijasa_snowboardera():
    """Dodaj novog skijaša/snowboardera u tabelu skijasi_snowboarderi."""
    ime = input("Unesite ime skijaša/snowboardera: ")
    prezime = input("Unesite prezime skijaša/snowboardera: ")
    godine = input("Unesite godine skijaša/snowboardera: ")
    vrsta_aktivnosti = input("Unesite vrstu aktivnosti (ski/snowboard): ")

    cursor.execute("INSERT INTO skijasi_snowboarderi (ime, prezime, godine, vrsta_aktivnosti) "
                   "VALUES (?, ?, ?, ?)", (ime, prezime, godine, vrsta_aktivnosti))
    conn.commit()
    print("Skijaš/Snowboarder uspješno dodat.")


def azuriraj_skijasa_snowboardera(id_skijasa, novo_ime):
    """Azuriraj ime ski-centra sa datim ID-jem."""
    cursor.execute("UPDATE ski_centri SET ime = ? WHERE id = ?", (novo_ime, id_skijasa))
    conn.commit()
    print("Skijaš uspješno izmijenjen!")


def obrisi_skijasa_snowboardera(id_skijasa):
    """Izbriši skijaša/snowboardera iz tabele."""
    cursor.execute("DELETE FROM skijasi_snowboarderi WHERE id = ?", (id_skijasa,))
    conn.commit()
    print("Skijaš/Snowboarder uspješno izbrisan.")

while True:
    print("Opcije:")
    print("1. Prikazi skijaše/snowboardere")
    print("2. Dodaj novog skijaša/snowboardera")
    print("3. Obriši skijaša/snowboardera")
    print("4. Ažuriraj skijaša/snowboardera")
    print("5. Izlaz")
    print()

    izbor = input("Unesite izbor: ")
    if izbor == "1":
        skijasi = izaberi_skijase_snowboardere()
        prikazi_skijase_snowboardere(skijasi)

    elif izbor == "2":
        dodaj_skijasa_snowboardera()

    elif izbor == "3":
        skijasi = izaberi_skijase_snowboardere()
        prikazi_skijase_snowboardere(skijasi)

        id_skijasa = input("Unesite ID skijaša/snowboardera kojeg želite obrisati: ")

        obrisi_skijasa_snowboardera(id_skijasa)
        # print("Skijaš/snowboarder uspješno izbrisan!")

        skijasi = izaberi_skijase_snowboardere()
        prikazi_skijase_snowboardere(skijasi)

    elif izbor == "4":
        skijasi = izaberi_skijase_snowboardere()
        prikazi_skijase_snowboardere(skijasi)

        id_skijasa = input("Unesite ID skijaša/snowboardera kojeg želite ažurirati!")
        novo_ime = input("Unesite ime skijaša/snowboardera")

        azuriraj_skijasa_snowboardera(id_skijasa, novo_ime)
        # print("Skijas/snowboarder uspješno izmjenjen")

        skijasi = izaberi_skijase_snowboardere()
        prikazi_skijase_snowboardere(skijasi)

    elif izbor == "4":
        break

    else:
        print("Pogrešan unos. Pokušaj ponovo od 1 do 4!")
