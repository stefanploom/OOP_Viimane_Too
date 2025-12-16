from easygui import *
import random
tegelane = enterbox("Sisestage oma tegelase nimi:")
tugevus = integerbox("Sisestage oma tegelase tugevus:", lowerbound = 1, upperbound = 50)
elupunkt = integerbox("Sisestage oma tegelase elu punktid:", lowerbound = 1, upperbound = 100)
if tegelane == None or tugevus == None or elupunkt == None or tegelane == "":
    msgbox("Palun sisestage õigesti!")
else:
    msgbox("Tegelase nimi: " + tegelane + " Tugevus: " + str(tugevus) + " Elupunktid: " + str(elupunkt))
    
for _ in iter(int, 1):
    liikumine = ["otse", "paremale", "vasakule", "tagasi"]
    vajutati = buttonbox("Valige kuhu liikuda: ", choices =liikumine)
    if vajutati == "otse":
        vajutati = buttonbox("Liikusite otse, valige kuhu liikuda:", choices =liikumine)
    elif vajutati == "paremale":
        vajutati = buttonbox("Liikusite paremale, valige kuhu liikuda:", choices=liikumine)
    elif vajutati == "vasakule":
        vajutati = buttonbox("Liikusite vasakule, valige kuhu liikuda:", choices=liikumine)
    elif vajutati == "tagasi":
        vajutati = buttonbox("Liikusite tagasi, valige kuhu liikuda:", choices=liikumine)
    