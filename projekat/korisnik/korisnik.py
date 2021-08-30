class Korisnik:


    @property
    def JMBG(self):
        return self.__JMBG

    @JMBG.setter
    def boja(self, JMBG):
        self.__JMBG = JMBG

    @property
    def Ime(self):
        return self.__Ime

    @Ime.setter
    def Ime(self, Ime):
        self.__Ime = Ime

    @property
    def Prezime(self):
        return self.__Prezime

    @Prezime.setter
    def Prezime(self, Prezime):
        self.__Prezime = Prezime

    @property
    def Datum_rodjenja(self):
        return self.__Datum_rodjenja

    @Datum_rodjenja.setter
    def Datum_rodjenja(self, Datum_rodjenja):
        self.__Datum_rodjenja = Datum_rodjenja

    def __init__(self, JMBG, Ime, Prezime, Datum_rodjenja):
        self.__JMBG = JMBG
        self.__Ime = Ime
        self.__Prezime=Prezime
        self.__Datum_rodjenja=Datum_rodjenja


    def __str__(self):
        return "\n".join([
            "{:10}{}".format("JMBG",self.__JMBG),
            "{:10}{:10}{}".format("Prezime Ime: ",self.__Prezime,self.__Ime),
            "{:10}{}".format("Datum rodjenja: ",self.__Datum_rodjenja)

        ])

    @classmethod
    def prikazi_korisnike(cls, korisnici):
        format_linije = "{:13} {:13} {:13} {:13}"
        print()

        print(format_linije.format("JMBG", "Ime", "Prezime", "Datum rodjenja"))
        print(format_linije.format("*" * 13, "*" * 13, "*" * 13, "*" * 13))

        for korisnik in korisnici:
            print(format_linije.format(
                korisnik.__JMBG,
                korisnik.__Ime,
                korisnik.__Prezime,
                korisnik.__Datum_rodjenja

            ))



