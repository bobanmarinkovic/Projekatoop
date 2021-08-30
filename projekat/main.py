from tkinter import *
from tkinter import messagebox
from Projekatoop.projekat.pacijent.pacijent import Pacijent,Lekar
from Projekatoop.projekat.pacijent.LekarIO import ucitaj_lekara,sacuvaj_lekara
from Projekatoop.projekat.pacijent.pacijentIO import ucitaj_pacijente,sacuvaj_pacijente
from Projekatoop.projekat.lek.lekIO import ucitaj_lek,sacuvaj_lek
from Projekatoop.projekat.Recept.receptIO import ucitaj_recepte,sacuvaj_recepte
import json
from types import SimpleNamespace

def main():
    root = Tk()
    app = glavni_prozor(root)
    root.mainloop()

def ocisti_labele(self):
    self.__sifra_labela["text"] = ""
    self.__naziv_labela["text"] = ""
    self.__cena_labela["text"] = ""
    self.__proizvodjac_labela["text"] = ""


class glavni_prozor():

    def __init__(self, master):
        self.master= master

        self.master.title("Apoteka")
        self.master.geometry("700x300")


        self.okvir = Frame(self.master)
        self.okvir.pack()

        unosFrame = Frame(self.master, bd=4, relief="solid", bg="Palegreen1")
        unosFrame.place(x=0, y=0, width=700, height=300)

        self.l_a = Label(unosFrame, text="APOTEKA", font=("arial", 35, "bold"))
        self.l_a.grid(row=2, column=1, sticky="")
        self.l_a.place(x=90, y=30, width=500, height=100)

        self.l_a = Label(unosFrame, text="**izaberite zeljenu opciju u meni baru**", font=("arial", 12, "bold"))
        self.l_a.grid(row=2, column=1, sticky="")
        self.l_a.place(x=140, y=200, width=420, height=40)
        meni = Menu(master)
        master.config(menu=meni)

        izlaz_meni = Menu(meni)
        meni.add_cascade(label="Izlaz", menu=izlaz_meni)
        izlaz_meni.add_command(label="Izadji", command=self.glavni_izlaz)
        podaci_meni = Menu(meni)
        meni.add_cascade(label="Podaci", menu=podaci_meni)
        podaci_meni.add_command(label="Pacijenti", command=self.prozor_pacijenti)
        podaci_meni.add_separator()
        podaci_meni.add_command(label="Lekari", command=self.prozor_lekari)
        podaci_meni.add_separator()
        podaci_meni.add_command(label="Recepti", command=self.prozor_recepti)
        podaci_meni.add_separator()
        podaci_meni.add_command(label="Lekovi", command=self.prozor_lekovi)

    def glavni_izlaz(self):
        pr = messagebox.askquestion('Izlaz', 'Da li zelite da izadjete iz aplikacije?',
                                         icon='question')
        if pr == 'yes':
            self.master.destroy()



    def prozor_pacijenti(self):
        self.window = Toplevel(self.master)
        self.app = prozor_pacijent(self.window)


    def prozor_lekari(self):
        self.window = Toplevel(self.master)
        self.app = prozor_lekari(self.window)
    def prozor_recepti(self):
        self.window = Toplevel(self.master)
        self.app = prozor_recepti(self.window)
    def prozor_lekovi(self):
        self.window = Toplevel(self.master)
        self.app = prozor_lekovi(self.window)

class prozor_pacijent():

    def prozor_za_dodavanje(self,ime, prezime, jmbg, datum, lbo):
        self.prozor=Tk()
        prozor=self.prozor

        Ime= Label(self.prozor, text='Unesite ime novog pacijenta', font=('bold'), pady=5)
        Ime.grid(row=0, column=0, sticky=W)
        self.Novoime = Entry(prozor, bg='whitesmoke')
        self.Novoime.grid(row=0, column=1)
        self.Novoime.insert(-1, ime)

        Prezime = Label(prozor, text='Unesite prezime pacijenta', font=('bold'))
        Prezime.grid(row=2, column=0, sticky=W)
        self.Novoprezime = Entry(prozor, bg='whitesmoke')
        self.Novoprezime.grid(row=2, column=1)
        self.Novoprezime.insert(-1, prezime)

        Datum= Label(prozor, text='Datum rodjenja', font=('bold'))
        Datum.grid(row=3, column=0, sticky=W)
        self.Novidatum = Entry(prozor, bg='whitesmoke')
        self.Novidatum.grid(row=3, column=1)
        self.Novidatum.insert(-1, datum)

        JMBG= Label(prozor, text='JMBG', font=('bold'))
        JMBG.grid(row=4, column=0, sticky=W)
        self.NoviJMBG= Entry(prozor, bg='whitesmoke')
        self.NoviJMBG.grid(row=4, column=1)
        self.NoviJMBG.insert(-1, jmbg)

        LBO= Label(prozor, text='LBO', font=('bold'))
        LBO.grid(row=5, column=0, sticky=W)
        self.NoviLBO = Entry(prozor, bg='whitesmoke')
        self.NoviLBO.grid(row=5, column=1)
        self.NoviLBO.insert(-1, lbo)

        self.prozor.geometry('1000x600')
        self.prozor.title("Dodavanje")
        return self.prozor

    def dodaj_prozor(self):
        self.prozor = self.prozor_za_dodavanje("", "", "", "","")
        self.dodaj_dugme = Button(self.prozor, text='Dodaj', width=12, command=self.dodaj)
        self.dodaj_dugme.grid(row=7, column=0, pady=20)

        izlaz_dugme = Button(self.prozor, text='Izlaz', bg='#d4575b', fg='white', width=12, command=self.prozor.destroy)
        izlaz_dugme.grid(row=7, column=1, pady=20)


    def dodaj(self):
        LBO=self.NoviLBO.get()
        JMBG=self.NoviJMBG.get()
        datum=self.Novidatum.get()
        prezime=self.Novoprezime.get()
        ime=self.Novoime.get()
        pacijent=ucitaj_pacijente()
        if not len(LBO)==11 :
            messagebox.showwarning("Greska","LBO mora imati 11 cifara i mora sadrzati iskljucivo cele brojeve!")
            self.prozor.destroy()
        elif not len(JMBG) == 13 :
            messagebox.showwarning("Greska","JMBG mora imati 13 cifara i mora sadrzati iskljucivo sele brojeve!")
            self.prozor.destroy()
        elif len(prezime)<2 :
            messagebox.showwarning("Greska","Prezime mora imati vise od 2 slova i mora sadrzati slova!")
            self.prozor.destroy()
        elif len(ime)<2 :
            messagebox.showwarning("Greska","Ime mora imati vise od 2 slova i mora sadrzati slova!")
            self.prozor.destroy()
        else:
                novipacijent={
                    "Ime" : ime,
                    "JMBG" : JMBG,
                    "Prezime" : prezime,
                    "Datum" :datum,
                    "LBO" : LBO


                }
        pacijent.append(novipacijent)
        sacuvaj_pacijente(pacijent)
        self.prikaz_listbox.delete(0, 'end')
        self.azuriraj_pacijenta()


    def sort(self):
        x = ucitaj_pacijente()

        z = 0
        for i in range(len(x)):
            for j in range(len(x)):
                if x[i]["Prezime"] <= x[j]["Prezime"]:
                    z = x[i]
                    x[i] = x[j]
                    x[j] = z

        sacuvaj_pacijente(x)
    def azuriraj_pacijenta(self):
        self.podaciopacijentu=[]
        self.sort()
        pacijent=ucitaj_pacijente()



        for i in pacijent:
            self.prikaz_listbox.insert(END, i["Prezime"] + " " + i["Ime"])
            korisnik={
                "Ime": i["Ime"],
                "JMBG":i["JMBG"],
                "Prezime":i["Prezime"],
                "Datum":i["Datum"],
                "LBO":i["LBO"]



            }
            self.podaciopacijentu.append(korisnik)

        print(self.podaciopacijentu)
    def izlaz(self):
        self.master.destroy()

    def prikaz(self):
        pozadina3 = Frame(self.master, bg='lemon chiffon', width=300, height=150)
        pozadina3.place(x=550, y=300, width=330, height=170)


        for i in self.prikaz_listbox.curselection():
            print(self.prikaz_listbox.get(i))
            proba=[]
            self.trenutni_pacijent = self.podaciopacijentu[self.prikaz_listbox.curselection()[0]]
            proba.append(self.trenutni_pacijent)
            print(proba)
            for i in proba:
                ime=i["Ime"]
                lbo=i["LBO"]
                datum=i["Datum"]
                prezime=i["Prezime"]
                jmbg=i["JMBG"]


            lbo_label = Label(pozadina3, text='LBO: ', bg='peachpuff2')
            lbo_label.grid(row=4, column=0, sticky=W, padx=10)
            self.lbo_entry = Entry(pozadina3, bg='white', width=30)
            self.lbo_entry.grid(row=4, column=1)
            self.lbo_entry.insert(-1, lbo)
            self.lbo_entry["state"] = "disabled"

            jmbg_label = Label(pozadina3, text='JMBG: ', bg='peachpuff2')
            jmbg_label.grid(row=3, column=0, sticky=W, padx=10)
            self.jmbg_entry = Entry(pozadina3, bg='white', width=30)
            self.jmbg_entry.grid(row=3, column=1)
            self.jmbg_entry.insert(-1,jmbg)
            self.jmbg_entry["state"] = "disabled"

            datum_label = Label(pozadina3, text='Datum rodjenja: ', bg='peachpuff2')
            datum_label.grid(row=2, column=0, sticky=W, padx=10)
            self.datum_entry = Entry(pozadina3, bg='white', width=30)
            self.datum_entry.grid(row=2, column=1)
            self.datum_entry.insert(1,datum)
            self.datum_entry["state"] = "disabled"

            prezime_label = Label(pozadina3, text='Prezime: ', bg='peachpuff2')
            prezime_label.grid(row=1, column=0, sticky=W, padx=10)
            self.prezime_entry = Entry(pozadina3, bg='white', width=30)
            self.prezime_entry.grid(row=1, column=1)
            self.prezime_entry.insert(-1,prezime)
            self.prezime_entry["state"] = "disabled"


            ime_label = Label(pozadina3, text='Ime: ', bg='peachpuff2')
            ime_label.grid(row=0, column=0, sticky=W, padx=10)
            self.ime_entry = Entry(pozadina3, bg='white', width=30)
            self.ime_entry.grid(row=0, column=1)
            self.ime_entry.insert(-1,ime)
            self.ime_entry["state"] = "disabled"
    def obrisi(self):
        Provera = messagebox.askquestion('Upozorenje', 'Brisanjem pacijenta, brisu se i svi njegovi recepti!\n\tDa li zelite da obrisete pacijenta?')

        if Provera == 'yes':

            pacijent=ucitaj_pacijente()
            recepti=ucitaj_recepte()
            self.trenutni_pacijent = self.podaciopacijentu[self.prikaz_listbox.curselection()[0]]
            test=[]
            test.append(self.trenutni_pacijent)

            for i in test:
                jmbgzabrisanje=i["JMBG"]

            for t in pacijent:
                if t["JMBG"]==jmbgzabrisanje:
                    receptpaczabrisanje=t["ReceptPac"]

                    for r in recepti:
                        if r["ReceptPac"]==receptpaczabrisanje:

                            recepti.remove(r)
            sacuvaj_recepte(recepti)
            for j in pacijent:
                if j["JMBG"] == jmbgzabrisanje:
                    pacijent.remove(j)
            sacuvaj_pacijente(pacijent)

            self.prikaz_listbox.delete(0,'end')
            self.azuriraj_pacijenta()



        else:
            self.izlaz()


    def cuvanje_promena(self):
        pacijent=ucitaj_pacijente()

        trpac=self.x
        ime=self.ime_entry.get()
        if len(ime)<2:
            messagebox.showwarning("Greska","Ime mora imati bar 2 karaktera!")
            self.prozor.destroy()
            self.izlaz()

        prezime=self.prezime_entry.get()
        if len(prezime)<2:
            messagebox.showwarning("Greska","Prezime mora imati bar 2 karaktera!")
            self.prozor.destroy()
            self.izlaz()

        datum=self.datum_entry.get()
        jmbg=self.jmbg_entry.get()
        lbo=self.lbo_entry.get()
        lista=[]
        for m in pacijent:
            lista.append(m)
        for j in lista:
            for s in j:
                if str(j["JMBG"])==jmbg:
                    if s=="ReceptPac":
                        recept=j["ReceptPac"]
                        trpac = {
                        "Ime": ime,
                        "Prezime": prezime,
                        "Datum": datum,
                        "JMBG": jmbg,
                        "LBO": lbo,
                        "ReceptPac": recept

                        }
                    else:
                        trpac = {
                        "Ime": ime,
                        "Prezime": prezime,
                        "Datum": datum,
                        "JMBG": jmbg,
                        "LBO": lbo
                    }



        for i in pacijent:
            if str(i["JMBG"]) == jmbg:
                pacijent.remove(i)
        sacuvaj_pacijente(pacijent)
        pacijent.append(trpac)
        sacuvaj_pacijente(pacijent)
        self.prikaz_listbox.delete(0, 'end')
        self.azuriraj_pacijenta()



    def izlaz2(self):
        self.prozor1.destroy()

    def izmena(self):
        self.prozor1 = Tk()
        prozor1 = self.prozor1
        prozor1.title("Izmena")
        prozor1.geometry("500x400")
        self.okvir = Frame(prozor1)
        self.okvir.pack()

        unosFrame = Frame(self.prozor1, bd=1, relief="solid", bg="LightBlue1")
        unosFrame.place(x=0, y=0, width=500, height=400)

        self.trenutni_pacijent = self.podaciopacijentu[self.prikaz_listbox.curselection()[0]]
        self.x=[]
        self.x.append(self.trenutni_pacijent)
        for i in self.x:
            ime=i["Ime"]
            prezime=i["Prezime"]
            datum=i["Datum"]
            jmbg=i["JMBG"]
            lbo=i["LBO"]

        print(self.trenutni_pacijent)
        ime_label = Label(unosFrame, text='Ime:                    ',font=("arial", 12),bg='azure')
        ime_label.place(x=10,y=30)
        self.ime_entry = Entry(unosFrame, bg='azure',font=("arial",12))
        self.ime_entry.place(x=140,y=30)
        self.ime_entry.insert(0, ime)


        prezime_label = Label(unosFrame, text='Prezime:            ', font=("arial", 12), bg='azure')
        prezime_label.place(x=10, y=60)
        self.prezime_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.prezime_entry.place(x=140, y=60)
        self.prezime_entry.insert(0,prezime)


        datum_label = Label(unosFrame, text='Datum rodjenja:', font=("arial", 12), bg='azure')
        datum_label.place(x=10, y=90)
        self.datum_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.datum_entry.place(x=140, y=90)
        self.datum_entry.insert(-1,datum)



        jmbg_label = Label(unosFrame, text='JMBG:               ', font=("arial", 12), bg='azure')
        jmbg_label.place(x=10, y=120)
        self.jmbg_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.jmbg_entry.place(x=140, y=120)
        self.jmbg_entry.insert(-1,jmbg)
        self.jmbg_entry["state"] = "disabled"

        lbo_label = Label(unosFrame, text='LBO:                  ', font=("arial", 12), bg='azure')
        lbo_label.place(x=10, y=150)
        self.lbo_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.lbo_entry.place(x=140, y=150)
        self.lbo_entry.insert(-1,lbo)
        self.lbo_entry["state"] = "disabled"


        self.dugme = Button(unosFrame, text='Izlaz', width=15, command=self.izlaz2)
        self.dugme.place(x=190, y=230)

        self.dugme2 = Button(unosFrame, text='Sacuvaj', width=15, command=self.cuvanje_promena)
        self.dugme2.place(x=350, y=80)

    def provera(self,event):
        podaci=[]
        uneto=self.pretraga_label.get()
        if uneto == '':
            self.prikaz_listbox.delete(0, 'end')
            self.azuriraj_pacijenta()

        else:

            z=ucitaj_pacijente()
            for i in z:
                if uneto.lower() in i["Prezime"].lower() or uneto.lower() in i["Ime"].lower():
                    podaci.append(i)

            self.prikaz_listbox.delete(0, 'end')
            for j in podaci:

                self.prikaz_listbox.insert('end',j["Prezime"]+" "+j["Ime"])

    def izlaz3(self):
        self.prozor2.destroy()

    def recepti(self):
        self.prozor2 = Tk()
        prozor2 = self.prozor2
        prozor2.title("Recepti-Pacijenti")
        prozor2.geometry("500x400")
        self.okvir = Frame(prozor2)
        self.okvir.pack()

        unosFrame = Frame(self.prozor2, bd=1, relief="solid", bg="LightBlue1")
        unosFrame.place(x=0, y=0, width=700, height=400)

        self.listbox_recepti = Listbox(unosFrame, width=40)
        self.listbox_recepti.place(x=50, y=70)

        self.dugmezaizlaz=Button(unosFrame,width=15,text='Izlaz',command=self.izlaz3)
        self.dugmezaizlaz.place(x=110, y=280)

        pacijent = ucitaj_pacijente()
        lekar = ucitaj_lekara()
        lek = ucitaj_lek()
        recept = ucitaj_recepte()
        self.trenutni_pacijent = self.podaciopacijentu[self.prikaz_listbox.curselection()[0]]
        test=[]
        test.append(self.trenutni_pacijent)
        trenutnijmbg=0
        for i in test:
            trenutnijmbg=i["JMBG"]
        for j in pacijent:
            if j["JMBG"]==trenutnijmbg:
                if "ReceptPac" in j:

                    for r in recept:
                        if j["ReceptPac"] == r["ReceptPac"]:
                            for m in lekar:
                                if "ReceptLekar" in m:
                                    if m["ReceptLekar"]==r["ReceptLekar"]:
                                        for l in lek:

                                            if l["ReceptLek"] == r["ReceptLek"]:

                                                self.listbox_recepti.insert(-1, str(l["JKL"])+", "+l["Naziv"]+", "+m["Ime"]+" "+m["Prezime"])






                else:
                    messagebox.showwarning("Greska", "Pacijent trenutno nema recepte!")

                    self.izlaz()
                    self.izlaz3()



    def dozvola(self, event):

            self.dodaj_dugme4["state"] = "active"
            self.dodaj_dugme2["state"] = "active"
            self.dodaj_dugme3['state'] = 'active'
            self.dodaj_dugme5['state'] = 'active'
            self.dodaj_dugme6['state'] = 'active'





    def __init__(self,master):
                self.master= master

                master.title("Pacijenti")
                master.geometry("1000x650")
                self.okvir = Frame(master)
                self.okvir.pack()

                unosFrame = Frame(self.master, bd=4, relief="solid", bg="peach puff")
                unosFrame.place(x=0, y=0, width=1000, height=800)

                self.okvir = Frame(master)
                self.okvir.pack()

                unosFrame = Frame(self.master, bd=4, relief="solid", bg="peach puff")
                unosFrame.place(x=0, y=0, width=1000, height=800)

                self.l_a = Label(unosFrame, text="PACIJENTI", font=("arial", 37, 'bold'),bg='peach puff3')
                self.l_a.place(x=400,y=100)


                self.dodaj_dugme = Button(unosFrame, text='Dodaj', width=15, command=self.dodaj_prozor)
                self.dodaj_dugme.place(x=720,y=500)

                self.dodaj_dugme2= Button(unosFrame,text='Izlaz', width=15,command=self.izlaz)
                self.dodaj_dugme2.place(x=800, y=200)


                self.dodaj_dugme3 = Button(unosFrame, text='Prikaz', width=15, command=self.prikaz)
                self.dodaj_dugme3.place(x=120, y=500)
                self.dodaj_dugme3['state'] = 'disabled'

                self.dodaj_dugme4=Button(unosFrame,text='Obrisi', width=15,command=self.obrisi)
                self.dodaj_dugme4.place(x=415,y=230)
                self.dodaj_dugme4['state'] = 'disabled'

                self.dodaj_dugme5=Button(unosFrame,text='Izmena', width=15, command=self.izmena)
                self.dodaj_dugme5.place(x=315,y=500)
                self.dodaj_dugme5['state'] = 'disabled'

                self.dodaj_dugme6 = Button(unosFrame, text='Recepti', width=15, command=self.recepti)
                self.dodaj_dugme6.place(x=520, y=500)
                self.dodaj_dugme6['state'] = 'disabled'

                self.pretraga=Label(unosFrame, text="PRETRAGA", font=("Al Tarikh", 12, 'bold'),bg='peach puff2')
                self.pretraga.place(x=100,y=230)
                self.pretraga_label = Entry(unosFrame, font=("ariel", 12))
                self.pretraga_label.place(x=100,y=260)

                self.pretraga_label.bind("<KeyRelease>",self.provera)

                self.prikaz_listbox=Listbox(unosFrame,width=50)
                self.prikaz_listbox.place(x=100,y=300)
                self.prikaz_listbox.bind("<<ListboxSelect>>", self.dozvola)
                self.azuriraj_pacijenta()


class prozor_lekari:
    def prozor_za_dodavanje_lekar(self,ime, prezime, jmbg, datum, lbo):
        self.prozorlekar=Tk()
        prozorlekar=self.prozorlekar


        lekarIme= Label(self.prozorlekar, text='Unesite ime novog pacijenta', font=('bold'), pady=5)
        lekarIme.grid(row=0, column=0, sticky=W)
        self.lekarNovoime = Entry(prozorlekar, bg='whitesmoke')
        self.lekarNovoime.grid(row=0, column=1)
        self.lekarNovoime.insert(-1, ime)

        lekarPrezime = Label(prozorlekar, text='Unesite prezime pacijenta', font=('bold'))
        lekarPrezime.grid(row=2, column=0, sticky=W)
        self.lekarNovoprezime = Entry(prozorlekar, bg='whitesmoke')
        self.lekarNovoprezime.grid(row=2, column=1)
        self.lekarNovoprezime.insert(-1, prezime)

        lekarDatum= Label(prozorlekar, text='Datum rodjenja', font=('bold'))
        lekarDatum.grid(row=3, column=0, sticky=W)
        self.lekarNovidatum = Entry(prozorlekar, bg='whitesmoke')
        self.lekarNovidatum.grid(row=3, column=1)
        self.lekarNovidatum.insert(-1, datum)

        lekarJMBG= Label(prozorlekar, text='JMBG', font=('bold'))
        lekarJMBG.grid(row=4, column=0, sticky=W)
        self.lekarNoviJMBG= Entry(prozorlekar, bg='whitesmoke')
        self.lekarNoviJMBG.grid(row=4, column=1)
        self.lekarNoviJMBG.insert(-1, jmbg)

        lekarLBO= Label(prozorlekar, text='Specijalizacija', font=('bold'))
        lekarLBO.grid(row=5, column=0, sticky=W)
        self.lekarNoviLBO = Entry(prozorlekar, bg='whitesmoke')
        self.lekarNoviLBO.grid(row=5, column=1)
        self.lekarNoviLBO.insert(-1, lbo)

        self.prozorlekar.geometry('1000x600')
        self.prozorlekar.title("Dodavanje")
        return self.prozorlekar

    def dodaj_prozor(self):
        self.prozorlekar = self.prozor_za_dodavanje_lekar("", "", "", "","")
        self.dodaj_dugme = Button(self.prozorlekar, text='Dodaj', width=12, command=self.dodaj)
        self.dodaj_dugme.grid(row=7, column=0, pady=20)

        izlaz_dugme = Button(self.prozorlekar, text='Izlaz', bg='#d4575b', fg='white', width=12, command=self.prozorlekar.destroy)
        izlaz_dugme.grid(row=7, column=1, pady=20)


    def dodaj(self):
        LBO=self.lekarNoviLBO.get()
        JMBG=self.lekarNoviJMBG.get()
        datum=self.lekarNovidatum.get()
        prezime=self.lekarNovoprezime.get()
        ime=self.lekarNovoime.get()
        lekar=ucitaj_lekara()

        if not len(JMBG) == 13 :
            messagebox.showwarning("Greska","JMBG mora imati 13 cifara i mora sadrzati iskljucivo sele brojeve!")
            self.prozorlekar.destroy()
        elif len(prezime)<2 :
            messagebox.showwarning("Greska","Prezime mora imati vise od 2 slova i mora sadrzati slova!")
            self.prozorlekar.destroy()
        elif len(ime)<2 :
            messagebox.showwarning("Greska","Ime mora imati vise od 2 slova i mora sadrzati slova!")
            self.prozorlekar.destroy()
        else:
                novilekar={
                    "Ime" : ime,
                    "JMBG" : JMBG,
                    "Prezime" : prezime,
                    "Datum" :datum,
                    "Specijalizacija" : LBO


                }
        lekar.append(novilekar)
        sacuvaj_lekara(lekar)
        self.prikaz_listbox.delete(0, 'end')
        self.azuriraj_lekara()


    def sort(self):
        x = ucitaj_lekara()

        z = 0
        for i in range(len(x)):
            for j in range(len(x)):
                if x[i]["Prezime"] <= x[j]["Prezime"]:
                    z = x[i]
                    x[i] = x[j]
                    x[j] = z

        sacuvaj_lekara(x)
    def azuriraj_lekara(self):
        self.podaciolekaru=[]
        self.sort()
        lekar=ucitaj_lekara()



        for i in lekar:
            self.prikaz_listbox.insert(END, i["Prezime"] + " " + i["Ime"])
            korisnik={
                "Ime": i["Ime"],
                "JMBG":i["JMBG"],
                "Prezime":i["Prezime"],
                "Datum":i["Datum"],
                "Specijalizacija":i["Specijalizacija"]


            }
            self.podaciolekaru.append(korisnik)

        print(self.podaciolekaru)
    def izlaz(self):
        self.master.destroy()

    def prikaz(self):
        pozadina3 = Frame(self.master, bg='lemon chiffon', width=300, height=150)
        pozadina3.place(x=550, y=300, width=330, height=170)


        for i in self.prikaz_listbox.curselection():
            print(self.prikaz_listbox.get(i))
            proba=[]
            self.trenutni_lekar = self.podaciolekaru[self.prikaz_listbox.curselection()[0]]
            proba.append(self.trenutni_lekar)
            print(proba)
            for i in proba:
                ime=i["Ime"]
                specijalizacija=i["Specijalizacija"]
                datum=i["Datum"]
                prezime=i["Prezime"]
                jmbg=i["JMBG"]


            lbo_label = Label(pozadina3, text='Specijalizacija: ', bg='peachpuff2')
            lbo_label.grid(row=4, column=0, sticky=W, padx=10)
            self.lbo_entry = Entry(pozadina3, bg='white', width=30)
            self.lbo_entry.grid(row=4, column=1)
            self.lbo_entry.insert(-1, specijalizacija)
            self.lbo_entry["state"] = "disabled"

            jmbg_label = Label(pozadina3, text='JMBG: ', bg='peachpuff2')
            jmbg_label.grid(row=3, column=0, sticky=W, padx=10)
            self.jmbg_entry = Entry(pozadina3, bg='white', width=30)
            self.jmbg_entry.grid(row=3, column=1)
            self.jmbg_entry.insert(-1,jmbg)
            self.jmbg_entry["state"] = "disabled"

            datum_label = Label(pozadina3, text='Datum rodjenja: ', bg='peachpuff2')
            datum_label.grid(row=2, column=0, sticky=W, padx=10)
            self.datum_entry = Entry(pozadina3, bg='white', width=30)
            self.datum_entry.grid(row=2, column=1)
            self.datum_entry.insert(1,datum)
            self.datum_entry["state"] = "disabled"

            prezime_label = Label(pozadina3, text='Prezime: ', bg='peachpuff2')
            prezime_label.grid(row=1, column=0, sticky=W, padx=10)
            self.prezime_entry = Entry(pozadina3, bg='white', width=30)
            self.prezime_entry.grid(row=1, column=1)
            self.prezime_entry.insert(-1,prezime)
            self.prezime_entry["state"] = "disabled"


            ime_label = Label(pozadina3, text='Ime: ', bg='peachpuff2')
            ime_label.grid(row=0, column=0, sticky=W, padx=10)
            self.ime_entry = Entry(pozadina3, bg='white', width=30)
            self.ime_entry.grid(row=0, column=1)
            self.ime_entry.insert(-1,ime)
            self.ime_entry["state"] = "disabled"
    def obrisi(self):
        Provera = messagebox.askquestion('Upozorenje', 'Brisanjem lekara, brisu se i svi njegovi recepti!\n\tDa li zelite da obrisete lekara?')

        if Provera == 'yes':

            pacijent=ucitaj_lekara()
            self.trenutni_lekar = self.podaciolekaru[self.prikaz_listbox.curselection()[0]]
            test=[]
            test.append(self.trenutni_lekar)
            recepti=ucitaj_recepte()
            for i in test:
                jmbgzabrisanje=i["JMBG"]
            for t in pacijent:
                if t["JMBG"] == jmbgzabrisanje:
                    receptpaczabrisanje = t["ReceptLekar"]

                    for r in recepti:
                        if r["ReceptLekar"] == receptpaczabrisanje:
                            recepti.remove(r)
            sacuvaj_recepte(recepti)
            for j in pacijent:
                if j["JMBG"] == jmbgzabrisanje:
                    pacijent.remove(j)
            sacuvaj_lekara(pacijent)

            self.prikaz_listbox.delete(0, 'end')
            self.azuriraj_lekara()

        else:
            self.izlaz()


    def cuvanje_promena(self):
        lekar=ucitaj_lekara()

        trpac=self.x
        ime=self.ime_entry.get()
        if len(ime)<2:
            messagebox.showwarning("Greska","Ime mora imati bar 2 karaktera!")
            self.prozorlekar.destroy()
            self.izlaz()

        prezime=self.prezime_entry.get()
        if len(prezime)<2:
            messagebox.showwarning("Greska","Prezime mora imati bar 2 karaktera!")
            self.prozorlekar.destroy()
            self.izlaz()

        datum=self.datum_entry.get()
        jmbg=self.jmbg_entry.get()
        specijalizacija=self.lbo_entry.get()
        lista=[]
        for m in lekar:
            lista.append(m)
        for j in lista:
            for s in j:
                if str(j["JMBG"])==jmbg:
                    if s=="ReceptLekar":
                        recept=j["ReceptLekar"]
                        trpac = {
                        "Ime": ime,
                        "Prezime": prezime,
                        "Datum": datum,
                        "JMBG": jmbg,
                        "Specijalizacija": specijalizacija,
                        "ReceptLekar": recept

                        }
                    else:
                        trpac = {
                        "Ime": ime,
                        "Prezime": prezime,
                        "Datum": datum,
                        "JMBG": jmbg,
                        "Specijalizacija": specijalizacija
                    }





        for i in lekar:
            if i["JMBG"]==jmbg:
                lekar.remove(i)


        sacuvaj_lekara(lekar)
        lekar.append(trpac)
        sacuvaj_lekara(lekar)
        self.prikaz_listbox.delete(0, 'end')
        self.azuriraj_lekara()



    def izlaz2(self):
        self.prozor1.destroy()

    def izmena(self):
        self.prozor1 = Tk()
        prozor1 = self.prozor1
        prozor1.title("Izmena")
        prozor1.geometry("500x400")
        self.okvir = Frame(prozor1)
        self.okvir.pack()

        unosFrame = Frame(self.prozor1, bd=1, relief="solid", bg="LightBlue1")
        unosFrame.place(x=0, y=0, width=500, height=400)

        self.trenutni_lekar = self.podaciolekaru[self.prikaz_listbox.curselection()[0]]
        self.x=[]
        self.x.append(self.trenutni_lekar)
        for i in self.x:
            ime=i["Ime"]
            prezime=i["Prezime"]
            datum=i["Datum"]
            jmbg=i["JMBG"]
            lbo=i["Specijalizacija"]

        print(self.trenutni_lekar)
        ime_label = Label(unosFrame, text='Ime:                    ',font=("arial", 12),bg='azure')
        ime_label.place(x=10,y=30)
        self.ime_entry = Entry(unosFrame, bg='azure',font=("arial",12))
        self.ime_entry.place(x=140,y=30)
        self.ime_entry.insert(0, ime)


        prezime_label = Label(unosFrame, text='Prezime:            ', font=("arial", 12), bg='azure')
        prezime_label.place(x=10, y=60)
        self.prezime_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.prezime_entry.place(x=140, y=60)
        self.prezime_entry.insert(0,prezime)


        datum_label = Label(unosFrame, text='Datum rodjenja:', font=("arial", 12), bg='azure')
        datum_label.place(x=10, y=90)
        self.datum_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.datum_entry.place(x=140, y=90)
        self.datum_entry.insert(-1,datum)



        jmbg_label = Label(unosFrame, text='JMBG:               ', font=("arial", 12), bg='azure')
        jmbg_label.place(x=10, y=120)
        self.jmbg_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.jmbg_entry.place(x=140, y=120)
        self.jmbg_entry.insert(-1,jmbg)
        self.jmbg_entry["state"] = "disabled"

        lbo_label = Label(unosFrame, text='Specijalizacija:   ', font=("arial", 12), bg='azure')
        lbo_label.place(x=10, y=150)
        self.lbo_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.lbo_entry.place(x=140, y=150)
        self.lbo_entry.insert(-1,lbo)



        self.dugme = Button(unosFrame, text='Izlaz', width=15, command=self.izlaz2)
        self.dugme.place(x=190, y=230)

        self.dugme2 = Button(unosFrame, text='Sacuvaj', width=15, command=self.cuvanje_promena)
        self.dugme2.place(x=350, y=80)

    def provera(self,event):
        podaci=[]
        uneto=self.pretraga_label.get()
        if uneto == '':
            self.prikaz_listbox.delete(0, 'end')
            self.azuriraj_lekara()

        else:

            z=ucitaj_lekara()
            for i in z:
                if uneto.lower() in i["Prezime"].lower() or uneto.lower() in i["Ime"].lower():
                    podaci.append(i)

            self.prikaz_listbox.delete(0, 'end')
            for j in podaci:

                self.prikaz_listbox.insert('end',j["Prezime"]+" "+j["Ime"])

    def izlaz3(self):
        self.prozor2.destroy()

    def recepti(self):
        self.prozor2 = Tk()
        prozor2 = self.prozor2
        prozor2.title("Recepti-Lekar")
        prozor2.geometry("500x400")
        self.okvir = Frame(prozor2)
        self.okvir.pack()

        unosFrame = Frame(self.prozor2, bd=1, relief="solid", bg="LightBlue1")
        unosFrame.place(x=0, y=0, width=700, height=400)

        self.listbox_recepti = Listbox(unosFrame, width=40)
        self.listbox_recepti.place(x=50, y=70)

        self.dugmezaizlaz=Button(unosFrame,width=15,text='Izlaz',command=self.izlaz3)
        self.dugmezaizlaz.place(x=110, y=280)

        pacijent = ucitaj_pacijente()
        lekar = ucitaj_lekara()
        lek = ucitaj_lek()
        recept = ucitaj_recepte()
        self.trenutni_lekar = self.podaciolekaru[self.prikaz_listbox.curselection()[0]]
        test=[]
        test.append(self.trenutni_lekar)
        trenutnijmbg=0
        for i in test:
            trenutnijmbg=i["JMBG"]
        for j in lekar:
            if j["JMBG"]==trenutnijmbg:
                if "ReceptLekar" in j:

                    for r in recept:
                        if j["ReceptLekar"] == r["ReceptLekar"]:
                            for l in lek:
                                if l["ReceptLek"]==r["ReceptLek"]:

                                            self.listbox_recepti.insert(-1, str(l["JKL"])+", "+l["Naziv"]+", "+l["Proizvodjac"])



                else:
                    messagebox.showwarning("Greska", "Lekar trenutno nema izdate recepte!")
                    self.izlaz2()
                    self.izlaz()
                    self.izlaz3()
    def dozvola(self, event):

            self.dodaj_dugme4["state"] = "active"
            self.dodaj_dugme2["state"] = "active"
            self.dodaj_dugme3['state'] = 'active'
            self.dodaj_dugme5['state'] = 'active'
            self.dodaj_dugme6['state'] = 'active'

    def __init__(self,master):
                self.master= master

                master.title("LEKAR")
                master.geometry("1000x650")
                self.okvir = Frame(master)
                self.okvir.pack()

                unosFrame = Frame(self.master, bd=4, relief="solid", bg="peach puff")
                unosFrame.place(x=0, y=0, width=1000, height=800)

                self.okvir = Frame(master)
                self.okvir.pack()

                unosFrame = Frame(self.master, bd=4, relief="solid", bg="peach puff")
                unosFrame.place(x=0, y=0, width=1000, height=800)

                self.l_a = Label(unosFrame, text="LEKARI", font=("arial", 37, 'bold'),bg='peach puff3')
                self.l_a.place(x=400,y=100)


                self.dodaj_dugme = Button(unosFrame, text='Dodaj', width=15, command=self.dodaj_prozor)
                self.dodaj_dugme.place(x=720,y=500)

                self.dodaj_dugme2= Button(unosFrame,text='Izlaz', width=15,command=self.izlaz)
                self.dodaj_dugme2.place(x=800, y=200)

                self.dodaj_dugme3 = Button(unosFrame, text='Prikaz', width=15, command=self.prikaz)
                self.dodaj_dugme3.place(x=120, y=500)
                self.dodaj_dugme3['state'] = 'disabled'

                self.dodaj_dugme4=Button(unosFrame,text='Obrisi', width=15,command=self.obrisi)
                self.dodaj_dugme4.place(x=415,y=230)
                self.dodaj_dugme4['state'] = 'disabled'

                self.dodaj_dugme5=Button(unosFrame,text='Izmena', width=15, command=self.izmena)
                self.dodaj_dugme5.place(x=315,y=500)
                self.dodaj_dugme5['state'] = 'disabled'

                self.dodaj_dugme6 = Button(unosFrame, text='Recepti', width=15, command=self.recepti)
                self.dodaj_dugme6.place(x=520, y=500)
                self.dodaj_dugme6['state'] = 'disabled'

                self.pretraga=Label(unosFrame, text="PRETRAGA", font=("Al Tarikh", 12, 'bold'),bg='peach puff2')
                self.pretraga.place(x=100,y=230)
                self.pretraga_label = Entry(unosFrame, font=("ariel", 12))
                self.pretraga_label.place(x=100,y=260)

                self.pretraga_label.bind("<KeyRelease>",self.provera)

                self.prikaz_listbox=Listbox(unosFrame,width=50)
                self.prikaz_listbox.place(x=100,y=300)
                self.prikaz_listbox.bind("<<ListboxSelect>>", self.dozvola)

                self.azuriraj_lekara()

class prozor_lekovi:
    def prozor_za_dodavanje_leka(self,ime, prezime, jmbg, datum):
        self.prozorlekar=Tk()
        prozorlekar=self.prozorlekar


        lekarIme= Label(self.prozorlekar, text='Naziv', font=('bold'), pady=5)
        lekarIme.grid(row=0, column=0, sticky=W)
        self.lekarNovoime = Entry(prozorlekar, bg='whitesmoke')
        self.lekarNovoime.grid(row=0, column=1)
        self.lekarNovoime.insert(-1, ime)

        lekarPrezime = Label(prozorlekar, text='Proizvodjac', font=('bold'))
        lekarPrezime.grid(row=2, column=0, sticky=W)
        self.lekarNovoprezime = Entry(prozorlekar, bg='whitesmoke')
        self.lekarNovoprezime.grid(row=2, column=1)
        self.lekarNovoprezime.insert(-1, prezime)

        lekarDatum= Label(prozorlekar, text='Tip leka', font=('bold'))
        lekarDatum.grid(row=3, column=0, sticky=W)
        self.lekarNovidatum = Entry(prozorlekar, bg='whitesmoke')
        self.lekarNovidatum.grid(row=3, column=1)
        self.lekarNovidatum.insert(-1, datum)

        lekarJMBG= Label(prozorlekar, text='JKL', font=('bold'))
        lekarJMBG.grid(row=4, column=0, sticky=W)
        self.lekarNoviJMBG= Entry(prozorlekar, bg='whitesmoke')
        self.lekarNoviJMBG.grid(row=4, column=1)
        self.lekarNoviJMBG.insert(-1, jmbg)



        self.prozorlekar.geometry('1000x600')
        self.prozorlekar.title("Dodavanje")
        return self.prozorlekar

    def dodaj_prozor(self):
        self.prozorlekar = self.prozor_za_dodavanje_leka("", "", "", "")
        self.dodaj_dugme = Button(self.prozorlekar, text='Dodaj', width=12, command=self.dodaj)
        self.dodaj_dugme.grid(row=7, column=0, pady=20)

        izlaz_dugme = Button(self.prozorlekar, text='Izlaz', bg='#d4575b', fg='white', width=12, command=self.prozorlekar.destroy)
        izlaz_dugme.grid(row=7, column=1, pady=20)


    def dodaj(self):

        JMBG=self.lekarNoviJMBG.get()
        datum=self.lekarNovidatum.get()
        prezime=self.lekarNovoprezime.get()
        ime=self.lekarNovoime.get()
        lekar=ucitaj_lek()

        if not len(JMBG) == 7 :
            messagebox.showwarning("Greska","JKL mora imati 7 cifara i mora sadrzati iskljucivo sele brojeve!")
            self.prozorlekar.destroy()
        elif len(prezime)<2 :
            messagebox.showwarning("Greska","Proizvodjac mora imati vise od 2 slova i mora sadrzati slova!")
            self.prozorlekar.destroy()
        elif len(ime)<2 :
            messagebox.showwarning("Greska","Naziv mora imati vise od 2 slova i mora sadrzati slova!")
            self.prozorlekar.destroy()
        else:
                novilekar={
                    "Naziv" : ime,
                    "JKL" : JMBG,
                    "Proizvodjac" : prezime,
                    "Tip leka" :datum



                }
        lekar.append(novilekar)
        sacuvaj_lek(lekar)
        self.prikaz_listbox.delete(0, 'end')
        self.azuriraj_lek()


    def sort(self):
        x = ucitaj_lek()

        z = 0
        for i in range(len(x)):
            for j in range(len(x)):
                if x[i]["Naziv"] <= x[j]["Naziv"]:
                    z = x[i]
                    x[i] = x[j]
                    x[j] = z

        sacuvaj_lek(x)
    def azuriraj_lek(self):
        self.podacioleku=[]
        self.sort()
        lekar=ucitaj_lek()



        for i in lekar:
            self.prikaz_listbox.insert(END, i["Naziv"] + " " + i["Proizvodjac"])
            korisnik={
                "Naziv": i["Naziv"],
                "JKL":i["JKL"],
                "Proizvodjac":i["Proizvodjac"],
                "Tip leka":i["Tip leka"]



            }
            self.podacioleku.append(korisnik)

        print(self.podacioleku)
    def izlaz(self):
        self.master.destroy()

    def prikaz(self):
        pozadina3 = Frame(self.master, bg='lemon chiffon', width=300, height=150)
        pozadina3.place(x=550, y=300, width=330, height=170)


        for i in self.prikaz_listbox.curselection():
            print(self.prikaz_listbox.get(i))
            proba=[]
            self.trenutni_lek = self.podacioleku[self.prikaz_listbox.curselection()[0]]
            proba.append(self.trenutni_lek)
            print(proba)
            for i in proba:
                ime=i["Naziv"]
                datum=i["Tip leka"]
                prezime=i["Proizvodjac"]
                jmbg=i["JKL"]



            jmbg_label = Label(pozadina3, text='JKL: ', bg='peachpuff2')
            jmbg_label.grid(row=3, column=0, sticky=W, padx=10)
            self.jmbg_entry = Entry(pozadina3, bg='white', width=30)
            self.jmbg_entry.grid(row=3, column=1)
            self.jmbg_entry.insert(-1,jmbg)
            self.jmbg_entry["state"] = "disabled"

            datum_label = Label(pozadina3, text='TIP leka: ', bg='peachpuff2')
            datum_label.grid(row=2, column=0, sticky=W, padx=10)
            self.datum_entry = Entry(pozadina3, bg='white', width=30)
            self.datum_entry.grid(row=2, column=1)
            self.datum_entry.insert(1,datum)
            self.datum_entry["state"] = "disabled"

            prezime_label = Label(pozadina3, text='Proizvodjac: ', bg='peachpuff2')
            prezime_label.grid(row=1, column=0, sticky=W, padx=10)
            self.prezime_entry = Entry(pozadina3, bg='white', width=30)
            self.prezime_entry.grid(row=1, column=1)
            self.prezime_entry.insert(-1,prezime)
            self.prezime_entry["state"] = "disabled"


            ime_label = Label(pozadina3, text='Naziv: ', bg='peachpuff2')
            ime_label.grid(row=0, column=0, sticky=W, padx=10)
            self.ime_entry = Entry(pozadina3, bg='white', width=30)
            self.ime_entry.grid(row=0, column=1)
            self.ime_entry.insert(-1,ime)
            self.ime_entry["state"] = "disabled"
    def obrisi(self):
        Provera = messagebox.askquestion('Upozorenje', 'Brisanjem leka, brisu se i svi njegovi recepti!\n\tDa li zelite da obrisete lek?')

        if Provera == 'yes':

            pacijent=ucitaj_lek()
            self.trenutni_lek = self.podacioleku[self.prikaz_listbox.curselection()[0]]
            test=[]
            test.append(self.trenutni_lek)
            recepti=ucitaj_recepte()
            for i in test:
                jmbgzabrisanje = i["JKL"]
            for t in pacijent:
                if t["JKL"] == jmbgzabrisanje:
                    receptpaczabrisanje = t["ReceptLek"]

                    for r in recepti:
                        if r["ReceptLek"] == receptpaczabrisanje:
                            recepti.remove(r)
            sacuvaj_recepte(recepti)
            for j in pacijent:
                if j["JKL"] == jmbgzabrisanje:
                    pacijent.remove(j)
            sacuvaj_lek(pacijent)

            self.prikaz_listbox.delete(0, 'end')
            self.azuriraj_lek()
        else:
            self.izlaz()


    def cuvanje_promena(self):
        lekar=ucitaj_lek()

        trpac=self.x
        ime=self.ime_entry.get()
        if len(ime)<2:
            messagebox.showwarning("Greska","Ime mora imati bar 2 karaktera!")
            self.prozorlekar.destroy()
            self.izlaz()

        prezime=self.prezime_entry.get()
        if len(prezime)<2:
            messagebox.showwarning("Greska","Prezime mora imati bar 2 karaktera!")
            self.prozorlekar.destroy()
            self.izlaz()

        datum=self.datum_entry.get()
        jmbg=self.jmbg_entry.get()

        lista = []
        for m in lekar:
            lista.append(m)
        for j in lista:
            for s in j:
                if str(j["JKL"]) == jmbg:
                    if s == "ReceptLek":
                        recept = j["ReceptLek"]
                        trpac = {
                            "Naziv": ime,
                            "Proizvodjac": prezime,
                            "Tip leka": datum,
                            "JKL": jmbg,

                            "ReceptLek": recept

                        }
                    else:
                        trpac = {
                            "Naziv": ime,
                            "Proizvodjac": prezime,
                            "Tip Leka": datum,
                            "JKL": jmbg

                        }
        for i in lekar:
            if str(i["JKL"])==jmbg:
                lekar.remove(i)
        sacuvaj_lek(lekar)
        lekar.append(trpac)
        sacuvaj_lek(lekar)
        self.prikaz_listbox.delete(0, 'end')
        self.azuriraj_lek()



    def izlaz2(self):
        self.prozor1.destroy()

    def izmena(self):
        self.prozor1 = Tk()
        prozor1 = self.prozor1
        prozor1.title("Izmena")
        prozor1.geometry("500x400")
        self.okvir = Frame(prozor1)
        self.okvir.pack()

        unosFrame = Frame(self.prozor1, bd=1, relief="solid", bg="LightBlue1")
        unosFrame.place(x=0, y=0, width=500, height=400)

        self.trenutni_lekar = self.podacioleku[self.prikaz_listbox.curselection()[0]]
        self.x=[]
        self.x.append(self.trenutni_lekar)
        for i in self.x:
            ime=i["Naziv"]
            prezime=i["Proizvodjac"]
            datum=i["Tip leka"]
            jmbg=i["JKL"]


        print(self.trenutni_lekar)
        ime_label = Label(unosFrame, text='Naziv:                  ',font=("arial", 12),bg='azure')
        ime_label.place(x=10,y=30)
        self.ime_entry = Entry(unosFrame, bg='azure',font=("arial",12))
        self.ime_entry.place(x=140,y=30)
        self.ime_entry.insert(0, ime)


        prezime_label = Label(unosFrame, text='Proiyvodjac:           ', font=("arial", 12), bg='azure')
        prezime_label.place(x=10, y=60)
        self.prezime_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.prezime_entry.place(x=140, y=60)
        self.prezime_entry.insert(0,prezime)


        datum_label = Label(unosFrame, text='Tip leka:   ', font=("arial", 12), bg='azure')
        datum_label.place(x=10, y=90)
        self.datum_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.datum_entry.place(x=140, y=90)
        self.datum_entry.insert(-1,datum)



        jmbg_label = Label(unosFrame, text='JKL:                ', font=("arial", 12), bg='azure')
        jmbg_label.place(x=10, y=120)
        self.jmbg_entry = Entry(unosFrame, bg='azure', font=("arial", 12))
        self.jmbg_entry.place(x=140, y=120)
        self.jmbg_entry.insert(-1,jmbg)
        self.jmbg_entry["state"] = "disabled"





        self.dugme = Button(unosFrame, text='Izlaz', width=15, command=self.izlaz2)
        self.dugme.place(x=190, y=230)

        self.dugme2 = Button(unosFrame, text='Sacuvaj', width=15, command=self.cuvanje_promena)
        self.dugme2.place(x=350, y=80)

    def provera(self,event):
        podaci=[]
        uneto=self.pretraga_label.get()
        if uneto == '':
            self.prikaz_listbox.delete(0, 'end')
            self.azuriraj_lek()

        else:

            z=ucitaj_lek()
            for i in z:
                if uneto.lower() in i["Naziv"].lower() or uneto.lower() in i["Proizvodjac"].lower():
                    podaci.append(i)

            self.prikaz_listbox.delete(0, 'end')
            for j in podaci:

                self.prikaz_listbox.insert('end',j["Naziv"]+" "+j["Proizvodjac"])

    def dozvola(self,event):
        if self.podacioleku[self.prikaz_listbox.curselection()[0]] != []:
            self.dodaj_dugme4["state"] = "active"
            self.dodaj_dugme2["state"] = "active"
            self.dodaj_dugme3['state'] = 'active'
            self.dodaj_dugme5['state'] = 'active'
        else:
            self.dodaj_dugme4["state"] = "disabled"
            self.dodaj_dugme2["state"] = "disabled"
            self.dodaj_dugme3['state'] = "disabled"
            self.dodaj_dugme5['state'] = "disabled"



    def __init__(self,master):
                self.master= master

                master.title("LEK")
                master.geometry("1000x650")
                self.okvir = Frame(master)
                self.okvir.pack()

                unosFrame = Frame(self.master, bd=4, relief="solid", bg="peach puff")
                unosFrame.place(x=0, y=0, width=1000, height=800)

                self.okvir = Frame(master)
                self.okvir.pack()

                unosFrame = Frame(self.master, bd=4, relief="solid", bg="peach puff")
                unosFrame.place(x=0, y=0, width=1000, height=800)

                self.l_a = Label(unosFrame, text="LEKOVI", font=("arial", 37, 'bold'),bg='peach puff3')
                self.l_a.place(x=400,y=100)


                self.dodaj_dugme = Button(unosFrame, text='Dodaj', width=15, command=self.dodaj_prozor)
                self.dodaj_dugme.place(x=700,y=500)
                self.dodaj_dugme['state'] = 'active'

                self.dodaj_dugme2= Button(unosFrame,text='Izlaz', width=15,command=self.izlaz)
                self.dodaj_dugme2.place(x=800, y=200)

                self.dodaj_dugme3 = Button(unosFrame, text='Prikaz', width=15, command=self.prikaz)
                self.dodaj_dugme3.place(x=150, y=500)
                self.dodaj_dugme3['state'] = 'disabled'

                self.dodaj_dugme4=Button(unosFrame,text='Obrisi', width=15,command=self.obrisi)
                self.dodaj_dugme4.place(x=415,y=230)
                self.dodaj_dugme4['state'] = 'disabled'

                self.dodaj_dugme5=Button(unosFrame,text='Izmena', width=15, command=self.izmena)
                self.dodaj_dugme5.place(x=415,y=500)
                self.dodaj_dugme5['state']='disabled'



                self.pretraga=Label(unosFrame, text="PRETRAGA", font=("Al Tarikh", 12, 'bold'),bg='peach puff2')
                self.pretraga.place(x=100,y=230)
                self.pretraga_label = Entry(unosFrame, font=("ariel", 12))
                self.pretraga_label.place(x=100,y=260)

                self.pretraga_label.bind("<KeyRelease>",self.provera)

                self.prikaz_listbox=Listbox(unosFrame,width=50)
                self.prikaz_listbox.place(x=100,y=300)
                self.prikaz_listbox.bind("<<ListboxSelect>>",self.dozvola)

                self.azuriraj_lek()
from tkinter import ttk
from datetime import date
class prozor_recepti:
    def izlaz(self):
        self.master.destroy()



    def comboxcilck(self, event):
        trenutni=self.combobox.current()
        brojac=0
        for i in ucitaj_pacijente():
            if brojac==trenutni:
                self.trenutnipacijent=i
                break

            else:
                brojac=brojac+1
        lista=[]
        lista.append(self.trenutnipacijent)
        brojac=0
        for j in lista:
            for m in j:
                if m=='ReceptPac':
                    receptpacijent = j["ReceptPac"]
                    brojac=brojac+1
        if brojac==0:
            messagebox.showwarning("Greska","Ovaj pacijent jos uvek nema nijedan recpet!")
            self.izlaz()

        recepti = ucitaj_recepte()
        lekar=ucitaj_lekara()
        pacijent=ucitaj_pacijente()
        lista2 = []
        lista2.append(recepti)
        self.trenutnirecept=[]
        self.prikaz_listbox.delete(0,'end')
        for l in recepti:
            if l["ReceptPac"]==receptpacijent:
                recept={
                    "ReceptPac":l["ReceptPac"],
                    "Datum izdavanja":l["Datum izdavanja"],
                    "Izvestaj":l["Izvestaj"],
                    "ReceptLekar":l["ReceptLekar"],
                    "ReceptLek":l["ReceptLek"],
                    "Kolicina":l["Kolicina"]
                }
                self.trenutnirecept.append(recept)

                self.prikaz_listbox.insert('end',l)

    def prikaz(self):
        receptpac=0
        self.trenutni_recept = self.trenutnirecept[self.prikaz_listbox.curselection()[0]]
        lista=[]
        lista.append(self.trenutni_recept)
        for i in lista:

            receptpac=i["ReceptPac"]
            receptlekar=i["ReceptLekar"]
            receptlek=i["ReceptLek"]
            datum=i["Datum izdavanja"]
            izvestaj=i["Izvestaj"]
            kolicina=i["Kolicina"]
        print(receptpac)
        pacijent=ucitaj_pacijente()
        lek=ucitaj_lek()
        lekar=ucitaj_lekara()
        for p in pacijent:
            for q in p:
                if q =='ReceptPac':
                    if p["ReceptPac"]==receptpac:

                        imepacijenta=p['Prezime']+" "+p["Ime"]
                        lbo=p["LBO"]
        for l in lekar:
            for t in l:
                if t=='ReceptLekar':
                    if l["ReceptLekar"]==receptlekar:
                        imelekar=l["Prezime"]+" "+l["Ime"]
        for le in lek:
            for s in le:
                if s=='ReceptLek':
                    if le["ReceptLek"]==receptlek:
                        imeleka=le["Naziv"]+", "+le["Proizvodjac"]

        pozadina3 = Frame(self.master, bg='lemon chiffon', width=300, height=150)
        pozadina3.place(x=550, y=300, width=330, height=170)

        izvestaj_label = Label(pozadina3, text='Izvestaj: ', bg='peachpuff2')
        izvestaj_label.grid(row=6, column=0, sticky=W, padx=10)
        self.izvestaj_entry = Entry(pozadina3, bg='white', width=30)
        self.izvestaj_entry.grid(row=6, column=1)
        self.izvestaj_entry.insert(-1, izvestaj)
        self.izvestaj_entry["state"] = "disabled"

        kolicina_label = Label(pozadina3, text='Kolicina: ', bg='peachpuff2')
        kolicina_label.grid(row=5, column=0, sticky=W, padx=10)
        self.kolicina_entry = Entry(pozadina3, bg='white', width=30)
        self.kolicina_entry.grid(row=5, column=1)
        self.kolicina_entry.insert(-1, kolicina)
        self.kolicina_entry["state"] = "disabled"


        datum_label = Label(pozadina3, text='Datum izdavanja leka: ', bg='peachpuff2')
        datum_label.grid(row=4, column=0, sticky=W, padx=10)
        self.datum_entry = Entry(pozadina3, bg='white', width=30)
        self.datum_entry.grid(row=4, column=1)
        self.datum_entry.insert(-1, datum)
        self.datum_entry["state"] = "disabled"

        lek_label = Label(pozadina3, text='Naziv i proizodjac leka: ', bg='peachpuff2')
        lek_label.grid(row=3, column=0, sticky=W, padx=10)
        self.lek_entry = Entry(pozadina3, bg='white', width=30)
        self.lek_entry.grid(row=3, column=1)
        self.lek_entry.insert(-1, imeleka)
        self.lek_entry["state"] = "disabled"

        lekar_label = Label(pozadina3, text='Ime i prezime lekara: ', bg='peachpuff2')
        lekar_label.grid(row=2, column=0, sticky=W, padx=10)
        self.lekar_entry = Entry(pozadina3, bg='white', width=30)
        self.lekar_entry.grid(row=2, column=1)
        self.lekar_entry.insert(1, imelekar)
        self.lekar_entry["state"] = "disabled"

        pacijent_label = Label(pozadina3, text='Ime i prezime pacijenta: ', bg='peachpuff2')
        pacijent_label.grid(row=1, column=0, sticky=W, padx=10)
        self.pacijent_entry = Entry(pozadina3, bg='white', width=30)
        self.pacijent_entry.grid(row=1, column=1)
        self.pacijent_entry.insert(-1, imepacijenta)
        self.pacijent_entry["state"] = "disabled"

        lbo_label = Label(pozadina3, text='LBO: ', bg='peachpuff2')
        lbo_label.grid(row=0, column=0, sticky=W, padx=10)
        self.lbo_entry = Entry(pozadina3, bg='white', width=30)
        self.lbo_entry.grid(row=0, column=1)
        self.lbo_entry.insert(-1, lbo)
        self.lbo_entry["state"] = "disabled"

    def obrisi(self):


            Provera = messagebox.askquestion('Upozorenje', 'Da li zelite da obriste recept?')

            if Provera == 'yes':
                self.trenutni_recept =self.trenutnirecept[ self.prikaz_listbox.curselection()[0]]
                recept = ucitaj_recepte()

                test = []
                test.append(self.trenutni_recept)

                for i in test:
                    izvestaj = i["Izvestaj"]
                    datum=i["Datum izdavanja"]
                for j in recept:
                    if j["Izvestaj"] == izvestaj and j["Datum izdavanja"]==datum:
                        recept.remove(j)
                print(recept)
                sacuvaj_recepte(recept)
                self.prikaz_listbox.delete(ANCHOR)
            else:
                self.izlaz()
    def izlaz2(self):
        self.prozor1.destroy()

    def cuvanje_dodavanja(self):
        pac=ucitaj_pacijente()
        pacijent=self.listap
        lekar=self.listal
        lek=self.listalek
        kolicina=self.kolicina
        izvestaj=self.labela5entry.get()
        datumdanas=str(date.today())
        maxpac=1
        brojac=0
        for p in pacijent:
            for k in p:

                if "ReceptPac"==k:
                    receptpac=p["ReceptPac"]

                    brojac=1


                else:

                    for i in pac:
                        for t in i:
                            if t == "ReceptPac":
                                if i["ReceptPac"]>=maxpac:
                                    maxpac=i["ReceptPac"]
                    receptpac=maxpac+1

                    ime=p["Ime"]
                    prezime=p["Prezime"]
                    datum=p["Datum"]
                    jmbg=p["JMBG"]
                    lbo=p["LBO"]
                    korisnik={
                        "Ime":ime,
                        "Prezime":prezime,
                        "Datum":datum,
                        "JMBG":jmbg,
                        "LBO":lbo,
                        "ReceptPac":receptpac
                    }
        if brojac==0:
            for l in pac:
                if jmbg == l["JMBG"]:
                        pac.remove(l)
            pac.append(korisnik)
            sacuvaj_pacijente(pac)


        maxlekar = 1
        brojac2=0
        leka = ucitaj_lekara()
        for p1 in lekar:
            for k1 in p1:
                if "ReceptLekar" in k1:
                    receptlekar = p1["ReceptLekar"]
                    brojac2=1

                else:
                    for i1 in leka:
                        for t1 in i1:
                            if t1 == "ReceptLekar":
                                if i1["ReceptLekar"] >= maxlekar:
                                    maxlekar = i1["ReceptLekar"]
                    receptlekar = maxlekar+1

                    ime1 = p1["Ime"]
                    prezime1 = p1["Prezime"]
                    datum1 = p1["Datum"]
                    jmbg1 = p1["JMBG"]
                    lbo1 = p1["Specijalizacija"]
                    korisnik1 = {
                        "Ime": ime1,
                        "Prezime": prezime1,
                        "Datum": datum1,
                        "JMBG": jmbg1,
                        "Specijalizacija": lbo1,
                        "ReceptLekar": receptlekar
                    }
        if brojac2==0:
            for l1 in leka:
                if jmbg1 == l1["JMBG"]:
                        leka.remove(l1)
            leka.append(korisnik1)
            sacuvaj_lekara(leka)
        print(receptlekar)
        maxlek = 1
        brojac = 0
        pac=ucitaj_lek()
        for p in lek:
            for k in p:

                if "ReceptLek" == k:
                    receptlek = p["ReceptLek"]

                    brojac = 1


                else:

                    for i in pac:
                        for t in i:
                            if t == "ReceptLek":
                                if i["ReceptLek"] >= maxlek:
                                    maxlek = i["ReceptLek"]
                    receptlek = maxlek + 1

                    ime = p["Naziv"]
                    prezime = p["Proizvodjac"]
                    datum = p["Tip leka"]
                    jmbg = p["JKL"]

                    korisnik = {
                        "Naziv": ime,
                        "Proizvodjac": prezime,
                        "Tip leka": datum,
                        "JKL": jmbg,

                        "ReceptLek": receptlek
                    }
        if brojac == 0:
            for l in pac:
                if jmbg == l["JKL"]:
                    pac.remove(l)
            pac.append(korisnik)
            sacuvaj_lek(pac)
        recept={
            "ReceptPac":receptpac,
            "ReceptLekar":receptlekar,
            "ReceptLek":receptlek,
            "Datum izdavanja":datumdanas,
            "Kolicina":kolicina,
            "Izvestaj":izvestaj
        }
        recepti=ucitaj_recepte()
        recepti.append(recept)
        sacuvaj_recepte(recepti)
    def combopacijent(self,event):
        trenutni = self.comboboxpacijent.current()
        brojac = 0
        for i in ucitaj_pacijente():
            if brojac == trenutni:
                self.trenutnipacijent = i
                break

            else:
                brojac = brojac + 1
        self.listap = []
        self.listap.append(self.trenutnipacijent)



    def combolekar(self,event):
        trenutni = self.comboboxlekar.current()
        brojac = 0
        for i in ucitaj_lekara():
            if brojac == trenutni:
                self.trenutnilekar = i
                break

            else:
                brojac = brojac + 1
        self.listal = []
        self.listal.append(self.trenutnilekar)

    def combolek(self,event):
        trenutni = self.comboboxlek.current()
        brojac = 0
        for i in ucitaj_lek():
            if brojac == trenutni:
                self.trenutnilek = i
                break

            else:
                brojac = brojac + 1
        self.listalek = []
        self.listalek.append(self.trenutnilek)
    def combokolicina(self,event):
        self.kolicina=self.comboboxkolicina.current()+1

    def dodaj(self):
        self.prozor1 = Tk()
        prozor1 = self.prozor1
        prozor1.title("Izmena")
        prozor1.geometry("700x400")
        self.okvir = Frame(prozor1)
        self.okvir.pack()

        unosFrame = Frame(self.prozor1, bd=1, relief="solid", bg="LightBlue1")
        unosFrame.place(x=0, y=0, width=700, height=400)

        self.dugme = Button(unosFrame, text='Izlaz', width=15, command=self.izlaz2)
        self.dugme.place(x=250, y=310)

        self.dugme2 = Button(unosFrame, text='Sacuvaj', width=15, command=self.cuvanje_dodavanja)
        self.dugme2.place(x=500, y=150)

        self.labela = Label(unosFrame, text='Odaberite pacijenta', bg='white', font=("arial", 12))
        self.labela.place(x=20, y=50)
        self.labela2 = Label(unosFrame, text='Odaberite lekara', bg='white', font=("arial", 12))
        self.labela2.place(x=20, y=90)
        self.labela3= Label(unosFrame, text='Odaberite lek', bg='white', font=("arial", 12))
        self.labela3.place(x=20, y=130)
        self.labela4 = Label(unosFrame, text='Odaberite kolicinu leka', bg='white', font=("arial", 12))
        self.labela4.place(x=20, y=170)

        self.labela5 = Label(unosFrame, text='Izvestaj', bg='white', font=("arial", 12))
        self.labela5.place(x=20, y=210)
        self.labela5entry=Entry(unosFrame,bg='white',width=30)
        self.labela5entry.place(x=200,y=210)

        self.comboboxpacijent = ttk.Combobox(unosFrame, values=ucitaj_pacijente(), width=30, state='readonly')
        self.comboboxpacijent.place(x=200, y=50)
        self.comboboxpacijent.bind("<<ComboboxSelected>>", self.combopacijent)

        self.comboboxlekar = ttk.Combobox(unosFrame, values=ucitaj_lekara(), width=30, state='readonly')
        self.comboboxlekar.place(x=200, y=90)
        self.comboboxlekar.bind("<<ComboboxSelected>>", self.combolekar)

        self.comboboxlek = ttk.Combobox(unosFrame, values=ucitaj_lek(), width=30, state='readonly')
        self.comboboxlek.place(x=200, y=130)
        self.comboboxlek.bind("<<ComboboxSelected>>", self.combolek)
        kolicina=[1,2,3,4,5,6,7,8,9,10]
        self.comboboxkolicina = ttk.Combobox(unosFrame, values=kolicina, width=30, state='readonly')
        self.comboboxkolicina.place(x=200, y=170)
        self.comboboxkolicina.bind("<<ComboboxSelected>>", self.combokolicina)


    def dozvola(self,event):

            self.dodaj_dugme4["state"] = "active"

            self.dodaj_dugme3['state'] = 'active'











    def __init__(self,master):
        self.master= master

        master.title("Recepti")
        master.geometry("1000x650")
        self.okvir = Frame(master)
        self.okvir.pack()

        unosFrame = Frame(self.master, bd=4, relief="solid", bg="peach puff")
        unosFrame.place(x=0, y=0, width=1000, height=800)

        self.l_a = Label(unosFrame, text="RECEPTI", font=("arial", 37, 'bold'), bg='peach puff3')
        self.l_a.place(x=400, y=100)

        self.dodaj_dugme2 = Button(unosFrame, text='Izlaz', width=15, command=self.izlaz)
        self.dodaj_dugme2.place(x=800, y=200)

        self.prikaz_listbox = Listbox(unosFrame, width=50)
        self.prikaz_listbox.place(x=100, y=300)

        self.dodaj_dugme3=Button(unosFrame,text='Prikaz',width=15,command=self.prikaz)
        self.dodaj_dugme3.place(x=250,y=500)

        self.dodaj_dugme4=Button(unosFrame,text='Obrisi',width=15,command=self.obrisi)
        self.dodaj_dugme4.place(x=450 , y=230)

        self.dodaj_dugme1=Button(unosFrame,text='Dodaj',width=15,command=self.dodaj)
        self.dodaj_dugme1.place(x=650,y=500)
        self.dodaj_dugme3['state']='disable'
        self.dodaj_dugme4['state']='disable'


        self.labela=Label(unosFrame,text='Odaberite pacijenta',bg='peach puff3',font=("arial", 12))
        self.labela.place(x=120,y=200)

        self.prikaz_listbox.bind("<<ListboxSelect>>", self.dozvola)

        self.combobox=ttk.Combobox(unosFrame,values= ucitaj_pacijente(),width=30,state='readonly')
        self.combobox.place(x=120,y=230)
        self.combobox.bind("<<ComboboxSelected>>", self.comboxcilck)
        self.combobox.current(0)











if __name__ == "__main__":
    main()

