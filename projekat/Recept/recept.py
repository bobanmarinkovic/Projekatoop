from Projekatoop.projekat.pacijent.pacijent import Lekar
from Projekatoop.projekat.pacijent.pacijent import Pacijent
from Projekatoop.projekat.lek.lek import Lek


class Recept():


    @property
    def ReceptPac(self):
        return self.__ReceptPac

    @ReceptPac.setter
    def ReceptPac(self, ReceptPac):
        self.__ReceptPac = ReceptPac

    @property
    def Datum_izdavanja(self):
        return self.__Datum_izdavanja

    @Datum_izdavanja.setter
    def Datum_izdavanja(self, Datum_izdavanja):
        self.__Datum_izdavanja = Datum_izdavanja

    @property
    def Izvestaj(self):
        return self.__Izvestaj

    @Izvestaj.setter
    def Izvestaj(self, Izvestaj):
        self.__Izvestaj = Izvestaj

    @property
    def ReceptLekar(self):
        return self.__ReceptLekar

    @ReceptLekar.setter
    def ReceptLekar(self, ReceptLekar):
        self.__ReceptLekar = ReceptLekar

    @property
    def ReceptLek(self):
        return self.__ReceptLek

    @ReceptLek.setter
    def ReceptLek(self, ReceptLek):
        self.__ReceptLek = ReceptLek

    @property
    def Kolicina(self):
        return self.__Kolicina

    @Kolicina.setter
    def Kolicina(self, Kolicina):
        self.__Kolicina = Kolicina

    def __init__(self, ReceptPac, Datum_izdavanja, Izvestaj, ReceptLekar, ReceptLek, Kolicina):
        self.__ReceptPac = ReceptPac
        self.__Datum_izdavanja = Datum_izdavanja
        self.__Izvestaj = Izvestaj
        self.__ReceptLekar = ReceptLekar
        self.__ReceptLek = ReceptLek
        self.__Kolicina = Kolicina

    def __str__(self):
        format_linije = "{} {}"
        return "\n".join([
            "{:10}{:10}{}".format("Pacijent: ", self.__ReceptPac.Ime, self.__ReceptPac.Prezime),
            "{:10}{}".format("Datum i vreme : ", self.__Datum_izdavanja),
            "{:10}{}".format("Izveštaj : ", self.__Izvestaj),
            "{:10}{:10}{}".format("Lekar: ",self.__ReceptLekar.Ime, self.__ReceptLekar.Prezime),
            "{:10}{}".format("Lek: ", self.__ReceptLek.naziv),
            "{:10}{}".format("Količina: ", self.__Kolicina)
        ])
