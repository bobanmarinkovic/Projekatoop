from Projekatoop.projekat.korisnik.korisnik import Korisnik

class Pacijent(Korisnik):
    @property
    def LBO(self):
        return self.__LBO

    @LBO.setter
    def LBO(self, LBO):
        self.__LBO = LBO

    @property
    def ReceptPac(self):
        return self.__ReceptPac

    @ReceptPac.setter
    def LBO(self, ReceptPac):
        self.__ReceptPac = ReceptPac

    def __init__(self, JMBG, Ime, Prezime, Datum_rodjenja, LBO, ReceptPac):
        super().__init__(JMBG,Ime,Prezime,Datum_rodjenja),
        self.__LBO= LBO
        self.__ReceptPac=ReceptPac



class Lekar(Korisnik):

    @property
    def Specijalizacija(self):
        return self.__Specijalizacija

    @Specijalizacija.setter
    def Specijalizacija (self, Specijalizacija):
        self.__Specijalizacija = Specijalizacija

    @property
    def ReceptiLekar(self):
        return self.__ReceptiLekar

    @ReceptiLekar.setter
    def ReceptiLekar(self, ReceptiLekar):
        self.__ReceptiLekar = ReceptiLekar

    def __init__(self, JMBG, Ime, Prezime, Datum_rodjenja, Specijalizacija, ReceptiLekar):
        super().__init__(JMBG, Ime, Prezime, Datum_rodjenja)
        self.__Specijalizacija = Specijalizacija
        self.__ReceptiLekar = ReceptiLekar

    def __str__(self):

        return "\n".join([
            super().__str__(),
            "{:10}{}".format("Specijalizacija", self.__Specijalizacija),
            "{:10}{}".format("ReceptiLekar", self.__ReceptiLekar)

        ])

