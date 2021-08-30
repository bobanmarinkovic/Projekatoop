class Lek:

    @property
    def JKL(self):
        return self.__JKL

    @JKL.setter
    def JKL(self, JKL):
        self.__JKL = JKL

    @property
    def Naziv(self):
        return self.__Naziv

    @Naziv.setter
    def Naziv(self, Naziv):
        self.__Naziv = Naziv

    @property
    def Proizvodjac(self):
        return self.__Proizvodjac

    @Proizvodjac.setter
    def Proizvodjac(self, Proizvodjac):
        self.__Proizvodjac = Proizvodjac

    @property
    def Tip_leka(self):
        return self.__Tip_leka

    @Tip_leka.setter
    def Tip_leka(self, Tip_leka):
        self.__Tip_leka = Tip_leka

    @property
    def ReceptLek(self):
        return self.__ReceptLek

    @ReceptLek.setter
    def ReceptLek(self, ReceptLek):
        self.__ReceptLek = ReceptLek

    def __init__(self, JKL, Naziv, Proizvodjac, Tip_leka, ReceptLek):
        self.__JKL = JKL
        self.__Naziv = Naziv
        self.__Proizvodjac = Proizvodjac
        self.__Tip_leka = Tip_leka
        self.__ReceptLek = ReceptLek

    def __str__(self):

        return "\n".join([
            "{:10}{}".format("JKL:", self.__JKL),
            "{:10}{}".format("Naziv: ", self.__Naziv),
            "{:10}{}".format("Tip Leka: ", self.__Tip_leka),
            "{:10}{}".format("Proizvodjac: ", self.__Proizvodjac),
            "{:10}{}".format('Recepti', self.__ReceptLek),
        ])
