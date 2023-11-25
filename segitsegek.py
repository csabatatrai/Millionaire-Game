import random
from szinezes import zold,piros,sarga,feher

def telefon(megfejtes, nehezseg):
    """A bemenetén a kérdésre adandó jó választ és a kérdés nehézségét várja,
    hiszen ezek függvényében tud a közönség választ adni a kérdésre. Minél könnyebb egy kérdés,
    annál nagyobb eséllyel kap a játékos jó választ a közönségtől."""

    jo_valasz = random.randint(50-nehezseg*5, 100)
    rossz_valasz1 = random.randint(0, (100-jo_valasz))
    rossz_valasz2 = random.randint(0, (100-jo_valasz-rossz_valasz1))
    rossz_valasz3 = 100-jo_valasz-rossz_valasz1-rossz_valasz2 # későbbi felhasználásra maradt benne, hogy árnyaltabb válaszokat adhasson a telefonos segítség

    if megfejtes == "A":
        if jo_valasz > 50:
            print(zold+"\nBiztos vagyok benne, hogy A lesz a jó válasz!\n")

        else:
            print(piros+"\nNe haragudj, de ezt most nem tudom\n")

    elif megfejtes == "B":
        if jo_valasz > 50:
            print(zold+"\nBiztos vagyok benne, hogy B lesz a jó válasz!\n")
        else:
            print(piros+"\nNe haragudj, de ezt most nem tudom\n")

    elif megfejtes == "C":
        if jo_valasz > 50:
            print(zold+"\nBiztos vagyok benne, hogy C lesz a jó válasz!\n")
        else:
            print(piros+"\nNe haragudj, de ezt most nem tudom\n")

    elif megfejtes == "D":
        if jo_valasz > 50:
            print(zold+"\nBiztos vagyok benne, hogy D lesz a jó válasz!\n")
        else:
            print(piros+"\nNe haragudj, de ezt most nem tudom\n")

def kozonseg(megfejtes,nehezseg):
    """A bemenetén a kérdésre adandó jó választ és a kérdés nehézségét várja,
    hiszen ezek függvényében tud a közönség választ adni a kérdésre. Minél könnyebb egy kérdés,
    annál nagyobb eséllyel kap a játékos jó választ a közönségtől."""

    jo_valasz = random.randint(50-nehezseg*10,100)
    rossz_valasz1 = random.randint(0,(100-jo_valasz))
    rossz_valasz2 = random.randint(0,(100-jo_valasz-rossz_valasz1))
    rossz_valasz3 = 100-jo_valasz-rossz_valasz1-rossz_valasz2

    if megfejtes == "A":
        print(sarga+f"A válasz:",jo_valasz*"|") # feltételezve, hogy A volt helyes
        print(f"B válasz:",rossz_valasz1*"|")
        print(f"C válasz:",rossz_valasz2*"|")
        print(f"D válasz:", rossz_valasz3*"|")

    elif megfejtes == "B":
        print(sarga+f"A válasz:",rossz_valasz1*"|")
        print(f"B válasz:",jo_valasz*"|")
        print(f"C válasz:",rossz_valasz2*"|")
        print(f"D válasz:", rossz_valasz3*"|")

    elif megfejtes == "C":
        print(sarga+f"A válasz:",rossz_valasz1*"|")
        print(f"B válasz:",rossz_valasz2*"|")
        print(f"C válasz:",jo_valasz*"|")
        print(f"D válasz:", rossz_valasz3*"|")

    elif megfejtes == "D":
        print(sarga+f"A válasz:",rossz_valasz1*"|")
        print(f"B válasz:",rossz_valasz2*"|")
        print(f"C válasz:",rossz_valasz3*"|")
        print(f"D válasz:", jo_valasz*"|") 

def kvizmester(megfejtes):
    """Szándékosan nincs az inputra hibakezelés!
    Ez egy olyan csalás a játékon belül, ami ugyan bármennyiszer használható, de frusztráló lehet a használata,
    mivel szerencse kell hozzá, hogy működjön. A hesoyam egy cheat kód, amivel garantáltan 
    kapható helyes válasz a kvízmestertől, ha eljut a játékos az input bekéréséig.
    
    Illetve van benne egy easter egg is, ami csak a forráskód ismeretében hívható elő: 98. sor """

    rng = random.randint(1, 2)
    if rng == 1:
        print(feher+"Sajnálom, tudja, hogy nem segíthetek. Bár...")
    if rng == 2:
        print(feher+"Nem segíthetnék, de tudja mit, feldobok egy érmét, ha eltalálja, hogy fej vagy írás, megmondom a megfejtést!")
        tipp = input("Fej vagy írás? ")
        if tipp == "fej":
            tipp = 1
        elif tipp == "írás":
            tipp = 2
        elif tipp != "fej" or tipp != "írás" and tipp != "hesoyam":
            print(piros+"Eljátszotta az esélyét!")
        # fej = 1
        # iras = 2
        fej_vagy_iras = random.randint(1, 2)
        if tipp == fej_vagy_iras:
            print(zold+f"Ma szerencsés napja van, ugyan nincs a monitoromon a megfejtés, de a jó válasz: {megfejtes}")
        elif tipp == "Mit szólna, ha a nyereményt feleznénk?": # forráskód nélkül felfedezhetetlen easter egg
            print(piros+"Erre még visszatérünk.")
        elif tipp == ("hesoyam"):
            print(piros+f"Szóval így állnuk - felelte kacsintva. Megfejtés: {megfejtes}")
        else:
            print(sarga+"Sajnos lemerült a kijelzőm, így nem tudom megmondani a megfejtést önnek.")
            print(zold+"Játékos: jó kifogás.")