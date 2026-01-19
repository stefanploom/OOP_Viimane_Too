from easygui import *
import sys

class Karakter:
    def __init__(self, nimi, elud: int, tugevus: int):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kogus: int):
        self.elud -= kogus

    def lisaElusi(self, kogus: int):
        self.elud += kogus


class Vaenlane:
    def __init__(self, elud: int, tugevus: int):
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kogus: int):
        self.elud -= kogus


laburint = [
    [1,1,0,1,1,1,1,1],
    [1,1,1,1,0,0,0,1],
    [0,1,0,0,0,1,0,1],
    [0,1,0,0,1,1,1,1],
    [1,1,1,0,1,0,1,0],
    [1,0,1,0,1,0,0,0],
    [1,0,0,0,1,1,1,1], # Siin on võit x=7, y=6
    [1,1,1,1,1,0,0,0]
]

mangija = Karakter("Kangelane", 20, 5)
vaenlane1 = Vaenlane(10, 3)
vaenlane2 = Vaenlane(15, 4)

vaenlased = {(1, 2): vaenlane1, (6, 6): vaenlane2}

x = 0
y = 0

liikumine = ["üles", "alla", "vasakule", "paremale"]

while True:
    msgbox(f"Asukoht ({y+1}, {x+1})\nElud: {mangija.elud}")
    valik = buttonbox("Vali suund:", choices=liikumine)
    vana_x, vana_y = x, y

    if valik == "üles":
        y -= 1
    elif valik == "alla":
        y += 1
    elif valik == "vasakule":
        x -= 1
    elif valik == "paremale":
        x += 1
    else:
        sys.exit()

    if x < 0 or x > 7 or y < 0 or y > 7 or laburint[y][x] == 0:
        msgbox("Sinna ei saa minna!")
        x, y = vana_x, vana_y
        continue

    if x == 7 and y == 6:
        msgbox("Põgenesite labürindist!")
        sys.exit()

    if (x, y) in vaenlased:
        v = vaenlased[(x, y)]
        mangija.kaotaElusi(v.tugevus)
        v.kaotaElusi(mangija.tugevus)

        if v.elud <= 0:
            msgbox("Vaenlane suri")
            del vaenlased[(x, y)]

        if mangija.elud <= 0:
            msgbox("Sa surid")
            sys.exit()
