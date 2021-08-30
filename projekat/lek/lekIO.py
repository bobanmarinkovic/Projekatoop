import json
datoteka= './datoteke/lek.json'

def sacuvaj_lek(lek):

    with open(datoteka, "w") as f:
        json.dump(lek,f)

def ucitaj_lek():
    with open(datoteka, "r") as f:
            return json.load(f)

ucitaj_lek()