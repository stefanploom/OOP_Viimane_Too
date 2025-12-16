import random
class Karakter:
    def __init__(self, nimi, karakteriElud:float, karakteriTugevus:int):
        self.nimi = nimi
        self.karakteriElud = karakteriElud
        self.karakteriTugevus = karakteriTugevus
    
    def kaotaElusi(self):
        karakteriElud -= vaenlaseTugevus
        print(self.nimi + "kaotas elusid, nüüd tal on" + self.karakteriElud + "elusid")
        
class Vaenlane:
    def __init__(self, vaenlaseElud:int, vaenlaseTugevus:float):
        self.vaenlaseElud = vaenlaseElud
        self.vaenlaseTugevus = vaenlaseTugevus
        
k1=Karakter("juhan",2,10)
v1=Vaenlane(125,1)
v2=Vaenlane(41, 6.7)
k1.kaotaElusi