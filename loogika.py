from easygui import *
import sys

# ---- KLASSID ----

class Karakter:
    def __init__(self, nimi, elud:int, tugevus:int):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kogus:int):
        self.elud -= kogus
        msgbox(f"{self.nimi} kaotas {kogus} elu! Alles on {self.elud} elupunkti.")
        if self.elud <= 0:
            msgbox(f"{self.nimi} suri! Mäng läbi.")
            sys.exit()

    def lisaElusi(self, kogus:int):
        self.elud += kogus
        msgbox(f"{self.nimi} sai juurde {kogus} elu! Nüüd on {self.elud} elupunkti.")


class Vaenlane:
    def __init__(self, elud:int, tugevus:int):
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kogus:int):
        self.elud -= kogus
        if self.elud > 0:
            msgbox(f"Vaenlane kaotas {kogus} elu! Tal on alles {self.elud}.")
        else:
            msgbox("Vaenlane suri!")

# ---- KARAKTERITE LOOMINE ----

nimi = enterbox("Sisesta oma tegelase nimi:")
elud = enterbox("Sisesta oma tegelase elud:")
tugevus = enterbox("Sisesta oma tegelase tugevus:")

mangija = Karakter(nimi, elud, tugevus)

v1 = Vaenlane(elud=10, tugevus=2)
v2 = Vaenlane(elud=15, tugevus=3)

# ---- VAENLASTE ASUKOHAD LABÜRINDIS ----
# (rida, veerg)
vaenlased = {
    (1, 2): v1,
    (5, 2): v2
}

# ---- LABÜRINDI LOOGIKA ----

laburint = [
    [1,0,0,1,1,1,1,1],
    [1,1,1,1,0,0,0,1],
    [0,1,0,0,0,1,0,1],
    [0,1,0,0,1,1,1,1],
    [1,1,1,0,1,0,1,0],
    [1,0,1,0,1,0,0,0],
    [1,0,0,0,1,1,1,1],
    [1,1,1,1,1,0,0,0]
]

x = 0
y = 0

liikumine = ["üles", "paremale", "vasakule", "alla"]

def kuva_asukoht():
    msgbox(f"Oled ruudus ({x+1}, {y+1}) (rida, veerg)")

kuva_asukoht()
vajutati = buttonbox("Vali kuhu liikuda:", choices=liikumine)

while True:
    vana_x, vana_y = x, y

    if vajutati == "üles":
        y -= 1
    elif vajutati == "alla":
        y += 1
    elif vajutati == "paremale":
        x += 1
    elif vajutati == "vasakule":
        x -= 1
    else:
        break

    # kontrollime seina või piiri
    if x < 0 or x > 7 or y < 0 or y > 7 or laburint[y][x] == 0:
        msgbox("Sinna ei saa minna!")
        x, y = vana_x, vana_y
    else:
        kuva_asukoht()

        # Kontrollime, kas seal on vaenlane
        if (y, x) in vaenlased:
            vaenlane = vaenlased[(y, x)]
            msgbox("Sa kohtasid vaenlast! Võitlus algab!")
            mangija.kaotaElusi(vaenlane.tugevus)
            vaenlane.kaotaElusi(mangija.tugevus)

            # Kui vaenlane sureb, eemaldame ta labürindist
            if vaenlane.elud <= 0:
                del vaenlased[(y, x)]

    # Võidu tingimus
    if x == 7 and y == 6:
        msgbox("Sa pääsesid labürindist! Võit!")
        break

    vajutati = buttonbox("Vali kuhu liikuda:", choices=liikumine)

