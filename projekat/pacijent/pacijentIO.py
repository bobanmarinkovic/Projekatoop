import json
datoteka= './datoteke/pacijent.json'

def sacuvaj_pacijente(pacijent):

    with open(datoteka, "w") as f:
        json.dump(pacijent,f)

def ucitaj_pacijente():
    with open(datoteka, "r") as f:
            return json.load(f)

ucitaj_pacijente()