# Legyen Ön is Milliomos! - Python Kvízjáték 💰

Ez a projekt a népszerű "Legyen Ön is milliomos!" televíziós vetélkedő terminálos (konzolos) változata, Pythonban megírva. A játék célja, hogy a játékos 15 egyre nehezedő kérdés megválaszolásával elvigye a virtuális főnyereményt.

## 🌟 Funkciók

* **Teljes játékélmény**: 15 db kérdésből álló körök, növekvő nehézségi szintekkel és egyre nagyobb nyereményekkel (5 000 Ft-tól egészen 40 000 000 Ft-ig).
* **4 fajta segítség**:
  * 📞 **Telefonos segítség**: Minél könnyebb a kérdés, annál biztosabb és pontosabb tippet ad a "vonal végén" lévő barát.
  * 👥 **Közönség**: Kiszámolja és sávokba (grafikon-szerűen) rendezi a közönség szavazatait a nehézségtől függően.
  * ✂️ **Felezések**: Véletlenszerűen eltávolít két rossz válaszlehetőséget, csak a helyeset és egy hibásat hagyva bent.
  * 🧔 **Kvízmester (Extra)**: Speciális játékon belüli "csalás" vagy interakció. A kvízmesterrel érmét lehet feldobni a válaszért, de rejtett Easter Egg-eket és Cheat kódokat (`hesoyam`) is tartalmaz a szemfüleseknek!
* **Toplista**: A rendszer a `toplista.txt` fájlban rögzíti és a nyeremény (valamint a játékidő) alapján rangsorolja a játékosokat.
* **Színes terminál output**: Az olvashatóságot és az élményt a színes konzolos szövegek teszik teljessé (zöld a jó válasz, piros a rossz stb.).

## 🛠️ Telepítés és Futtatás

### Előfeltételek
A program futtatásához **Python 3.x** szükséges. 
A színes konzolos megjelenítéshez a játék az `sty` modult használja, ezt telepíteni kell:

```bash
pip install sty
```

## Futtatás

Klónozd le a tárolót (vagy töltsd le a fájlokat).

Nyiss meg egy terminált a projekt mappájában.

Futtasd a fő fájlt:
"main().py"

## 📁 Projekt struktúra
```
main().py: A játék fő ciklusa, a menürendszer és a játékmenet (kérdések léptetése, nyeremények számítása, inputok kezelése) irányítója.

kerdesek.py: Felel a kérdések beolvasásáért a CSV fájlból. Ezekből Kerdes objektumokat készít, majd rendezi őket nehézségi szint szerint és sorsolja az aktuális játék 15 kérdését.

segitsegek.py: A telefonos segítség, a közönségszavazás és a speciális kvízmester segítség logikáját tartalmazza.

szinezes.py: Beállítja a terminálban megjelenő szövegek RGB alapú színeit (zöld, piros, kék, lila, sárga, fehér).

kerdesek_valaszok.csv: A játék adatbázisa, amely a kérdéseket, a válaszlehetőségeket, a helyes válasz betűjelét, a nehézséget és a témakört tartalmazza pontosvesszővel elválasztva.

toplista.txt: Egy szöveges fájl, amelyben az eddigi játékosok pontszámai és eredményei mentődnek.
```

## 🎮 Így játssz!
A játék elindítása után a főmenübe kerülsz, ahol az 1, 2, 3, 4 számgombokkal navigálhatsz. Játék közben az 1-4 számokkal válaszolhatsz a kérdésekre (A, B, C, D), illetve az 5-8 számokkal veheted igénybe a négy különböző segítséget. A program stabil bemenetkezeléssel rendelkezik, egy elgépelés miatt nem fog összeomlani a futás.

Sok sikert és jó szórakozást!
