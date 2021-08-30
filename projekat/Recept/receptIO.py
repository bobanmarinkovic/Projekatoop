import json
datoteka= './datoteke/recept.json'

def sacuvaj_recepte(recept):

    with open(datoteka, "w") as f:
        json.dump(recept,f)

def ucitaj_recepte():
    with open(datoteka, "r") as f:
            return json.load(f)

