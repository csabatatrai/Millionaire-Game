import csv
import random

class Kerdes:
    
    def __init__(self, nehezseg, kerdes, A, B, C, D, megfejtes, temakor):
        self.nehezseg = int(nehezseg) # ❗fontos a konverzió, különben mikor a kérdések listáját rendezem nehézség szerint, ASCII szerint rendezné őket, 10 ASCII kódja pedig A, ami megelőzné a nála kisebb számokat!
        self.kerdes = kerdes
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.megfejtes = megfejtes
        self.temakor = temakor

    def __str__(self):
        return f"\nÁh, egy kis {self.temakor} ! Na lássuk ezzel hogy bolodogul!\n\n{self.kerdes}\n1.A: {self.A}\n2.B: {self.B}\n3.C: {self.C}\n4.D: {self.D}\n5.telefonos segítség\n6.közönség\n7.felezés\n8.Ön mit jelölne a helyemben?\n9.Kilépés"

    def valasz_jele_jelentesse_alakitas(self,karakter):
        """Hasonló funkciót lát el, mintha egy szótárat írtunk volna, amiben ha
        pl. 'A' sztring a kulcs, a hozzá tartozó érték az 1. lehetséges válasz.
        Azért volt szükség erre a függvényre, mert a kerdesek_valaszok.csv fájlban
        a válasz oszlopban a válasz betűje szerepel, nem pedig szövegesen a jó válasz,
        csak a felezes() függvény használja, táblázatkezelőben Excel függvénnyel is kiváltható
        lett volna, tehát a bemenet átalaktásával, ahogy a kérdések rendezésénél."""
        if karakter == "A":
            return self.A
        elif karakter == "B":
            return self.B
        elif karakter == "C":
            return self.C
        elif karakter == "D":
            return self.D
        
    def felezes(self):
        """Kicserél véletlenszerű két rossz választ üres sztringre"""
        valaszok = [self.A, self.B, self.C, self.D]
        jo_valasz = self.valasz_jele_jelentesse_alakitas(self.megfejtes)
        
        valaszok.remove(jo_valasz) # elveszi a listából, hogy a jó választ ne tudja az üres sztringgé alakítandókból kiszedni

        rossz_valasz = random.choice(valaszok)

        self.A = "" if self.A != jo_valasz and self.A != rossz_valasz else self.A
        self.B = "" if self.B != jo_valasz and self.B != rossz_valasz else self.B
        self.C = "" if self.C != jo_valasz and self.C != rossz_valasz else self.C
        self.D = "" if self.D != jo_valasz and self.D != rossz_valasz else self.D

def rendezett_kerdesek():
    """ 1) Beolvassa fájlból a kérdéseket először létrehoz nekik egy 2 dimenziós listát (kerdeslista nevű lista)
        2) Konvertálja a 2D-s lista részlistáit Kerdes típusú objektumokká (kerdesek nevű lista)
        3) Rendezi a kérdéseket nehézségük szerint majd visszaadja az ezeket tartalmazó listát (rendezett nevű lista)"""

    kerdeslista = []
    with open("kerdesek_valaszok.csv", "r", encoding="utf8") as kerdessor:
        tsv_reader = csv.reader(kerdessor, delimiter=";")

        # ❗első sor átugrása, ami a fejléc
        next(tsv_reader)

        for i in tsv_reader:
            kerdeslista.append(i)

    # ❗ez a lista tartalmazza a Kerdesek() típussá konvertált kérdéseket!
    kerdesek = []
    for i in kerdeslista:
        kerdesek.append(Kerdes(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
    rendezett = sorted(kerdesek, key=lambda x: x.nehezseg, reverse=False) # rosszul rendez, ha nem történt meg a .nehezseg konverziója integerré! olyankor ASCII szerint rakná sorba
    return rendezett

def indexlista(rendezett):
    """Létrehozza az egyes nehézségekhez tartozó indexhatárok listáját, ami segít a sorsolásnál a kívánt nehézség címzéséhez"""

    indexlist = [0] # szükség van a 0-ra is kezdőelemnek, hogy később ciklussal fel lehessen használni ezt a listát 15 kérdés generálására
    for i in range(len(rendezett)-1):
        if rendezett[i].nehezseg != rendezett[i+1].nehezseg:
            indexlist.append(i)
    indexlist.append(len(rendezett)-1) # szükség van a későbbi ciklus megírásához az utolsó elem indexére is
    return  indexlist

def minden_nehezsegbol_egy(rendezett_kerdeslista,indexek):
    """A rendezett kérdéslistából sorsol mind a 15 nehézségből 1 kérdést, hisz 1 játékhoz ennyi szükséges"""
    tizenot = []
    for i in range(14+1):
        idx = random.randint(indexek[i],indexek[i+1])
        tizenot.append(rendezett_kerdeslista[idx])
    return tizenot