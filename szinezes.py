from sty import fg

""" Bővebb információ és példák az sty modul használatáról itt:
https://pypi.org/project/sty/ """

class Szin:
    def __init__(self, colour, r, g, b):
        self.colour = colour
        self.r = r
        self.g = g
        self.b = b
    def __str__(self):
        return f"{self.colour}"
    
szinek = [
Szin("zöld", 10, 255, 10),
Szin("piros", 255, 10, 10),
Szin("kék", 0, 100, 255),
Szin("lila", 191, 62, 255),
Szin("sarga", 255, 255, 0),
Szin("feher", 255, 255 , 255)
]

zold = fg(szinek[0].r, szinek[0].g, szinek[0].b)
piros = fg(szinek[1].r, szinek[1].g, szinek[1].b)
kek = fg(szinek[2].r, szinek[2].g, szinek[2].b)
lila = fg(szinek[3].r, szinek[3].g, szinek[3].b)
sarga = fg(szinek[4].r, szinek[4].g, szinek[4].b)
feher = fg(szinek[5].r, szinek[5].g, szinek[5].b)