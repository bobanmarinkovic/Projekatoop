import json
datoteka= './datoteke/korisnici.json'

def sacuvaj_korisnike(korisnik):

    with open(datoteka, "w") as f:
        json.dump(korisnik,f)

def ucitaj_korisnike():
    with open(datoteka, "r") as f:
            return json.load(f)

ucitaj_korisnike()