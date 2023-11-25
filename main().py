import time
import segitsegek
from szinezes import zold,piros,kek,lila,sarga,feher
import kerdesek

start = time.time()

class Toplista_sor:

    def __init__(self, jatekosnev, nyeremeny, jatekido):
        self.jatekosnev = jatekosnev
        self.nyeremeny = int(nyeremeny.replace(" ", "")) # egésszé alakítja az összehasonlíthatósághoz az elért nyereményt
        self.jatekido = float(jatekido)
    
    def __str__(self):
        return f"\t{self.jatekosnev:8}\t{self.nyeremeny:11}\t{round(self.jatekido):12}s\n"

class Toplista:

    def __init__(self, fajlnev):
        self.fajlnev = fajlnev
        self.sorok = []
        self.beolvas()

    def beolvas(self):
        """Korábbi játékok eredményeit beolvassa"""
        with open("toplista.txt", "r", encoding="utf-8") as fajl:
            next(fajl)
            for sor in fajl:
                sor = sor.split("\t")
                self.sorok.append(Toplista_sor(sor[3], sor[4], sor[5].replace("s\n", "")))

    def kiir(self):
        """Újraírja a toplista.txt-t az új eredményekkel"""
        self.sorok = sorted(self.sorok, key=lambda x: x.nyeremeny, reverse=True)
        with open("toplista.txt", "w", encoding="utf-8") as fajl:
            fajl.write("helyezés\tjátékosnév\t\tnyeremény\t\tjátékidő\n")  # fejléc
            for idx, i in enumerate(self.sorok, start=1):
                fajl.write(f"\t{idx}\t" + str(i))
                
    def hozzaad(self, toplista_sor):
        """Hozzáadja a jelenlegi játék végeredményét a toplistához"""
        self.sorok.append(toplista_sor)
        self.kiir()

    def megjelenit(self):
        """Az aktuális toplista kiíratása konzolra"""
        for idx, i in enumerate(self.sorok, start=1):
            print(f"{idx}. {i}")

def fomenu():  # ❗printnél nem kellett returnt megadni! így is működik
    print(lila+"Válasszon menüpontot egy szám megadásával!",
          sarga+"1. Új játék",
          sarga+"2. Toplista",
          sarga+"3. Játékosnév megadása",
          sarga+"4. Kilépés\n", sep="\n")

nyeremenyek_sztringkent = ["5000", "10 000", "25 000", "50 000", "100 000",
                           "200 000", "300 000", "500 000", "800 000", "1 500 000",
                           "3 000 000", "5 000 000", "10 000 000", "20 000 000", "40 000 000"]


def jatszhat_e_tovabb(userinput,tizenot_kerdes,kerdes_idx): # main-ben van ez a változó, nem globális
    """Eldönti, hogy a játékos helyes választ adott-e a kérdésre és jogosult-e a további játékra"""
    if userinput == 1: # megjelöl A
        felelet = "A"
        if tizenot_kerdes[kerdes_idx].megfejtes == felelet:
            print(zold + "A válasz helyes!\n")
            return True
        else:
            print(piros + "Rossz válasz!\n")
            return False
    elif userinput == 2: # megjelöl B
        felelet = "B"
        if tizenot_kerdes[kerdes_idx].megfejtes == felelet:
            print(zold + "A válasz helyes!\n")
            return True
        else:
            print(piros + "Rossz válasz!\n")
            return False
    elif userinput == 3: # megjlelöl C
        felelet = "C"
        if tizenot_kerdes[kerdes_idx].megfejtes == felelet:
            print(zold + "A válasz helyes!\n")
            return True
        else:
            print(piros + "Rossz válasz!\n")
            return False
    elif userinput == 4: # megjelöl D
        felelet = "D"
        if tizenot_kerdes[kerdes_idx].megfejtes == felelet:
            print(zold + "A válasz helyes!\n")
            return True
        else:
            print(piros + "Rossz válasz!\n")
            return False


def main():
    jatekosnev = "Játékos"
    nyeremeny = "0"
    rendezett = kerdesek.rendezett_kerdesek()
    indexek = kerdesek.indexlista(rendezett)
    tizenot_kerdes = kerdesek.minden_nehezsegbol_egy(rendezett,indexek)
    toplista = Toplista("toplista.txt")
    van_felezes = True
    van_telefon = True
    van_kozonseg = True

    while True:
        # jatek = minden_nehezsegbol_egy(rendezett,indexlist)
        fomenu()
        try:
            userinput = int(input())
            if userinput == 1: # új játék
                kerdes_idx = 0 # ez a kérdés sorszáma és egyben a nehézségét is jelöli (magasbb index magasabb nehézség)
                while kerdes_idx < 16:
                    print(lila + str(tizenot_kerdes[kerdes_idx]))
                    try:
                        userinput = int(input())
                        if 0 < userinput < 5:
                            if jatszhat_e_tovabb(userinput,tizenot_kerdes,kerdes_idx):
                                nyeremeny = nyeremenyek_sztringkent[kerdes_idx]
                                kerdes_idx += 1 # ha tovább játszhat, nőjön a nehézség (vagyis egy index-szel lépjünk előrébb a tizenot_kerdes nevű listában)
                                continue
                            else:
                                break
                        elif userinput == 5 and van_telefon: # segítség: telefon
                            segitsegek.telefon(tizenot_kerdes[kerdes_idx].megfejtes,tizenot_kerdes[kerdes_idx].nehezseg)
                            van_telefon = False
                        elif userinput == 6 and van_kozonseg: # segítség: közönség
                            segitsegek.kozonseg(tizenot_kerdes[kerdes_idx].megfejtes,tizenot_kerdes[kerdes_idx].nehezseg)
                            van_kozonseg = False
                        elif userinput == 7 and van_felezes: # segítség: felezés
                            tizenot_kerdes[kerdes_idx].felezes()
                            van_felezes = False
                        elif userinput == 8: # segítség: kvízmeseter
                            segitsegek.kvizmester(tizenot_kerdes[kerdes_idx].megfejtes)
                        elif userinput == 9: # kilépés
                            print(feher+"A játékos időnek vége")
                            break
                    except:
                        pass # így rossz bemenet (pl. sztring, ami nem konvertálható egésszé ugye) esetén is zavartalanul folytatható a játék
            elif userinput == 2: # toplista: fájlkezelés, kiírás ❗
                toplista.megjelenit()
            elif userinput == 3: # játékosnév
                jatekosnev = input("Adjon meg új játékosnevet: \n")
            elif userinput == 4: # kilépés
                break # ❗
        except:
            pass # ne csináljon semmit rossz bemenetre, hogy folytatódhasson a játék!
    
    print(zold+f"Gratulálok {jatekosnev}, az ön nyereménye: " + piros + nyeremeny + " forint! ")
    stop = time.time()
    eltelt_ido = stop-start
    toplista.hozzaad(Toplista_sor(jatekosnev,nyeremeny,eltelt_ido))
    print(kek + f"Játékban töltött idő: {round(eltelt_ido,2)} sec")

main()





