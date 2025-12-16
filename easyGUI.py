from easygui import *
import random

tegelane = enterbox("Sisestage oma tegelase nimi:")
tugevus = integerbox("Sisestage oma tegelase tugevus:", lowerbound = 1, upperbound = 50)
elupunkt = integerbox("Sisestage oma tegelase elu punktid:", lowerbound = 1, upperbound = 100)
if tegelane == None or tugevus == None or elupunkt == None or tegelane == "":
    msgbox("Palun sisestage õigesti!")
else:
    msgbox(tegelane + " Tugevus: " + str(tugevus) + " Elupunktid: " + str(elupunkt))
    
for _ in iter(int, 1):
    liikumine = ["otse", "paremale", "vasakule", "tagasi"]
    vajutati = buttonbox("Valige kuhu liikuda: ", choices = liikumine)
