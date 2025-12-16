from easygui import *

tegelane = enterbox("Sisestage oma tegelase nimi:")
tugevus = integerbox("Sisestage oma tegelase tugevus:", lowerbound = 1, upperbound = 50)
elupunkt = integerbox("Sisestage oma tegelase elu punktid:", lowerbound = 1, upperbound = 100)
if tegelane == None or tugevus == None or elupunkt == None or tegelane == "":
    msgbox("Palun sisestage õigesti!")
else:
    msgbox(tegelane + " Tugevus: " + str(tugevus) + " Elupunktid: " + str(elupunkt))
    

liikumine = ["otse", "paremale", "vasakule", "tagasi"]
vajutati = buttonbox("Valige kuhu liikuda: ", choices = liikumine)
liikumine = ["otse", "paremale", "vasakule", "tagasi"]
vajutati = buttonbox("Liikusite ", choices = liikumine)
liikumine = ["otse", "paremale", "vasakule", "tagasi"]
vajutati = buttonbox("Liikusite ", choices = liikumine)
