import sqlite3

# Povezivanje sa bazom podataka (kreiranje nove baze ako ne postoji)
conn = sqlite3.connect('skiing_database.db')

# Kreiranje objekta kursora za interakciju sa bazom
cursor = conn.cursor()

# Kreiranje tabele za ski-centre
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ski_centri (
        id INTEGER PRIMARY KEY,
        ime TEXT,
        lokacija TEXT,
        tezina TEXT,
        broj_staza INTEGER,
        sezona_otvaranja TEXT
    )
''')

# Ubacivanje ski centara u tabelu
cursor.execute('''
    INSERT INTO ski_centri (ime, lokacija, tezina, broj_staza, sezona_otvaranja)
    VALUES ('Aspen Mountain', 'Aspen, Kolorado', 'Napredno', 76, 'Novembar - April')
''')
cursor.execute('''
    INSERT INTO ski_centri (ime, lokacija, tezina, broj_staza, sezona_otvaranja)
    VALUES ('Whistler Blackcomb', 'Whistler, Britanska Kolumbija', 'Napredno', 200, 'Novembar - Maj')
''')
cursor.execute('''
    INSERT INTO ski_centri (ime, lokacija, tezina, broj_staza, sezona_otvaranja)
    VALUES ('St. Anton am Arlberg', 'St. Anton, Austrija', 'Ekspert', 340, 'Decembar - April')
''')

conn.commit()


def izaberi_ski_centre():
    """Izaberi sve ski-centre iz tabele ski_centri."""
    cursor.execute("SELECT * FROM ski_centri")
    centri = cursor.fetchall()
    return centri


def azuriraj_ime_ski_centra(id_centra, novo_ime):
    """Azuriraj ime ski-centra sa datim ID-jem."""
    cursor.execute("UPDATE ski_centri SET ime = ? WHERE id = ?", (novo_ime, id_centra))
    conn.commit()


def obrisi_ski_centar(id_centra):
    """Obrisi ski-centar sa datim ID-jem iz tabele ski_centri."""
    cursor.execute("DELETE FROM ski_centri WHERE id = ?", (id_centra,))
    conn.commit()


def prikazi_ski_centre(centri):
    """Prikazi detalje o ski-centrima."""
    print("Ski Centri:")
    for centar in centri:
        print(centar)
    print()



# Glavna petlja za interakciju sa korisnikom
while True:
    print("Opcije:")
    print("1. Prikazi ski centre")
    print("2. Azuriraj ime ski centra")
    print("3. Obrisi ski centar")
    print("4. Izlaz")

    izbor = input("Unesite izbor: ")

    if izbor == "1":
        centri = izaberi_ski_centre()
        prikazi_ski_centre(centri)

    elif izbor == "2":
        centri = izaberi_ski_centre()
        prikazi_ski_centre(centri)

        id_centra = input("Unesite ID ski centra koji želite ažurirati: ")
        novo_ime = input("Unesite novo ime za ski centar: ")

        azuriraj_ime_ski_centra(id_centra, novo_ime)
        print("Ime ski centra uspješno ažurirano.")

        centri = izaberi_ski_centre()
        prikazi_ski_centre(centri)

    elif izbor == "3":
        centri = izaberi_ski_centre()
        prikazi_ski_centre(centri)

        id_centra = input("Unesite ID ski centra koji želite obrisati: ")

        obrisi_ski_centar(id_centra)
        print("Ski centar uspešno obrisan.")

        centri = izaberi_ski_centre()
        prikazi_ski_centre(centri)

    elif izbor == "4":
        break

    else:
        print("Nevažeći izbor. Molimo pokušajte ponovo.")