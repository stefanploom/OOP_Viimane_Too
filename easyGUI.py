from easygui import *
import random

# 8x8 labürint: 1 = saab minna, 0 = sein
laburint = [
    [1,1,0,1,1,1,1,1],
    [1,1,1,1,0,0,0,1],
    [0,1,0,0,0,1,0,1],
    [0,1,0,0,1,1,1,1],
    [1,1,1,0,1,0,1,0],
    [1,0,1,0,1,0,0,0],
    [1,0,0,0,1,1,1,1],
    [1,1,1,1,1,0,0,0]
]

# Algpositsioon
x = 0  # veerg
y = 0  # rida

liikumine = ["üles", "paremale", "vasakule", "alla"]

#Tegelase asukoht
def kuva_asukoht():
    msgbox(f"Oled ruudus ({x+1}, {y+1})  (rida, veerg)")

kuva_asukoht()
vajutati = buttonbox("Valige kuhu liikuda:", choices=liikumine)

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
    # Kontrollime, et kas oleme väljaspool 8x8 või seina peal
    if x < 0 or x > 7 or y < 0 or y > 7 or laburint[y][x] == 0:
        msgbox("Sinna ei saa minna!")
        x, y = vana_x, vana_y  # taastame vana asukoha
    else:
        kuva_asukoht()

    vajutati = buttonbox("Valige kuhu liikuda:", choices=liikumine)

# Võit kui pääsed labürindist   
if x == 2 and y == 1:
        print("Põgenesite labürindist!")
        exit