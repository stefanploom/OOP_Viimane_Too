import sys
class Karakter:
    def __init__(self, nimi, elud:int, tugevus:int):
        self.nimi = nimi
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kogus:int):
        self.elud -= kogus
        if self.elud <= 0:

    def lisaElusi(self, kogus:int):
        self.elud += kogus
       
class Vaenlane:
    def __init__(self, elud:int, tugevus:int):
        self.elud = elud
        self.tugevus = tugevus

    def kaotaElusi(self, kogus:int):
        self.elud -= kogus


