import json
datoteka= './datoteke/lekar.json'

def sacuvaj_lekara(lekar):

    with open(datoteka, "w") as f:
        json.dump(lekar,f)

def ucitaj_lekara():
    with open(datoteka, "r") as f:
            return json.load(f)

ucitaj_lekara()